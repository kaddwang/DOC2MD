#!/usr/bin/env python3
"""
Build Knowledge Graph v5 — GitBookLLMv2.md
- Corrected product hierarchy: MAAC, CAAC, DAAC, CDH are same-level products
- Neo4j Bloom-style UI data preparation
"""

import re
import json
from collections import defaultdict

INPUT_FILE = "GitBookLLMv2.md"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    raw = f.read()
lines = raw.split("\n")
total_lines = len(lines)
print(f"📄 Read {total_lines} lines")

# ============================================================
# H1/H2/H3 index
# ============================================================
h1_re = re.compile(r"^\\#\s+(.+)$")
h2_re = re.compile(r"^\\#\\#\s+(.+)$")
h3_re = re.compile(r"^\\#\\#\\#\s+(.+)$")

h1_index, h2_index = [], []
for i, line in enumerate(lines):
    m3 = h3_re.match(line)
    if m3:
        continue
    m2 = h2_re.match(line)
    if m2:
        h2_index.append((i, m2.group(1).strip()))
        continue
    m1 = h1_re.match(line)
    if m1:
        h1_index.append((i, m1.group(1).strip()))

# ============================================================
# Module boundaries
# ============================================================
MODULE_MAP = {
    "Insight": "insight",
    "Contacts": "contacts",
    "Segment": "segment",
    "Tag Manager": "tag_manager",
    "Broadcast": "broadcast",
    "Template Library": "template",
    "Rich Menu": "richmenu",
    "Auto-reply": "autoreply",
    "Deeplink": "deeplink",
    "Smart redirect tool": "smart_redirect",
    "Tracelink": "tracelink",
    "Prize Management": "prize",
    "Customer Journey": "journey",
}

module_positions = [(ln, t) for ln, t in h1_index if t in MODULE_MAP]
module_positions.append((total_lines, "END"))

modules = {}
for i in range(len(module_positions) - 1):
    ln, title = module_positions[i]
    next_ln = module_positions[i + 1][0]
    section_text = "\n".join(lines[ln:next_ln])
    sub_h2 = [(l, t) for l, t in h2_index if l > ln and l < next_ln]
    modules[title] = {
        "key": MODULE_MAP[title],
        "start": ln,
        "end": next_ln,
        "text": section_text,
        "sub_h2": sub_h2,
    }

# ============================================================
# Extract investigation tickets
# ============================================================
def extract_field(field_name, txt):
    pat = re.compile(
        r"\\\*\\\*" + re.escape(field_name) + r":\\\*\\\*\s*(.*?)(?:\s{2,}|\n|$)"
    )
    m = pat.search(txt)
    return m.group(1).strip() if m else ""

def clean_escaped(txt):
    txt = txt.replace("\\*", "").replace("\\#", "").replace("\\_", "_")
    txt = txt.replace("\\[", "[").replace("\\]", "]").replace("\\-", "-")
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt

all_tickets = []
for mod_name, mod_info in modules.items():
    h2s = mod_info["sub_h2"]
    for idx, (ln, title) in enumerate(h2s):
        if not title.startswith("Investigation of") and "Why Can" not in title:
            continue
        rel_end = h2s[idx + 1][0] if idx + 1 < len(h2s) else mod_info["end"]
        section = "\n".join(lines[ln:rel_end])

        feature = clean_escaped(extract_field("Feature", section))
        date = clean_escaped(extract_field("Created At", section))
        priority_raw = clean_escaped(extract_field("Ticket Priority", section))
        priority = priority_raw.split(" ")[0].split("-")[0].strip() if priority_raw else ""
        client = clean_escaped(extract_field("Client Name", section))
        owner = clean_escaped(extract_field("Resolution Owner", section))
        result = clean_escaped(extract_field("Result Breakdown", section))

        asana_m = re.search(r"\\\[(\d{13,})\\\]\((https://app\.asana\.com[^\)]+)\)", section)
        asana_id = asana_m.group(1) if asana_m else ""
        asana_url = asana_m.group(2) if asana_m else ""

        rc_m = re.search(r"\\\*\\\*Root Cause:?\\\*\\\*\s*\n?\s*(.*?)(?=\n\s*\\\*\\\*Solution|\Z)", section, re.DOTALL)
        root_cause = clean_escaped(rc_m.group(1))[:350] if rc_m else ""

        sol_m = re.search(r"\\\*\\\*Solution:?\\\*\\\*\s*\n?\s*(.*?)(?=\n\s*\\\*\\\*Status|\n\s*\\\*\\\*Action|\n\*\*\*|\n\\#|\Z)", section, re.DOTALL)
        solution = clean_escaped(sol_m.group(1))[:350] if sol_m else ""

        desc_m = re.search(r"Issue Description\s*\n\s*(.*?)(?=\n\\#\\#\\#|\n\\\*\\\*|\Z)", section, re.DOTALL)
        description = clean_escaped(desc_m.group(1))[:300] if desc_m else ""

        all_tickets.append({
            "module": mod_name,
            "title": title.replace("Investigation of ", ""),
            "feature": feature, "date": date, "priority": priority,
            "client": client, "owner": owner, "result": result,
            "asana_id": asana_id, "asana_url": asana_url,
            "root_cause": root_cause, "solution": solution, "description": description,
        })

