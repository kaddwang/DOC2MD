#!/usr/bin/env python3
"""
graph_to_md.py — Flatten Knowledge Graph → LLM-optimized Markdown

Converts the knowledge graph JSON into a structured Markdown document
that any LLM can quickly parse to understand:
  - Product suite hierarchy
  - Module dependencies & data flows
  - Infrastructure dependencies
  - Root cause taxonomy with causal attribution
  - Issue catalog with Asana traceability

Usage:
    python3 graph_to_md.py                          # uses /tmp/graph_data_v5.json
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
DEFAULT_INPUT = "/tmp/graph_data_v5.json"
DEFAULT_OUTPUT = "knowledge_graph.md"


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


def desc_lines(node):
    """Extract clean description lines."""
    raw = node.get("desc", node.get("label", ""))
    return [l.strip() for l in raw.split("\n") if l.strip() and l.strip() != "---"]


def render(data):
    nid, ntype, out, inc = build_index(data)
    lines = []
    w = lines.append  # shorthand

    # ============================================================
    # HEADER
    # ============================================================
    w("# Crescendo Lab — Knowledge Graph (LLM-Optimized)")
    w("")
    w(f"> Auto-generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    w(f"> Nodes: {len(data['nodes'])} | Edges: {len(data['edges'])}")
    w("> Purpose: Provide LLMs a flattened, structured representation of the CL product suite's")
    w(">          architecture, dependencies, root causes, and issue attribution.")
    w("")
    w("---")
    w("")

    # ============================================================
    # 1. PRODUCT SUITE OVERVIEW
    # ============================================================
    w("## 1. Product Suite Overview")
    w("")
    products = ntype.get("product", [])
    for p in products:
        w(f"### {p['label']}")
        for dl in desc_lines(p):
            w(f"- {dl}")
        # Cross-product relationships
        cross = [(e, t) for e, t in out[p["id"]] if t["type"] == "product"]
        cross += [(e, f) for e, f in inc[p["id"]] if f["type"] == "product"]
        if cross:
            w("")
            w("**Cross-product relationships:**")
            for e, other in cross:
                w(f"- {p['label']} ←{e['label']}→ {other['label']}")
        w("")

    # ============================================================
    # 2. MODULE ARCHITECTURE (per product)
    # ============================================================
    w("## 2. Module Architecture")
    w("")
    w("### MAAC Modules")
    w("")
    w("| Module | Sub-features | Issues | Infra Dependencies |")
    w("|--------|-------------|--------|-------------------|")

    modules = sorted(ntype.get("module", []), key=lambda n: n["label"])
    for mod in modules:
        subs = [t for e, t in out[mod["id"]] if t["type"] == "subfeature"]
        issues = [t for e, t in out[mod["id"]] if t["type"] == "issue"]
        infras = [t for e, t in out[mod["id"]] if t["type"] == "infra"]
        sub_str = ", ".join(s["label"] for s in subs) if subs else "—"
        infra_str = ", ".join(i["label"] for i in infras) if infras else "—"
        w(f"| **{mod['label']}** | {sub_str} | {len(issues)} | {infra_str} |")

    w("")

    # ============================================================
    # 3. MODULE DETAILS + SUB-FEATURES
    # ============================================================
    w("## 3. Module Details")
    w("")
    for mod in modules:
        w(f"### {mod['label']}")
        for dl in desc_lines(mod):
            w(f"- {dl}")
        w("")

        # Sub-features
        subs = [(e, t) for e, t in out[mod["id"]] if t["type"] == "subfeature"]
        if subs:
            w("**Sub-features:**")
            for e, sf in subs:
                sf_desc = " — ".join(desc_lines(sf)[:2])
                w(f"- **{sf['label']}**: {sf_desc}")
            w("")

        # Data flows
        flows_out = [(e, t) for e, t in out[mod["id"]]
                     if e["type"] == "data_flow" and t["type"] == "module"]
        flows_in = [(e, f) for e, f in inc[mod["id"]]
                    if e["type"] == "data_flow" and f["type"] == "module"]
        if flows_out or flows_in:
            w("**Data flows:**")
            for e, t in flows_out:
                w(f"- {mod['label']} → {t['label']} ({e['label']})")
            for e, f in flows_in:
                w(f"- {f['label']} → {mod['label']} ({e['label']})")
            w("")

        # Infra deps
        infras = [(e, t) for e, t in out[mod["id"]] if t["type"] == "infra"]
        if infras:
            w("**Infrastructure dependencies:**")
            for e, i in infras:
                w(f"- {i['label']}")
            w("")

        # Issues summary
        issues = [(e, t) for e, t in out[mod["id"]] if t["type"] == "issue"]
        if issues:
            priority_count = defaultdict(int)
            for e, iss in issues:
                p = iss.get("priority", "?")
                priority_count[p] += 1
            pstr = ", ".join(f"{k}: {v}" for k, v in sorted(priority_count.items()))
            w(f"**Issues ({len(issues)}):** {pstr}")
            w("")

    # ============================================================
    # 4. CROSS-MODULE DEPENDENCY MAP
    # ============================================================
    w("## 4. Cross-Module Dependency Map")
    w("")
    w("This section maps how modules depend on and feed data to each other.")
    w("Use this to understand impact when changing a module.")
    w("")
    w("```")
    w("FROM                  → TO                    RELATIONSHIP")
    w("─────────────────────────────────────────────────────────────")
    data_flows = [e for e in data["edges"] if e["type"] == "data_flow"]
    for e in data_flows:
        fn = nid.get(e["from"], {})
        tn = nid.get(e["to"], {})
        if fn and tn:
            w(f"{fn['label']:22s} → {tn['label']:22s} {e['label']}")
    w("```")
    w("")

    # ============================================================
    # 5. INFRASTRUCTURE MAP
    # ============================================================
    w("## 5. Infrastructure Dependencies")
    w("")
    infras = ntype.get("infra", [])
    for infra in sorted(infras, key=lambda n: n["label"]):
        dependents = [f for e, f in inc[infra["id"]] if f["type"] in ("module", "product")]
        dep_str = ", ".join(d["label"] for d in dependents)
        w(f"### {infra['label']}")
        for dl in desc_lines(infra):
            w(f"- {dl}")
        if dep_str:
            w(f"- **Used by:** {dep_str}")
        w("")

    # ============================================================
    # 6. ROOT CAUSE TAXONOMY
    # ============================================================
    w("## 6. Root Cause Taxonomy")
    w("")
    w("Root causes are clustered from 106 investigation tickets.")
    w("Each cluster represents a systemic pattern that recurs across modules.")
    w("")

    rcs = sorted(ntype.get("rootcause", []),
                 key=lambda n: n.get("count", 0), reverse=True)
    for rc in rcs:
        count = rc.get("count", 0)
        w(f"### {rc['label']} ({count} tickets)")
        for dl in desc_lines(rc):
            w(f"- {dl}")
        w("")

        # Which modules are affected?
        rc_issues = [t for e, t in inc[rc["id"]] if t["type"] == "issue"]
        mod_count = defaultdict(int)
        for iss in rc_issues:
            m = iss.get("module", "Unknown")
            mod_count[m] += 1
        if mod_count:
            w("**Affected modules:**")
            for m, c in sorted(mod_count.items(), key=lambda x: -x[1]):
                w(f"- {m}: {c} tickets")
            w("")

        # Linked infra?
        rc_infras = [t for e, t in out[rc["id"]] if t["type"] == "infra"]
        if rc_infras:
            w(f"**Related infrastructure:** {', '.join(i['label'] for i in rc_infras)}")
            w("")

    # ============================================================
    # 7. ISSUE CATALOG (Attribution Table)
    # ============================================================
    w("## 7. Issue Catalog — Attribution Table")
    w("")
    w("Each issue is linked to its module, root cause cluster, and Asana ticket.")
    w("")

    issues = sorted(ntype.get("issue", []),
                    key=lambda n: (n.get("priority", "Z"), n.get("module", "")))

    # Group by priority
    by_priority = defaultdict(list)
    for iss in issues:
        by_priority[iss.get("priority", "?")].append(iss)

    for priority in ["P0", "P1", "P2", "P3", "P4", "?"]:
        group = by_priority.get(priority, [])
        if not group:
            continue
        w(f"### {priority} Issues ({len(group)})")
        w("")
        w("| Issue | Module | Root Cause | Asana |")
        w("|-------|--------|-----------|-------|")

        for iss in group:
            label = iss["label"].replace("|", "\\|")
            module = iss.get("module", "—")
            # Find root cause
            rc_edges = [(e, t) for e, t in out[iss["id"]] if t["type"] == "rootcause"]
            rc_str = rc_edges[0][1]["label"] if rc_edges else "—"
            asana = iss.get("asana_url", "")
            asana_str = f"[{iss.get('asana_id', 'link')}]({asana})" if asana else "—"
            w(f"| {label} | {module} | {rc_str} | {asana_str} |")

        w("")

    # ============================================================
    # 8. ATTRIBUTION CHAINS (Impact Paths)
    # ============================================================
    w("## 8. Attribution Chains")
    w("")
    w("These chains show how root causes propagate through the system.")
    w("Format: `Root Cause → Issue → Module → Product`")
    w("")

    for rc in rcs:
        rc_issues = [(e, t) for e, t in inc[rc["id"]] if t["type"] == "issue"]
        if not rc_issues:
            continue
        w(f"### {rc['label']}")
        for e, iss in rc_issues[:15]:  # limit to 15 per RC
            mod = iss.get("module", "?")
            asana = iss.get("asana_url", "")
            chain = f"- `{rc['label']}` → `{iss['label']}` → `{mod}` → MAAC"
            if asana:
                chain += f" | [Asana]({asana})"
            w(chain)
        if len(rc_issues) > 15:
            w(f"- ... +{len(rc_issues) - 15} more")
        w("")

    # ============================================================
    # 9. QUICK REFERENCE — IMPACT ANALYSIS GUIDE
    # ============================================================
    w("## 9. Quick Reference — Impact Analysis Guide")
    w("")
    w("When evaluating a change to any component, use this guide:")
    w("")
    w("| If you change... | Check impact on... |")
    w("|------------------|-------------------|")

    for mod in modules:
        downstream = [t["label"] for e, t in out[mod["id"]]
                      if e["type"] == "data_flow" and t["type"] == "module"]
        upstream = [f["label"] for e, f in inc[mod["id"]]
                    if e["type"] == "data_flow" and f["type"] == "module"]
        infras = [t["label"] for e, t in out[mod["id"]] if t["type"] == "infra"]
        all_impact = downstream + upstream + infras
        if all_impact:
            w(f"| **{mod['label']}** | {', '.join(all_impact)} |")

    w("")
    w("---")
    w("")
    w("*End of Knowledge Graph Document*")

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
