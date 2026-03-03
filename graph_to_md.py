#!/usr/bin/env python3
"""
graph_to_md.py — Flatten Knowledge Graph → LLM-optimized Markdown

Converts the code-architecture knowledge graph JSON (v7) into a structured
Markdown document that any LLM can quickly parse to understand:
  - Product suite hierarchy & cross-product connections
  - Module architecture & internal dependencies per product
  - Semantic dependency breakdown (model refs, const refs, task deps, API clients)
  - Frontend → Backend mapping
  - Infrastructure dependencies
  - Shared services
  - Cross-product data flows (API calls & data sync)
  - Impact analysis (high-impact modules, hub modules, change chains)

Usage:
    python3 graph_to_md.py                          # uses /tmp/graph_data_v7.json
    python3 graph_to_md.py --input my_graph.json    # custom input
    python3 graph_to_md.py --output my_output.md    # custom output
"""

import json
import argparse
from collections import defaultdict, Counter
from datetime import datetime

# ============================================================
# Config
# ============================================================
DEFAULT_INPUT = "/tmp/graph_data_v7.json"
DEFAULT_OUTPUT = "knowledge_graph.md"

PRODUCT_ORDER = ["MAAC", "CAAC", "DAAC", "CDH"]
PRODUCT_REPOS = {
    "MAAC": "rubato (Python/Django) + Grazioso (React/TS)",
    "CAAC": "cantata (Go) + Zeffiroso (React/TS)",
    "DAAC": "bebop (Python/FastAPI)",
    "CDH": "polyrhythmic (Python+Go)",
}

# Semantic edge categories
SEMANTIC_DEP_TYPES = {
    "model_ref":  "Model Reference — imports Django/Go models from another module",
    "const_ref":  "Constant Reference — imports settings, constants, or enums",
    "task_dep":   "Task Dependency — calls or enqueues a Celery/async task",
    "api_client": "API Client — uses an HTTP client to call another service",
}
CODE_DEP_TYPES = ["code_dep", "model_ref", "const_ref", "task_dep", "api_client"]

# ── Deep-link base URL (Vercel deployment) ──
GRAPH_BASE_URL = "https://doc-2-md.vercel.app/"


def node_url(label):
    """Generate a deep-link URL that opens the knowledge graph focused on this node."""
    from urllib.parse import quote
    return f"{GRAPH_BASE_URL}#node={quote(label)}"


def linked(label, raw_label=None):
    """Return Markdown link: [label](deep-link-url)"""
    target = raw_label or label
    return f"[{label}]({node_url(target)})"


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


def short_label(label):
    """Extract short module name: 'maac/accounts' → 'accounts'"""
    return label.split("/")[-1] if "/" in label else label


def clean_page(label):
    """Remove prefix like 'page/' or 'caac_page/' from frontend page labels."""
    return label.split("/", 1)[-1] if "/" in label else label