print(f"🎫 Tickets: {len(all_tickets)}")

# ============================================================
# Root cause clustering
# ============================================================
RC_CATEGORIES = {
    "airflow_pipeline": (["airflow", "dag", "pipeline", "etl", "bigquery", "data processing", "batch"],
        "Data Pipeline Failure", "Airflow DAG failures, BigQuery sync issues, ETL errors causing missing report data"),
    "data_inconsistency": (["discrepancy", "inconsisten", "mismatch", "data gap", "incorrect data"],
        "Data Inconsistency", "Mismatched metrics between reports/dashboards"),
    "api_external_dep": (["line api", "meta api", "facebook", "instagram", "sendgrid", "external", "third party", "api limit"],
        "External API Dep", "LINE/Meta/SendGrid API changes, rate limits, or policy restrictions"),
    "cache_state": (["cache", "cookie", "session", "stale", "outdated state"],
        "Cache / State Issue", "Stale cache, cookies, or session data"),
    "webhook_sync": (["webhook", "sync", "delay", "timing", "race condition", "event processing"],
        "Webhook / Sync Delay", "Event processing timing, race conditions"),
    "permission_config": (["permission", "config", "setting", "disabled", "enable", "admin", "django"],
        "Config / Permission", "Missing permissions or disabled settings"),
    "product_logic": (["product design", "by design", "expected behavior", "product expectation", "intended"],
        "By Design", "Behavior working as designed but misaligned with user expectations"),
    "resource_constraint": (["too costly", "resource", "infeasible", "not planned", "limitation"],
        "Resource Constraint", "Issues too costly to fix; accepted technical debt"),
    "user_misunderstanding": (["misunderstand", "clarif", "user error", "documentation"],
        "User Misunderstanding", "Customer misunderstanding resolved by documentation"),
    "encoding_format": (["encoding", "format", "character", "emoji", "unicode", "template"],
        "Encoding / Format", "Character encoding, emoji, or template format issues"),
    "quota_limit": (["quota", "limit", "exceeded", "throttle", "cap", "restriction"],
        "Quota / Limit", "System or API quota/rate limit exceeded"),
}

def normalize_rc(txt):
    return re.sub(r"[^a-z0-9\s]", " ", txt.lower()).strip()

rc_clusters = defaultdict(list)
ticket_rc_map = {}
for ticket in all_tickets:
    rc_norm = normalize_rc(ticket["root_cause"])
    assigned = False
    for cat, (keywords, _, _) in RC_CATEGORIES.items():
        if any(kw in rc_norm for kw in keywords):
            rc_clusters[cat].append(ticket["title"][:60])
            ticket_rc_map[ticket["title"]] = cat
            assigned = True
            break
    if not assigned and ticket["root_cause"]:
        rc_clusters["other"].append(ticket["title"][:60])
        ticket_rc_map[ticket["title"]] = "other"

