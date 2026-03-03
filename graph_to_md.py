#!/usr/bin/env python3
"""
graph_to_md.py — Flatten Knowledge Graph → LLM-optimized Markdown

Converts the code-architecture knowledge graph JSON into a structured
Markdown document that any LLM can quickly parse to understand:
  - Product suite hierarchy & cross-product connections
  - Module architecture & internal dependencies per product
  - Frontend → Backend mapping
  - Infrastructure dependencies
  - Shared services
  - Cross-product data flows (API calls & data sync)
  - Impact analysis (high-impact modules, hub modules, change chains)

Usage:
    python3 graph_to_md.py                          # uses /tmp/graph_data_v6.json
    python3 graph_to_md.py --input my_graph.json    # custom input
    python3 graph_to_md.py --output my_output.md    # custom output
"""

import json
import argparse
from collections import defaultdict
from datetime import datetime

# ============================================================
# Config
# ============================================================
DEFAULT_INPUT = "/tmp/graph_data_v6.json"
DEFAULT_OUTPUT = "knowledge_graph.md"

PRODUCT_ORDER = ["MAAC", "CAAC", "DAAC", "CDH"]
PRODUCT_REPOS = {
    "MAAC": "rubato (Python/Django) + Grazioso (React/TS)",
    "CAAC": "cantata (Go) + Zeffiroso (React/TS)",
    "DAAC": "bebop (Python/FastAPI)",
    "CDH": "polyrhythmic (Python+Go)",
}