def render(data):
    nid, ntype, out, inc = build_index(data)
    lines = []
    w = lines.append

    # Edge type statistics
    edge_counts = Counter(e["type"] for e in data["edges"])

    # ============================================================
    # HEADER
    # ============================================================
    w("# Crescendo Lab — Code Architecture Knowledge Graph v7 (LLM-Optimized)")
    w("")
    w(f"> Auto-generated from deep codebase analysis on {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    w(f"> Repos: rubato (MAAC BE), Grazioso (MAAC FE), cantata (CAAC BE), Zeffiroso (CAAC FE), bebop (DAAC), polyrhythmic (CDH)")
    w(f"> Nodes: {len(data['nodes'])} | Edges: {len(data['edges'])}")
    w(f"> Edge breakdown: {', '.join(f'{k}={v}' for k, v in sorted(edge_counts.items(), key=lambda x: -x[1]))}")
    w("> Purpose: Verified architecture map with semantic dependency types — for LLM impact analysis, attribution & root-cause tracing.")
    w(f"> 🔗 Interactive graph: {GRAPH_BASE_URL}")
    w("")
    w("**📌 Deep-link convention:** Every module, product, infrastructure, and frontend page name in this document is a clickable link.")
    w(f"Links follow the pattern `{GRAPH_BASE_URL}#node=<label>` and open the interactive knowledge graph focused on that node.")
    w("When referencing a module in conversation, include its link so the user can jump directly to the interactive view.")
    w("")
    w("---")
    w("")

    # ============================================================
    # 1. PRODUCT SUITE
    # ============================================================
    w("## 1. Product Suite")
    w("")
    products = sorted(
        ntype.get("product", []),
        key=lambda n: PRODUCT_ORDER.index(n["label"]) if n["label"] in PRODUCT_ORDER else 99,
    )

    for p in products:
        w(f"### {linked(p['label'])}")
        w(f"- **{p['label']}**: {p.get('desc', '')}")
        title = p.get("title", "")
        if title:
            w(f"- Tech: {title}")
        w(f"- Repos: {PRODUCT_REPOS.get(p['label'], 'N/A')}")
        w("")

        # Module count
        prod_modules = nodes_for_product(ntype, p["label"], "module")
        prod_pages = nodes_for_product(ntype, p["label"], "frontend_page")
        w(f"- Backend modules: {len(prod_modules)}")
        w(f"- Frontend pages: {len(prod_pages)}")

        # Cross-product API calls and data syncs
        cross_out = [(e, t) for e, t in out[p["id"]] if t["type"] == "product" and e["type"] in ("api_call", "data_sync")]
        cross_in = [(e, f) for e, f in inc[p["id"]] if f["type"] == "product" and e["type"] in ("api_call", "data_sync")]
        if cross_out or cross_in:
            w("")
            w("**Cross-product connections:**")
            for e, t in cross_out:
                label = e.get("label", "").replace("\n", " ")
                w(f"- → {linked(t['label'])}: {label}")
            for e, f in cross_in:
                label = e.get("label", "").replace("\n", " ")
                w(f"- ← {linked(f['label'])}: {label}")
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
        w(f"### {prod} Modules ({len(modules)} total)")
        w("")
        w("| Module | Description | code_dep | model_ref | const_ref | task_dep | api_client |")
        w("|--------|-------------|----------|-----------|-----------|----------|------------|")

        for mod in modules:
            desc = mod.get("desc", "").replace("\n", " ").replace("|", "\\|")[:60]
            short = short_label(mod["label"])
            lnk = linked(short, mod["label"])

            # Count semantic dep types (outgoing)
            dep_counts = Counter()
            for e, t in out[mod["id"]]:
                if e["type"] in CODE_DEP_TYPES and t["type"] == "module":
                    dep_counts[e["type"]] += 1

            cd = dep_counts.get("code_dep", 0) or ""
            mr = dep_counts.get("model_ref", 0) or ""
            cr = dep_counts.get("const_ref", 0) or ""
            td = dep_counts.get("task_dep", 0) or ""
            ac = dep_counts.get("api_client", 0) or ""

            w(f"| **{lnk}** | {desc} | {cd} | {mr} | {cr} | {td} | {ac} |")

        w("")

    # ============================================================
    # 3. SEMANTIC DEPENDENCY TYPES (new in v7)
    # ============================================================
    w("## 3. Semantic Dependency Types")
    w("")
    w("v7 differentiates generic `code_dep` into fine-grained relationship types:")
    w("")
    for etype, desc in SEMANTIC_DEP_TYPES.items():
        cnt = edge_counts.get(etype, 0)
        w(f"- **`{etype}`** ({cnt} edges) — {desc}")
    w(f"- **`code_dep`** ({edge_counts.get('code_dep', 0)} edges) — General Python/Go import dependency (catch-all)")
    w("")

    # Per-product semantic breakdown
    w("### Semantic Dependency Distribution by Product")
    w("")
    w("| Product | code_dep | model_ref | const_ref | task_dep | api_client | Total |")
    w("|---------|----------|-----------|-----------|----------|------------|-------|")

    for prod in PRODUCT_ORDER:
        modules = nodes_for_product(ntype, prod, "module")
        mod_ids = {m["id"] for m in modules}
        pcounts = Counter()
        for e in data["edges"]:
            if e["type"] in CODE_DEP_TYPES and e["from"] in nid and e["to"] in nid:
                from_node = nid[e["from"]]
                if from_node.get("product") == prod and from_node["type"] == "module":
                    pcounts[e["type"]] += 1
        total = sum(pcounts.values())
        w(f"| **{prod}** | {pcounts.get('code_dep',0)} | {pcounts.get('model_ref',0)} | {pcounts.get('const_ref',0)} | {pcounts.get('task_dep',0)} | {pcounts.get('api_client',0)} | {total} |")

    w("")

    # ============================================================
    # 4. MODULE DETAILS
    # ============================================================
    w("## 4. Module Details")
    w("")

    for prod in PRODUCT_ORDER:
        modules = nodes_for_product(ntype, prod, "module")
        for mod in modules:
            short = short_label(mod["label"])
            w(f"### {linked(f'{prod}/{short}', mod['label'])}")
            w(f"- **Product**: {linked(prod)}")
            desc = mod.get("desc", "")
            if desc:
                w(f"- **Description**: {desc}")

            # Group outgoing deps by edge type
            deps_by_type = defaultdict(list)
            for e, t in out[mod["id"]]:
                if e["type"] in CODE_DEP_TYPES and t["type"] == "module":
                    deps_by_type[e["type"]].append((short_label(t["label"]), t["label"]))

            for etype in CODE_DEP_TYPES:
                targets = sorted(set(deps_by_type.get(etype, [])), key=lambda x: x[0])
                if targets:
                    links = ", ".join(linked(s, r) for s, r in targets)
                    w(f"- **{etype}** → {links}")

            # Imported by (all code dep types incoming)
            importers_by_type = defaultdict(list)
            for e, f in inc[mod["id"]]:
                if e["type"] in CODE_DEP_TYPES and f["type"] == "module":
                    importers_by_type[e["type"]].append((short_label(f["label"]), f["label"]))

            for etype in CODE_DEP_TYPES:
                sources = sorted(set(importers_by_type.get(etype, [])), key=lambda x: x[0])
                if sources:
                    links = ", ".join(linked(s, r) for s, r in sources)
                    w(f"- **← {etype}** from: {links}")

            # Frontend pages
            pages_out = [(clean_page(t["label"]), t["label"]) for e, t in out[mod["id"]] if t["type"] == "frontend_page"]
            pages_in = [(clean_page(f["label"]), f["label"]) for e, f in inc[mod["id"]] if f["type"] == "frontend_page"]
            all_pages = sorted(set(pages_out + pages_in), key=lambda x: x[0])
            if all_pages:
                links = ", ".join(linked(s, r) for s, r in all_pages)
                w(f"- **Frontend pages**: {links}")

            # Infrastructure deps
            infra_out = [(t["label"], t["label"]) for e, t in out[mod["id"]] if t["type"] == "infra"]
            infra_deps = sorted(set(infra_out), key=lambda x: x[0])
            if infra_deps:
                links = ", ".join(linked(s, r) for s, r in infra_deps)
                w(f"- **Infrastructure**: {links}")

            # Shared services
            svc_out = [(t["label"], t["label"]) for e, t in out[mod["id"]] if t["type"] == "shared_service"]
            svc_deps = sorted(set(svc_out), key=lambda x: x[0])
            if svc_deps:
                links = ", ".join(linked(s, r) for s, r in svc_deps)
                w(f"- **Shared services**: {links}")

            w("")

    # ============================================================
    # 5. FRONTEND → BACKEND MAPPING
    # ============================================================
    w("## 5. Frontend → Backend Mapping")
    w("")

    for prod in PRODUCT_ORDER:
        pages = nodes_for_product(ntype, prod, "frontend_page")
        if not pages:
            continue
        w(f"### {prod} Frontend Pages")
        w("")
        w("| Page | Calls Backend Modules |")
        w("|------|----------------------|")

        for page in pages:
            page_name = clean_page(page["label"])
            page_lnk = linked(page_name, page["label"])
            mods_out = [(short_label(t["label"]), t["label"]) for e, t in out[page["id"]] if t["type"] == "module"]
            mods_in = [(short_label(f["label"]), f["label"]) for e, f in inc[page["id"]] if f["type"] == "module"]
            all_mods = sorted(set(mods_out + mods_in), key=lambda x: x[0])
            mods_str = ", ".join(linked(s, r) for s, r in all_mods) if all_mods else "—"
            w(f"| {page_lnk} | {mods_str} |")

        w("")

    # Orphan pages
    orphan_pages = [n for n in ntype.get("frontend_page", []) if not n.get("product")]
    if orphan_pages:
        w("### Other Frontend Pages")
        w("")
        w("| Page | Calls Backend Modules |")
        w("|------|----------------------|")
        for page in sorted(orphan_pages, key=lambda n: n["label"]):
            page_name = clean_page(page["label"])
            page_lnk = linked(page_name, page["label"])
            mods_out = [(short_label(t["label"]), t["label"]) for e, t in out[page["id"]] if t["type"] == "module"]
            mods_in = [(short_label(f["label"]), f["label"]) for e, f in inc[page["id"]] if f["type"] == "module"]
            all_mods = sorted(set(mods_out + mods_in), key=lambda x: x[0])
            mods_str = ", ".join(linked(s, r) for s, r in all_mods) if all_mods else "—"
            w(f"| {page_lnk} | {mods_str} |")
        w("")

    # ============================================================
    # 6. INFRASTRUCTURE DEPENDENCIES
    # ============================================================
    w("## 6. Infrastructure Dependencies")
    w("")
    w("| Infrastructure | Description | Used by Products |")
    w("|---------------|-------------|-----------------|")

    infras = sorted(ntype.get("infra", []), key=lambda n: n["label"])
    for infra in infras:
        desc = infra.get("desc", "").replace("\n", " ").replace("|", "\\|")
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
        user_links = ", ".join(linked(u) for u in sorted(users, key=lambda x: PRODUCT_ORDER.index(x) if x in PRODUCT_ORDER else 99))
        w(f"| **{linked(infra['label'])}** | {desc} | {user_links} |")

    w("")

    # ============================================================
    # 7. SHARED SERVICES
    # ============================================================
    w("## 7. Shared Services")
    w("")

    shared = sorted(ntype.get("shared_service", []), key=lambda n: n["label"])
    for svc in shared:
        w(f"### {linked(svc['label'])}")
        desc = svc.get("desc", "")
        if desc:
            w(f"- {desc}")
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
            user_links = ", ".join(linked(u) for u in sorted(users, key=lambda x: PRODUCT_ORDER.index(x) if x in PRODUCT_ORDER else 99))
            w(f"- Used by: {user_links}")
        # Show which modules connect to this service
        mod_users_raw = sorted(set(
            (short_label(f["label"]), f["label"])
            for e, f in inc[svc["id"]]
            if f["type"] == "module"
        ), key=lambda x: x[0])
        if mod_users_raw:
            links = ", ".join(linked(s, r) for s, r in mod_users_raw)
            w(f"- Module consumers: {links}")
        w("")

    # ============================================================
    # 8. CROSS-PRODUCT DATA FLOW
    # ============================================================
    w("## 8. Cross-Product Data Flow")
    w("")

    api_calls = [e for e in data["edges"] if e["type"] == "api_call"]
    data_syncs = [e for e in data["edges"] if e["type"] == "data_sync"]

    if api_calls:
        w("### API Calls")
        w("")
        w("```")
        for e in api_calls:
            fn = nid.get(e["from"], {})
            tn = nid.get(e["to"], {})
            if fn and tn:
                label = e.get("label", "").replace("\n", " ")
                from_label = fn["label"]
                to_label = tn["label"]
                if fn["type"] == "product":
                    from_label = f"{fn['label']} ({PRODUCT_REPOS.get(fn['label'], '')})"
                if tn["type"] == "product":
                    to_label = f"{tn['label']} ({PRODUCT_REPOS.get(tn['label'], '')})"
                w(f"{from_label} ──[API]──→ {to_label}  ({label})")
        w("```")
        w("")

    if data_syncs:
        w("### Data Sync")
        w("")
        w("```")
        for e in data_syncs:
            fn = nid.get(e["from"], {})
            tn = nid.get(e["to"], {})
            if fn and tn:
                label = e.get("label", "").replace("\n", " ")
                w(f"{fn['label']} ──[SYNC]──→ {tn['label']}  ({label})")
        w("```")
        w("")

    # ============================================================
    # 9. IMPACT ANALYSIS GUIDE
    # ============================================================
    w("## 9. Impact Analysis Guide")
    w("")

    all_modules = ntype.get("module", [])

    # Compute comprehensive import counts (all code dep types)
    import_count = {}   # module_id → count of modules that import it
    depend_count = {}   # module_id → count of modules it depends on
    import_by_type = defaultdict(lambda: Counter())  # module_id → {etype: count}

    for mod in all_modules:
        importers = [f for e, f in inc[mod["id"]] if e["type"] in CODE_DEP_TYPES and f["type"] == "module"]
        import_count[mod["id"]] = len(importers)

        for e, f in inc[mod["id"]]:
            if e["type"] in CODE_DEP_TYPES and f["type"] == "module":
                import_by_type[mod["id"]][e["type"]] += 1

        dependencies = [t for e, t in out[mod["id"]] if e["type"] in CODE_DEP_TYPES and t["type"] == "module"]
        depend_count[mod["id"]] = len(dependencies)

    # High-impact modules
    w("### High-Impact Modules (most imported by others)")
    w("")
    w("| Module | Product | Imported by N | code_dep | model_ref | const_ref | task_dep | api_client | Risk |")
    w("|--------|---------|---------------|----------|-----------|-----------|----------|------------|------|")

    top_imported = sorted(all_modules, key=lambda n: import_count[n["id"]], reverse=True)
    for mod in top_imported[:20]:
        cnt = import_count[mod["id"]]
        if cnt == 0:
            break
        name = short_label(mod["label"])
        lnk = linked(name, mod["label"])
        prod = mod.get("product", "")
        bt = import_by_type[mod["id"]]
        if cnt >= 14:
            risk = "🔴 Critical"
        elif cnt >= 7:
            risk = "🟡 High"
        elif cnt >= 3:
            risk = "🟠 Medium"
        else:
            risk = "🟢 Low"
        w(f"| {lnk} | {prod} | {cnt} | {bt.get('code_dep',0)} | {bt.get('model_ref',0)} | {bt.get('const_ref',0)} | {bt.get('task_dep',0)} | {bt.get('api_client',0)} | {risk} |")

    w("")

    # Hub modules (most outgoing deps)
    w("### Hub Modules (most outgoing deps)")
    w("")
    w("| Module | Product | Depends on N | Coupling |")
    w("|--------|---------|-------------|----------|")

    top_deps = sorted(all_modules, key=lambda n: depend_count[n["id"]], reverse=True)
    for mod in top_deps[:15]:
        cnt = depend_count[mod["id"]]
        if cnt == 0:
            break
        name = short_label(mod["label"])
        lnk = linked(name, mod["label"])
        prod = mod.get("product", "")
        if cnt >= 14:
            coupling = "🔴 High"
        elif cnt >= 8:
            coupling = "🟡 Medium"
        else:
            coupling = "🟠 Low-Medium"
        w(f"| {lnk} | {prod} | {cnt} | {coupling} |")

    w("")

    # ============================================================
    # 10. CHANGE IMPACT CHAINS
    # ============================================================
    w("## 10. Change Impact Chains")
    w("")
    w("Format: `If you change X → these modules are directly affected`")
    w("")

    for mod in top_imported[:10]:
        cnt = import_count[mod["id"]]
        if cnt == 0:
            break
        name = mod["label"]
        short = short_label(name)

        importers_detail = defaultdict(list)
        for e, f in inc[mod["id"]]:
            if e["type"] in CODE_DEP_TYPES and f["type"] == "module":
                importers_detail[e["type"]].append((short_label(f["label"]), f["label"]))

        w(f"### Changing {linked(short, name)} ({mod.get('product', '')})")
        w(f"Directly affects {cnt} modules:")
        for etype in CODE_DEP_TYPES:
            sources = sorted(set(importers_detail.get(etype, [])), key=lambda x: x[0])
            if sources:
                links = ", ".join(linked(s, r) for s, r in sources)
                w(f"- via `{etype}`: {links}")
        w("")

    # ============================================================
    # 11. PRODUCT DEPENDENCY MATRIX
    # ============================================================
    w("## 11. Product Dependency Matrix")
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
    # 12. MODULE-TO-INFRASTRUCTURE MAPPING
    # ============================================================
    w("## 12. Module-to-Infrastructure Mapping")
    w("")
    w("Which modules depend on which infrastructure components:")
    w("")

    for infra in infras:
        dep_links = []
        for e, f in inc[infra["id"]]:
            if f["type"] == "module":
                dep_links.append((f"{f.get('product','')}/{short_label(f['label'])}", f["label"]))
            elif f["type"] == "product":
                dep_links.append((f["label"], f["label"]))
        if dep_links:
            w(f"### {linked(infra['label'])}")
            desc = infra.get("desc", "")
            if desc:
                w(f"- {desc}")
            links = ", ".join(linked(s, r) for s, r in sorted(dep_links, key=lambda x: x[0]))
            w(f"- **Depended on by**: {links}")
            w("")

    # ============================================================
    # 13. SEMANTIC DEPENDENCY HOTSPOTS
    # ============================================================
    w("## 13. Semantic Dependency Hotspots")
    w("")
    w("Modules with the most fine-grained semantic dependencies (model_ref + const_ref + task_dep + api_client):")
    w("")

    semantic_scores = []
    for mod in all_modules:
        score = 0
        breakdown = Counter()
        for e, t in out[mod["id"]]:
            if e["type"] in SEMANTIC_DEP_TYPES:
                score += 1
                breakdown[e["type"]] += 1
        for e, f in inc[mod["id"]]:
            if e["type"] in SEMANTIC_DEP_TYPES:
                score += 1
                breakdown[e["type"]] += 1
        if score > 0:
            semantic_scores.append((mod, score, breakdown))

    semantic_scores.sort(key=lambda x: -x[1])

    w("| Module | Product | Total Semantic Edges | model_ref | const_ref | task_dep | api_client |")
    w("|--------|---------|---------------------|-----------|-----------|----------|------------|")
    for mod, score, bd in semantic_scores[:20]:
        name = short_label(mod["label"])
        lnk = linked(name, mod["label"])
        prod = mod.get("product", "")
        w(f"| {lnk} | {prod} | {score} | {bd.get('model_ref',0)} | {bd.get('const_ref',0)} | {bd.get('task_dep',0)} | {bd.get('api_client',0)} |")

    w("")

    # ============================================================
    # FOOTER
    # ============================================================
    w("---")
    w("*End of Code Architecture Knowledge Graph v7*")

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