# ============================================================
# Sub-features per module
# ============================================================
MODULE_SUBFEATURES = {
    "Insight": [
        ("Data Overview", "Dashboard with LINE overview, tag coverage, CID binding"),
        ("Deeplink Report", "Tracks new contacts acquired via deeplinks"),
        ("Acquisition Analytics", "New contact acquisition metrics and sources"),
        ("Open Rate Hotspot", "Heatmap of message open rates by day/time"),
        ("Message Analytics", "Track messages sent across channels"),
    ],
    "Contacts": [
        ("Contact Profile", "Unified contact profile with LINE UID, CID, phone, email"),
        ("Profile Unification", "Merge contacts across channels using matching logic"),
        ("Contact Import/Export", "Bulk import/export contacts via CSV or API"),
        ("Email Channel", "Email contact management and sender domain setup"),
        ("Contact Fields", "Custom and system fields on contact profiles"),
    ],
    "Segment": [
        ("AI Segment", "NL prompt-based audience segmentation"),
        ("Segment Filters", "Rule-based segmentation with include/exclude"),
        ("Segment Tag Ops", "Batch tag operations on segments"),
    ],
    "Tag Manager": [
        ("Tag CRUD", "Create, read, update, delete tags"),
        ("Auto Tagging", "Rule-based automatic tag assignment"),
        ("Tag Coverage", "Analytics on tag usage across contacts"),
    ],
    "Broadcast": [
        ("LINE Broadcast", "Push messages to LINE contacts"),
        ("Broadcast Scheduling", "Schedule future broadcast sends"),
        ("Broadcast Report", "Post-send analytics and delivery stats"),
    ],
    "Template Library": [
        ("Message Templates", "Reusable LINE Flex Message templates"),
    ],
    "Rich Menu": [
        ("Rich Menu Editor", "Visual editor for LINE rich menus"),
        ("Rich Menu Scheduling", "Schedule rich menu activation"),
    ],
    "Auto-reply": [
        ("Keyword Auto-reply", "Trigger replies based on keyword matching"),
        ("Web Chat Auto-reply", "Auto-reply for web chat channels"),
        ("Auto-reply Scheduling", "Time-based auto-reply activation"),
        ("New Friend Welcome", "Greeting for new contacts"),
        ("Reply Limit & Dedup", "Rate limiting and deduplication"),
    ],
    "Deeplink": [
        ("Deeplink Generator", "Create trackable deeplinks for LINE"),
        ("UTM Tracking", "UTM parameter support for deeplinks"),
        ("Deeplink Report", "Click and conversion analytics"),
        ("Deeplink QR Code", "QR code generation for deeplinks"),
    ],
    "Smart redirect tool": [
        ("Smart Redirect", "Intelligent URL redirection logic"),
    ],
    "Tracelink": [
        ("Tracelink Short URL", "Short URL generation with tracking"),
        ("LIFF Integration", "LINE Front-end Framework integration"),
        ("CLID Tracking", "Cross-domain customer ID tracking"),
    ],
    "Prize Management": [
        ("Prize Setup", "Configure prizes for campaigns"),
        ("Rapid Referral", "Referral campaign prize distribution"),
        ("Prize Messages", "LINE Flex Message prize notifications"),
    ],
    "Customer Journey": [
        ("Journey Editor", "Visual flow canvas for journey design"),
        ("Journey Triggers", "Event-based triggers (tag, GA, time)"),
        ("Journey Actions", "Message send, tag ops, wait nodes"),
        ("Journey Conditions", "Yes/No branch and filter conditions"),
        ("Journey Report", "Per-node analytics and conversion"),
        ("EDM Integration", "Email channel in journey via SendGrid"),
    ],
}

# ============================================================
# Infrastructure
# ============================================================
INFRA_NODES = [
    ("LINE API", "LINE Messaging API, LIFF, Rich Menu API"),
    ("Meta API", "Facebook & Instagram messaging APIs"),
    ("Airflow", "Apache Airflow for ETL pipelines"),
    ("BigQuery", "Google BigQuery data warehouse"),
    ("PostgreSQL", "Primary relational database"),
    ("SendGrid", "Email delivery service"),
    ("Django Admin", "Admin panel for config management"),
    ("Redis", "Cache layer for session/state"),
    ("LIFF", "LINE Front-end Framework"),
]

# ============================================================
# BUILD GRAPH
# ============================================================
nodes = []
edges = []
nid = [0]
def make_id():
    nid[0] += 1
    return nid[0]

# --- Company node ---
company_id = make_id()
nodes.append({
    "id": company_id, "label": "Crescendo Lab", "type": "company",
    "desc": "Crescendo Lab SaaS Product Suite\nOMO marketing automation platform",
})

# --- Product nodes (same level) ---
PRODUCTS = {
    "MAAC": ("Marketing Automation\n& Analytics Cloud", "Core marketing automation platform — LINE/FB/IG/SMS messaging, automation, analytics"),
    "CAAC": ("Conversation Automation\n& Analytics Cloud", "Real-time chat and conversation management — agent inbox, chatbot, AI assist"),
    "DAAC": ("Data Automation\n& Analytics Cloud", "Data analytics engine — Audience360, predictive models, data enrichment"),
    "CDH": ("Customer Data Hub", "Cross-platform data unification — profile merging, segment engine, data exchange"),
}