def load_graph(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_index(data):
    """Build lookup tables for fast traversal."""
    nodes_by_id = {n["id"]: n for n in data["nodes"]}
    nodes_by_type = defaultdict(list)
    for n in data["nodes"]:
        nodes_by_type[n["type"]].append(n)

    outgoing = defaultdict(list)  # from_id → [(edge, to_node)]
    incoming = defaultdict(list)  # to_id → [(edge, from_node)]
    for e in data["edges"]:
        f, t = e["from"], e["to"]
        if f in nodes_by_id and t in nodes_by_id:
            outgoing[f].append((e, nodes_by_id[t]))
            incoming[t].append((e, nodes_by_id[f]))

    return nodes_by_id, nodes_by_type, outgoing, incoming


def nodes_for_product(nodes_by_type, product, ntype):
    """Get nodes of a given type belonging to a specific product."""
    return sorted(
        [n for n in nodes_by_type.get(ntype, []) if n.get("product") == product],
        key=lambda n: n["label"],
    )


def render(data):
    nid, ntype, out, inc = build_index(data)
    lines = []
    w = lines.append

    # ============================================================
    # HEADER
    # ============================================================
    w("# Crescendo Lab — Code Architecture Knowledge Graph (LLM-Optimized)")
    w("")
    w(f"> Auto-generated from source code analysis on {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    w(f"> Repos: rubato (MAAC BE), Grazioso (MAAC FE), cantata (CAAC BE), Zeffiroso (CAAC FE), bebop (DAAC), polyrhythmic (CDH)")
    w(f"> Nodes: {len(data['nodes'])} | Edges: {len(data['edges'])}")
    w("> Purpose: Verified architecture map from actual import analysis — for LLM impact analysis & attribution.")
    w("")
    w("---")
    w("")

    # ============================================================
    # 1. PRODUCT SUITE
    # ============================================================
    w("## 1. Product Suite")
    w("")
    products = sorted(ntype.get("product", []), key=lambda n: PRODUCT_ORDER.index(n["label"]) if n["label"] in PRODUCT_ORDER else 99)

    for p in products:
        w(f"### {p['label']}")
        w(f"- **{p['label']}**: {p.get('desc', '')}")
        title = p.get("title", "")
        if title:
            w(f"- Title: {title}")
        w("")

        # Cross-product API calls and data syncs
        cross_out = [(e, t) for e, t in out[p["id"]] if t["type"] == "product" and e["type"] in ("api_call", "data_sync")]
        cross_in = [(e, f) for e, f in inc[p["id"]] if f["type"] == "product" and e["type"] in ("api_call", "data_sync")]
        if cross_out or cross_in:
            w("**Cross-product connections:**")
            for e, t in cross_out:
                label = e.get("label", "").replace("\n", " ")
                w(f"- → {t['label']}: {label}")
            for e, f in cross_in:
                label = e.get("label", "").replace("\n", " ")
                w(f"- ← {f['label']}: {label}")
            w("")

    # ============================================================
    # 2. MODULE ARCHITECTURE (per product)
    # ============================================================
    w("## 2. Module Architecture")
    w("")

    for prod in PRODUCT_ORDER:
        modules = nodes_for_product(ntype, prod, "module")
        if not modules:
            continue
        w(f"### {prod} Modules")
        w("")
        w("| Module | Description | Dependencies (imports) |")
        w("|--------|-------------|----------------------|")

        for mod in modules:
            # code_dep outgoing = this module imports from
            deps_out = sorted(set(
                (t["label"].split("/")[-1] if "/" in t["label"] else t["label"])
                for e, t in out[mod["id"]]
                if e["type"] == "code_dep" and t["type"] == "module"
            ))
            dep_str = ", ".join(deps_out) if deps_out else ""
            desc = mod.get("desc", "").replace("\n", " ").replace("|", "\\|")
            short = mod["label"].split("/")[-1] if "/" in mod["label"] else mod["label"]
            w(f"| **{short}** | {desc} | {dep_str} |")

        w("")

    # ============================================================
    # 3. MODULE DETAILS
    # ============================================================
    w("## 3. Module Details")
    w("")

    for prod in PRODUCT_ORDER:
        modules = nodes_for_product(ntype, prod, "module")
        for mod in modules:
            # label is already like "maac/accounts", use short name for header
            short = mod["label"].split("/")[-1] if "/" in mod["label"] else mod["label"]
            w(f"### {prod}/{short}")
            w(f"- **Product**: {prod}")
            w(f"- **Description**: {mod.get('desc', '')}")

            # Imports from (code_dep outgoing to other modules)
            imports_from = sorted(set(
                (t["label"].split("/")[-1] if "/" in t["label"] else t["label"])
                for e, t in out[mod["id"]]
                if e["type"] == "code_dep" and t["type"] == "module"
            ))
            if imports_from:
                w(f"- **Imports from**: {', '.join(imports_from)}")

            # Imported by (code_dep incoming from other modules)
            imported_by = sorted(set(
                (f["label"].split("/")[-1] if "/" in f["label"] else f["label"])
                for e, f in inc[mod["id"]]
                if e["type"] == "code_dep" and f["type"] == "module"
            ))
            if imported_by:
                w(f"- **Imported by**: {', '.join(imported_by)}")

            # Frontend pages (hierarchy edges to frontend_page nodes)
            def clean_page(lbl):
                """Remove prefix like 'page/' or 'caac_page/' from frontend page labels."""
                if "/" in lbl:
                    return lbl.split("/", 1)[-1]
                return lbl

            pages = sorted(set(
                clean_page(t["label"]) for e, t in out[mod["id"]]
                if t["type"] == "frontend_page"
            ))
            # Also check incoming from frontend pages
            pages_inc = sorted(set(
                clean_page(f["label"]) for e, f in inc[mod["id"]]
                if f["type"] == "frontend_page"
            ))
            all_pages = sorted(set(pages + pages_inc))
            if all_pages:
                w(f"- **Frontend pages**: {', '.join(all_pages)}")

            # Infrastructure deps
            infra_deps = sorted(set(
                t["label"] for e, t in out[mod["id"]]
                if t["type"] == "infra"
            ))
            if infra_deps:
                w(f"- **Infrastructure**: {', '.join(infra_deps)}")

            w("")

    # ============================================================
    # 4. FRONTEND → BACKEND MAPPING
    # ============================================================
    w("## 4. Frontend → Backend Mapping")
    w("")

    for prod in PRODUCT_ORDER:
        pages = nodes_for_product(ntype, prod, "frontend_page")
        if not pages:
            # Also check pages without product assigned
            continue
        w(f"### {prod} Frontend Pages")
        w("")
        w("| Page | Calls Backend Modules |")
        w("|------|----------------------|")

        for page in pages:
            page_name = page["label"].split("/", 1)[-1] if "/" in page["label"] else page["label"]
            # hierarchy edges from page to modules
            backend_mods = sorted(set(
                (t["label"].split("/")[-1] if "/" in t["label"] else t["label"])
                for e, t in out[page["id"]]
                if t["type"] == "module"
            ))
            # Also check incoming
            backend_mods_inc = sorted(set(
                (f["label"].split("/")[-1] if "/" in f["label"] else f["label"])
                for e, f in inc[page["id"]]
                if f["type"] == "module"
            ))
            all_mods = sorted(set(backend_mods + backend_mods_inc))
            w(f"| {page_name} | {', '.join(all_mods) if all_mods else '—'} |")

        w("")

    # Also handle pages without product
    orphan_pages = [n for n in ntype.get("frontend_page", []) if not n.get("product")]
    if orphan_pages:
        w("### Other Frontend Pages")
        w("")
        w("| Page | Calls Backend Modules |")
        w("|------|----------------------|")
        for page in sorted(orphan_pages, key=lambda n: n["label"]):
            page_name = page["label"].split("/", 1)[-1] if "/" in page["label"] else page["label"]
            backend_mods = sorted(set(
                (t["label"].split("/")[-1] if "/" in t["label"] else t["label"])
                for e, t in out[page["id"]]
                if t["type"] == "module"
            ))
            backend_mods_inc = sorted(set(
                (f["label"].split("/")[-1] if "/" in f["label"] else f["label"])
                for e, f in inc[page["id"]]
                if f["type"] == "module"
            ))
            all_mods = sorted(set(backend_mods + backend_mods_inc))
            w(f"| {page_name} | {', '.join(all_mods) if all_mods else '—'} |")
        w("")

    # ============================================================
    # 5. INFRASTRUCTURE DEPENDENCIES
    # ============================================================
    w("## 5. Infrastructure Dependencies")
    w("")
    w("| Infrastructure | Description | Used by Products |")
    w("|---------------|-------------|-----------------|")

    infras = sorted(ntype.get("infra", []), key=lambda n: n["label"])
    for infra in infras:
        desc = infra.get("desc", "").replace("\n", " ").replace("|", "\\|")
        # Find which products use this infra
        users = set()
        for e, f in inc[infra["id"]]:
            if f["type"] == "product":
                users.add(f["label"])
            elif f.get("product"):
                users.add(f["product"])
        for e, t in out[infra["id"]]:
            if t["type"] == "product":
                users.add(t["label"])
            elif t.get("product"):
                users.add(t["product"])
        user_str = ", ".join(sorted(users, key=lambda x: PRODUCT_ORDER.index(x) if x in PRODUCT_ORDER else 99))
        w(f"| **{infra['label']}** | {desc} | {user_str} |")

    w("")

    # ============================================================
    # 6. SHARED SERVICES
    # ============================================================
    w("## 6. Shared Services")
    w("")

    shared = sorted(ntype.get("shared_service", []), key=lambda n: n["label"])
    for svc in shared:
        w(f"### {svc['label']}")
        desc = svc.get("desc", "")
        if desc:
            w(f"- {desc}")
        # Find which products use this service
        users = set()
        for e, f in inc[svc["id"]]:
            if f["type"] == "product":
                users.add(f["label"])
            elif f.get("product"):
                users.add(f["product"])
        for e, t in out[svc["id"]]:
            if t["type"] == "product":
                users.add(t["label"])
            elif t.get("product"):
                users.add(t["product"])
        if users:
            user_str = ", ".join(sorted(users, key=lambda x: PRODUCT_ORDER.index(x) if x in PRODUCT_ORDER else 99))
            w(f"- Used by: {user_str}")
        w("")

    # ============================================================
    # 7. CROSS-PRODUCT DATA FLOW
    # ============================================================
    w("## 7. Cross-Product Data Flow")
    w("")
    w("```")

    api_calls = [e for e in data["edges"] if e["type"] == "api_call"]
    data_syncs = [e for e in data["edges"] if e["type"] == "data_sync"]

    for e in api_calls + data_syncs:
        fn = nid.get(e["from"], {})
        tn = nid.get(e["to"], {})
        if fn and tn:
            label = e.get("label", "").replace("\n", " ")
            from_label = fn["label"]
            to_label = tn["label"]
            # Add repo name context for products
            if fn["type"] == "product":
                from_label = f"{fn['label']} ({PRODUCT_REPOS.get(fn['label'], '')})"
            if tn["type"] == "product":
                to_label = f"{tn['label']} ({PRODUCT_REPOS.get(tn['label'], '')})"
            edge_type = "API" if e["type"] == "api_call" else "DATA_SYNC"
            w(f"{from_label} ──[{edge_type}]──→ {to_label}  ({label})")

    w("```")
    w("")

    # ============================================================
    # 8. IMPACT ANALYSIS GUIDE
    # ============================================================
    w("## 8. Impact Analysis Guide")
    w("")

    # Calculate import counts for all modules
    all_modules = ntype.get("module", [])
    import_count = {}  # module_id → count of modules that import it
    depend_count = {}  # module_id → count of modules it depends on

    for mod in all_modules:
        # How many other modules import this one (incoming code_dep)
        importers = [f for e, f in inc[mod["id"]] if e["type"] == "code_dep" and f["type"] == "module"]
        import_count[mod["id"]] = len(importers)

        # How many other modules this one depends on (outgoing code_dep)
        dependencies = [t for e, t in out[mod["id"]] if e["type"] == "code_dep" and t["type"] == "module"]
        depend_count[mod["id"]] = len(dependencies)

    # High-impact modules (most imported by others)
    w("### High-Impact Modules (most imported by others)")
    w("")
    w("| Module | Imported by N modules | Risk |")
    w("|--------|----------------------|------|")

    top_imported = sorted(all_modules, key=lambda n: import_count[n["id"]], reverse=True)
    for mod in top_imported[:15]:
        cnt = import_count[mod["id"]]
        if cnt == 0:
            break
        name = mod["label"]
        if cnt >= 14:
            risk = "🔴 Critical"
        elif cnt >= 7:
            risk = "🟡 High"
        elif cnt >= 3:
            risk = "🟠 Medium"
        else:
            risk = "🟢 Low"
        w(f"| {name} | {cnt} | {risk} |")

    w("")

    # Hub modules (most outgoing deps)
    w("### Hub Modules (most outgoing deps)")
    w("")
    w("| Module | Depends on N modules | Coupling |")
    w("|--------|---------------------|----------|")

    top_deps = sorted(all_modules, key=lambda n: depend_count[n["id"]], reverse=True)
    for mod in top_deps[:15]:
        cnt = depend_count[mod["id"]]
        if cnt == 0:
            break
        name = mod["label"]
        if cnt >= 14:
            coupling = "🔴 High"
        elif cnt >= 8:
            coupling = "🟡 Medium"
        else:
            coupling = "🟠 Low-Medium"
        w(f"| {name} | {cnt} | {coupling} |")

    w("")

    # ============================================================
    # 9. CHANGE IMPACT CHAINS
    # ============================================================
    w("## 9. Change Impact Chains")
    w("")
    w("Format: `If you change X → these modules are directly affected`")
    w("")

    # Show change impact for top 10 most-imported modules
    for mod in top_imported[:10]:
        cnt = import_count[mod["id"]]
        if cnt == 0:
            break
        name = mod["label"]

        importers = sorted(set(
            f["label"]
            for e, f in inc[mod["id"]]
            if e["type"] == "code_dep" and f["type"] == "module"
        ))

        w(f"### Changing `{name}`")
        w(f"Directly affects {cnt} modules:")
        for imp in importers:
            w(f"- {imp}")
        w("")

    # ============================================================
    # 10. PRODUCT DEPENDENCY MATRIX
    # ============================================================
    w("## 10. Product Dependency Matrix")
    w("")
    w("Summary of how each product connects to others:")
    w("")
    w("| From \\ To | MAAC | CAAC | DAAC | CDH |")
    w("|-----------|------|------|------|-----|")

    product_nodes = {p["label"]: p for p in ntype.get("product", [])}
    for from_prod in PRODUCT_ORDER:
        fp = product_nodes.get(from_prod)
        if not fp:
            continue
        cells = []
        for to_prod in PRODUCT_ORDER:
            if from_prod == to_prod:
                cells.append("—")
                continue
            tp = product_nodes.get(to_prod)
            if not tp:
                cells.append("—")
                continue
            # Check direct edges
            connections = []
            for e, t in out[fp["id"]]:
                if t["id"] == tp["id"]:
                    label = e.get("label", "").replace("\n", " ").strip()
                    connections.append(f"{e['type']}: {label}")
            for e, f in inc[fp["id"]]:
                if f["id"] == tp["id"]:
                    label = e.get("label", "").replace("\n", " ").strip()
                    connections.append(f"←{e['type']}: {label}")
            cells.append("; ".join(connections) if connections else "—")
        w(f"| **{from_prod}** | {' | '.join(cells)} |")

    w("")

    # ============================================================
    # 11. MODULE-TO-INFRASTRUCTURE MAPPING
    # ============================================================
    w("## 11. Module-to-Infrastructure Mapping")
    w("")
    w("Which modules depend on which infrastructure components:")
    w("")

    for infra in infras:
        dependents = []
        for e, f in inc[infra["id"]]:
            if f["type"] == "module":
                dependents.append(f["label"])
            elif f["type"] == "product":
                dependents.append(f["label"])
        if dependents:
            w(f"### {infra['label']}")
            desc = infra.get("desc", "")
            if desc:
                w(f"- {desc}")
            w(f"- **Depended on by**: {', '.join(sorted(dependents))}")
            w("")

    # ============================================================
    # FOOTER
    # ============================================================
    w("---")
    w("*End of Code Architecture Knowledge Graph*")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Flatten knowledge graph to LLM-optimized Markdown")
    parser.add_argument("--input", "-i", default=DEFAULT_INPUT, help="Input graph JSON")
    parser.add_argument("--output", "-o", default=DEFAULT_OUTPUT, help="Output Markdown file")
    args = parser.parse_args()

    print(f"📖 Loading graph from {args.input}")
    data = load_graph(args.input)
    print(f"   Nodes: {len(data['nodes'])} | Edges: {len(data['edges'])}")

    print(f"📝 Generating Markdown...")
    md = render(data)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(md)

    line_count = md.count("\n") + 1
    print(f"✅ Written to {args.output}")
    print(f"   {line_count} lines, {len(md):,} characters")


if __name__ == "__main__":
    main()