product_ids = {}
for prod_name, (subtitle, desc) in PRODUCTS.items():
    pid = make_id()
    nodes.append({
        "id": pid, "label": prod_name, "type": "product",
        "desc": f"{prod_name}\n{subtitle}\n---\n{desc}",
    })
    product_ids[prod_name] = pid
    edges.append({"from": company_id, "to": pid, "label": "product", "type": "hierarchy"})

# Cross-product relationships
CROSS_PRODUCT = [
    ("CDH", "MAAC", "unifies contacts", "CDH unifies contact profiles for MAAC"),
    ("CDH", "CAAC", "unifies contacts", "CDH unifies contact profiles for CAAC"),
    ("DAAC", "MAAC", "provides data", "DAAC Audience360 feeds MAAC AI Segment & analytics"),
    ("DAAC", "CDH", "enriches data", "DAAC enriches CDH with predictive models"),
    ("MAAC", "CAAC", "shares contacts", "MAAC & CAAC share contact profiles via CDH"),
]
for f, t, label, desc in CROSS_PRODUCT:
    if f in product_ids and t in product_ids:
        edges.append({"from": product_ids[f], "to": product_ids[t], "label": label, "type": "data_flow", "desc": desc})

# --- Module nodes (under MAAC) ---
module_ids = {}
for mod_name, mod_key in MODULE_MAP.items():
    mid = make_id()
    inv_count = sum(1 for t in all_tickets if t["module"] == mod_name)
    desc_parts = [f"MAAC Module: {mod_name}"]
    if inv_count:
        desc_parts.append(f"Known issues: {inv_count}")
    nodes.append({
        "id": mid, "label": mod_name, "type": "module",
        "desc": "\n".join(desc_parts),
    })
    module_ids[mod_name] = mid
    edges.append({"from": product_ids["MAAC"], "to": mid, "label": "contains", "type": "hierarchy"})

# --- Sub-feature nodes ---
subfeature_ids = {}
for mod_name, features in MODULE_SUBFEATURES.items():
    if mod_name not in module_ids:
        continue
    for feat_name, feat_desc in features:
        fid = make_id()
        nodes.append({
            "id": fid, "label": feat_name, "type": "subfeature",
            "desc": f"{feat_name}\n{feat_desc}", "module": mod_name,
        })
        subfeature_ids[(mod_name, feat_name)] = fid
        edges.append({"from": module_ids[mod_name], "to": fid, "label": "has", "type": "hierarchy"})

# --- Infrastructure nodes ---
infra_ids = {}
for infra_name, infra_desc in INFRA_NODES:
    iid = make_id()
    nodes.append({
        "id": iid, "label": infra_name, "type": "infra",
        "desc": f"Infrastructure: {infra_name}\n{infra_desc}",
    })
    infra_ids[infra_name] = iid

# --- Root Cause nodes ---
RC_CATEGORIES["other"] = ([], "Other Root Cause", "Other root causes not fitting major categories")
rc_node_ids = {}
for cat, ticket_titles in rc_clusters.items():
    rcid = make_id()
    kw, label, desc = RC_CATEGORIES.get(cat, ([], cat, ""))
    nodes.append({
        "id": rcid, "label": label, "type": "rootcause",
        "desc": f"Root Cause: {label}\n{desc}\nAffected: {len(ticket_titles)} tickets",
        "count": len(ticket_titles),
    })
    rc_node_ids[cat] = rcid

# --- Issue nodes ---
issue_ids = {}
for ticket in all_tickets:
    iid = make_id()
    desc_parts = [ticket["title"]]
    if ticket["priority"]: desc_parts.append(f"Priority: {ticket['priority']}")
    if ticket["date"]: desc_parts.append(f"Date: {ticket['date']}")
    if ticket["client"] and "REDACTED" not in ticket["client"] and ticket["client"] != "N/A":
        desc_parts.append(f"Client: {ticket['client']}")
    if ticket["owner"]: desc_parts.append(f"Owner: {ticket['owner']}")
    if ticket["result"]: desc_parts.append(f"Result: {ticket['result']}")
    if ticket["description"]: desc_parts.append(f"---\n{ticket['description'][:200]}")
    if ticket["root_cause"]: desc_parts.append(f"---\nRoot Cause: {ticket['root_cause'][:200]}")
    if ticket["solution"]: desc_parts.append(f"Solution: {ticket['solution'][:200]}")

    nodes.append({
        "id": iid, "label": ticket["title"][:40], "type": "issue",
        "desc": "\n".join(desc_parts), "module": ticket["module"],
        "priority": ticket["priority"],
        "asana_id": ticket["asana_id"], "asana_url": ticket["asana_url"],
    })
    issue_ids[ticket["title"]] = iid

    # issue -> module
    if ticket["module"] in module_ids:
        edges.append({"from": module_ids[ticket["module"]], "to": iid, "label": "has issue", "type": "issue_rel"})
    # issue -> root cause
    rc_cat = ticket_rc_map.get(ticket["title"])
    if rc_cat and rc_cat in rc_node_ids:
        edges.append({"from": iid, "to": rc_node_ids[rc_cat], "label": "caused by", "type": "causal"})

# --- Cross-module dependencies ---
CROSS_MODULE = [
    ("Contacts", "Segment", "provides data"),
    ("Segment", "Broadcast", "filters audience"),
    ("Template Library", "Broadcast", "provides templates"),
    ("Template Library", "Auto-reply", "provides templates"),
    ("Tag Manager", "Segment", "tags for filtering"),
    ("Tag Manager", "Contacts", "labels contacts"),
    ("Deeplink", "Contacts", "acquires contacts"),
    ("Deeplink", "Insight", "feeds analytics"),
    ("Tracelink", "Deeplink", "wraps URLs"),
    ("Broadcast", "Insight", "feeds metrics"),
    ("Customer Journey", "Broadcast", "sends messages"),
    ("Customer Journey", "Tag Manager", "applies tags"),
    ("Customer Journey", "Segment", "uses segments"),
    ("Auto-reply", "Contacts", "creates contacts"),
    ("Rich Menu", "Deeplink", "links to deeplinks"),
    ("Contacts", "Customer Journey", "enters journey"),
]
for f, t, label in CROSS_MODULE:
    if f in module_ids and t in module_ids:
        edges.append({"from": module_ids[f], "to": module_ids[t], "label": label, "type": "data_flow"})

# --- Infra dependencies ---
INFRA_DEPS = [
    ("Insight", "Airflow"), ("Insight", "BigQuery"), ("Insight", "PostgreSQL"),
    ("Contacts", "LINE API"), ("Contacts", "PostgreSQL"),
    ("Broadcast", "LINE API"), ("Auto-reply", "LINE API"), ("Auto-reply", "Meta API"),
    ("Deeplink", "LIFF"), ("Tracelink", "LIFF"), ("Tracelink", "Redis"),
    ("Customer Journey", "SendGrid"), ("Customer Journey", "Airflow"),
    ("Tag Manager", "PostgreSQL"), ("Prize Management", "LINE API"),
    ("Rich Menu", "LINE API"), ("Segment", "BigQuery"),
]
for mod, infra in INFRA_DEPS:
    if mod in module_ids and infra in infra_ids:
        edges.append({"from": module_ids[mod], "to": infra_ids[infra], "label": "depends on", "type": "infra_dep"})

# RC -> Infra
RC_INFRA = [
    ("airflow_pipeline", "Airflow"), ("airflow_pipeline", "BigQuery"),
    ("api_external_dep", "LINE API"), ("api_external_dep", "Meta API"),
    ("cache_state", "Redis"), ("permission_config", "Django Admin"),
]
for rc_cat, infra in RC_INFRA:
    if rc_cat in rc_node_ids and infra in infra_ids:
        edges.append({"from": rc_node_ids[rc_cat], "to": infra_ids[infra], "label": "occurs in", "type": "infra_dep"})

# CDH -> Contacts module (special cross-product)
edges.append({"from": product_ids["CDH"], "to": module_ids["Contacts"], "label": "unifies profiles", "type": "data_flow"})
# DAAC -> Segment (AI Segment data)
edges.append({"from": product_ids["DAAC"], "to": module_ids["Segment"], "label": "feeds AI Segment", "type": "data_flow"})

# ============================================================
# Summary
# ============================================================
type_counts = defaultdict(int)
for n in nodes:
    type_counts[n["type"]] += 1
edge_type_counts = defaultdict(int)
for e in edges:
    edge_type_counts[e["type"]] += 1

print(f"\n📊 GRAPH SUMMARY")
print(f"   Nodes: {len(nodes)} | Edges: {len(edges)}")
print(f"   Node types: {dict(type_counts)}")
print(f"   Edge types: {dict(edge_type_counts)}")

graph_data = {"nodes": nodes, "edges": edges}
with open("/tmp/graph_data_v5.json", "w") as f:
    json.dump(graph_data, f, ensure_ascii=False)

print(f"✅ Saved to /tmp/graph_data_v5.json")
