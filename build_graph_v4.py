#!/usr/bin/env python3
"""
Build Knowledge Graph v4 — GitBookLLMv2.md Deep Analysis
Extracts modules, sub-features, PRDs, investigations, root causes, and Asana links.
Outputs graph_data JSON embedded into knowledge_graph.html
"""

import re
import json
from collections import defaultdict

INPUT_FILE = "GitBookLLMv2.md"

# ============================================================
# 1. Read file
# ============================================================
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    raw = f.read()

lines = raw.split("\n")
total_lines = len(lines)
print(f"📄 Read {total_lines} lines from {INPUT_FILE}")

# ============================================================
# 2. Build H1 / H2 / H3 indexes
# ============================================================
# File uses escaped markdown: \# for H1, \#\# for H2, \#\#\# for H3
# In Python string: \\# is literal backslash + hash

h1_re = re.compile(r"^\\#\s+(.+)$")
h2_re = re.compile(r"^\\#\\#\s+(.+)$")
h3_re = re.compile(r"^\\#\\#\\#\s+(.+)$")

h1_index = []
h2_index = []
h3_index = []

for i, line in enumerate(lines):
    # Must check H3 before H2 before H1 (longest prefix first)
    m3 = h3_re.match(line)
    if m3:
        h3_index.append((i, m3.group(1).strip()))
        continue
    m2 = h2_re.match(line)
    if m2:
        h2_index.append((i, m2.group(1).strip()))
        continue
    m1 = h1_re.match(line)
    if m1:
        h1_index.append((i, m1.group(1).strip()))

print(f"   H1: {len(h1_index)}, H2: {len(h2_index)}, H3: {len(h3_index)}")

# ============================================================
# 3. Define module boundaries
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

# Find positions of module H1 headers
module_positions = []
for idx, (line_no, title) in enumerate(h1_index):
    if title in MODULE_MAP:
        module_positions.append((line_no, title))

# Add sentinel
module_positions.append((total_lines, "END"))

modules = {}
for i in range(len(module_positions) - 1):
    start_ln, name = module_positions[i]
    end_ln = module_positions[i + 1][0]
    section_text = "\n".join(lines[start_ln:end_ln])
    key = MODULE_MAP[name]

    # Get sub-H1 sections within this module
    sub_h1 = [(ln, t) for ln, t in h1_index if ln > start_ln and ln < end_ln]
    # Get H2 sections within this module
    sub_h2 = [(ln, t) for ln, t in h2_index if ln > start_ln and ln < end_ln]

    modules[name] = {
        "key": key,
        "start": start_ln,
        "end": end_ln,
        "text": section_text,
        "sub_h1": sub_h1,
        "sub_h2": sub_h2,
    }

print(f"\n📦 Modules found: {len(modules)}")
for mod, info in modules.items():
    inv_count = sum(1 for _, t in info["sub_h2"] if t.startswith("Investigation of"))
    print(f"   {mod:25s} | L{info['start']:5d}-{info['end']:5d} | H2:{len(info['sub_h2']):3d} | Inv:{inv_count:3d}")

# ============================================================
# 4. Extract investigation tickets
# ============================================================
all_tickets = []

for mod_name, mod_info in modules.items():
    text = mod_info["text"]
    h2s = mod_info["sub_h2"]

    for idx, (ln, title) in enumerate(h2s):
        if not title.startswith("Investigation of") and "Why Can" not in title:
            continue

        # Get section text from this H2 to the next H2
        rel_start = ln - mod_info["start"]
        if idx + 1 < len(h2s):
            rel_end = h2s[idx + 1][0] - mod_info["start"]
        else:
            rel_end = mod_info["end"] - mod_info["start"]

        section_lines = lines[ln : ln + (rel_end - rel_start)]
        section = "\n".join(section_lines)

        # Parse metadata — file uses escaped markdown: \*\* for bold, \[ for brackets
        def extract_field(field_name, txt):
            # Match: \* \*\*FieldName:\*\* value
            pat = re.compile(
                r"\\\*\\\*" + re.escape(field_name) + r":\\\*\\\*\s*(.*?)(?:\s{2,}|\n|$)"
            )
            m = pat.search(txt)
            return m.group(1).strip() if m else ""

        def clean_escaped(txt):
            """Remove markdown escape chars."""
            txt = txt.replace("\\*", "").replace("\\#", "").replace("\\_", "_")
            txt = txt.replace("\\[", "[").replace("\\]", "]").replace("\\-", "-")
            txt = re.sub(r"\s+", " ", txt).strip()
            return txt

        feature = clean_escaped(extract_field("Feature", section))
        date = clean_escaped(extract_field("Created At", section))
        priority_raw = clean_escaped(extract_field("Ticket Priority", section))
        priority = priority_raw.split(" ")[0].split("-")[0].strip() if priority_raw else ""
        client = clean_escaped(extract_field("Client Name", section))
        owner = clean_escaped(extract_field("Resolution Owner", section))
        result = clean_escaped(extract_field("Result Breakdown", section))

        # Asana — format: \[ID\](URL)
        asana_m = re.search(
            r"\\\[(\d{13,})\\\]\((https://app\.asana\.com[^\)]+)\)", section
        )
        asana_id = asana_m.group(1) if asana_m else ""
        asana_url = asana_m.group(2) if asana_m else ""

        # Root cause — format: \*\*Root Cause:\*\* or \*\*Root Cause\*\*
        rc_m = re.search(
            r"\\\*\\\*Root Cause:?\\\*\\\*\s*\n?\s*(.*?)(?=\n\s*\\\*\\\*Solution|\Z)",
            section,
            re.DOTALL,
        )
        root_cause = ""
        if rc_m:
            root_cause = clean_escaped(rc_m.group(1))[:350]

        # Solution
        sol_m = re.search(
            r"\\\*\\\*Solution:?\\\*\\\*\s*\n?\s*(.*?)(?=\n\s*\\\*\\\*Status|\n\s*\\\*\\\*Action|\n\*\*\*|\n\\#|\Z)",
            section,
            re.DOTALL,
        )
        solution = ""
        if sol_m:
            solution = clean_escaped(sol_m.group(1))[:350]

        # Issue description — after "### 1. Issue Description" or "### Issue Description"
        desc_m = re.search(
            r"Issue Description\s*\n\s*(.*?)(?=\n\\#\\#\\#|\n\\\*\\\*|\Z)",
            section,
            re.DOTALL,
        )
        description = ""
        if desc_m:
            description = clean_escaped(desc_m.group(1))[:300]

        clean_title = title.replace("Investigation of ", "")

        ticket = {
            "module": mod_name,
            "title": clean_title,
            "feature": feature,
            "date": date,
            "priority": priority,
            "client": client,
            "owner": owner,
            "result": result,
            "asana_id": asana_id,
            "asana_url": asana_url,
            "root_cause": root_cause,
            "solution": solution,
            "description": description,
        }
        all_tickets.append(ticket)

print(f"\n🎫 Tickets extracted: {len(all_tickets)}")
by_mod = defaultdict(int)
by_pri = defaultdict(int)
for t in all_tickets:
    by_mod[t["module"]] += 1
    by_pri[t["priority"] or "?"] += 1
print(f"   By module: {dict(by_mod)}")
print(f"   By priority: {dict(by_pri)}")
print(f"   With Asana URL: {sum(1 for t in all_tickets if t['asana_url'])}")
print(f"   With root cause: {sum(1 for t in all_tickets if t['root_cause'])}")

# ============================================================
# 5. Extract PRDs and System Design docs
# ============================================================
prds = []
sys_designs = []
tutorials = []
knowledge_bases = []

for mod_name, mod_info in modules.items():
    for ln, title in mod_info["sub_h1"]:
        tl = title.lower()
        clean = re.sub(r"\\[\\_]", "_", title)
        if "prd" in tl:
            prds.append({"module": mod_name, "title": clean, "line": ln})
        elif any(x in tl for x in ["system design", "architecture", "scoping"]):
            sys_designs.append({"module": mod_name, "title": clean, "line": ln})
        elif any(x in tl for x in ["tutorial", "guide", "description"]):
            tutorials.append({"module": mod_name, "title": clean, "line": ln})
        elif "knowledge_base" in tl or "troubleshooting" in tl.replace(" ", ""):
            knowledge_bases.append({"module": mod_name, "title": clean, "line": ln})

    # Also check H1 titles outside of sub_h1 that contain design keywords
    for ln, title in h1_index:
        if ln > mod_info["start"] and ln < mod_info["end"]:
            tl = title.lower()
            if any(x in tl for x in ["edm", "architecture", "scoping", "performance"]):
                if not any(d["line"] == ln for d in sys_designs):
                    clean = re.sub(r"\\[\\_]", "_", title)
                    sys_designs.append({"module": mod_name, "title": clean, "line": ln})

# Also check H1 for standalone docs like "CL Customer 360", "Unification logic" etc.
standalone_docs = []
for ln, title in h1_index:
    tl = title.lower()
    if any(x in tl for x in ["customer 360", "unification", "channel entity", "profile", "fields limitation", "selector", "segment exclude", "country"]):
        for mod_name, mod_info in modules.items():
            if ln > mod_info["start"] and ln < mod_info["end"]:
                standalone_docs.append({"module": mod_name, "title": re.sub(r"\\[\\_]", "_", title), "line": ln})
                break

print(f"\n📋 PRDs: {len(prds)}")
for p in prds:
    print(f"   [{p['module']}] {p['title']}")
print(f"🔧 System Design docs: {len(sys_designs)}")
for s in sys_designs:
    print(f"   [{s['module']}] {s['title']}")
print(f"📚 Tutorials: {len(tutorials)}")
for t in tutorials:
    print(f"   [{t['module']}] {t['title'][:70]}")
print(f"📄 Standalone docs: {len(standalone_docs)}")
for d in standalone_docs:
    print(f"   [{d['module']}] {d['title'][:70]}")

# ============================================================
# 6. Extract key sub-features from Contacts Troubleshooting KB
# ============================================================
# The Contacts module has a large troubleshooting KB with structured Q&A
contacts_kb_features = []
for mod_name, mod_info in modules.items():
    if mod_name != "Contacts":
        continue
    # Find "MAAC Contacts Troubleshooting Knowledge Base" section
    for ln, title in mod_info["sub_h1"]:
        if "Troubleshooting Knowledge Base" in title:
            # Extract H2 categories within
            kb_h2s = [(l, t) for l, t in mod_info["sub_h2"] if l > ln]
            for l, t in kb_h2s:
                if not t.startswith("Investigation"):
                    contacts_kb_features.append(t)

print(f"\n📖 Contacts KB categories: {len(contacts_kb_features)}")
for c in contacts_kb_features[:10]:
    print(f"   - {c[:70]}")

# ============================================================
# 7. Root cause clustering — find common root causes across tickets
# ============================================================
def normalize_rc(rc_text):
    """Normalize root cause text for clustering."""
    rc = rc_text.lower()
    rc = re.sub(r"[^a-z0-9\s]", " ", rc)
    rc = re.sub(r"\s+", " ", rc).strip()
    return rc

# Define root cause categories based on semantic analysis
RC_CATEGORIES = {
    "airflow_pipeline": ["airflow", "dag", "pipeline", "etl", "bigquery", "data processing", "batch"],
    "data_inconsistency": ["discrepancy", "inconsisten", "mismatch", "data gap", "incorrect data", "wrong data", "data error"],
    "api_external_dep": ["line api", "meta api", "facebook", "instagram", "sendgrid", "external", "third party", "api limit", "rate limit"],
    "cache_state": ["cache", "cookie", "session", "stale", "outdated state"],
    "webhook_sync": ["webhook", "sync", "delay", "timing", "race condition", "event processing"],
    "permission_config": ["permission", "config", "setting", "disabled", "enable", "admin", "django"],
    "product_logic": ["product design", "by design", "expected behavior", "product expectation", "intended", "specification"],
    "resource_constraint": ["too costly", "resource", "infeasible", "not planned", "limitation"],
    "user_misunderstanding": ["misunderstand", "clarif", "user error", "documentation", "expected use"],
    "encoding_format": ["encoding", "format", "character", "emoji", "unicode", "utf", "template"],
    "quota_limit": ["quota", "limit", "exceeded", "throttle", "cap", "restriction"],
}

rc_clusters = defaultdict(list)

for ticket in all_tickets:
    rc_norm = normalize_rc(ticket["root_cause"])
    assigned = False
    for cat, keywords in RC_CATEGORIES.items():
        if any(kw in rc_norm for kw in keywords):
            rc_clusters[cat].append(ticket["title"][:60])
            assigned = True
            break
    if not assigned and ticket["root_cause"]:
        rc_clusters["other"].append(ticket["title"][:60])

print(f"\n🔍 Root Cause Clusters:")
for cat, items in sorted(rc_clusters.items(), key=lambda x: -len(x[1])):
    print(f"   {cat:25s}: {len(items)} tickets")

# ============================================================
# 8. Extract known sub-features from module content
# ============================================================
MODULE_SUBFEATURES = {
    "Insight": [
        ("Data Overview", "Dashboard with LINE overview, tag coverage, CID binding rate"),
        ("Deeplink Report", "Tracks new contacts acquired via deeplinks"),
        ("Acquisition Analytics", "New contact acquisition metrics and sources"),
        ("Open Rate Hotspot", "Heatmap of message open rates by day/time"),
        ("Message Count Analytics", "Track messages sent across channels"),
    ],
    "Contacts": [
        ("Contact Profile", "Unified contact profile with LINE UID, CID, phone, email"),
        ("Profile Unification", "Merge contacts across channels using matching logic"),
        ("Contact Import/Export", "Bulk import/export contacts via CSV"),
        ("Email Channel", "Email contact management and sender domain setup"),
        ("Contact Fields", "Custom and system fields on contact profiles"),
        ("Customer 360", "Cross-platform unified customer view (CDH)"),
    ],
    "Segment": [
        ("AI Segment", "Natural language prompt-based audience segmentation"),
        ("Segment Filters", "Rule-based segmentation with include/exclude logic"),
        ("Segment Add/Remove Tag", "Batch tag operations on segments"),
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
        ("Rich Menu Scheduling", "Schedule rich menu activation/deactivation"),
    ],
    "Auto-reply": [
        ("Keyword Auto-reply", "Trigger replies based on keyword matching"),
        ("Web Chat Auto-reply", "Auto-reply for web chat channels"),
        ("Auto-reply Scheduling", "Time-based auto-reply activation"),
        ("New Friend Welcome", "Greeting message for new contacts"),
        ("Reply Limit & Dedup", "Rate limiting and deduplication for replies"),
    ],
    "Deeplink": [
        ("Deeplink Generator", "Create trackable deeplinks for LINE"),
        ("Deeplink UTM Tracking", "UTM parameter support for deeplinks"),
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
        ("Journey Triggers", "Event-based journey triggers (tag, GA, time)"),
        ("Journey Actions", "Message send, tag add/remove, wait nodes"),
        ("Journey Conditions", "Yes/No branch and filter conditions"),
        ("Journey Report", "Per-node analytics and conversion tracking"),
        ("EDM Integration", "Email channel in journey via SendGrid"),
    ],
}

# ============================================================
# 9. Define infrastructure & external dependencies
# ============================================================
INFRA_NODES = [
    ("LINE API", "LINE Messaging API, LIFF, Rich Menu API"),
    ("Meta API", "Facebook & Instagram messaging APIs"),
    ("Airflow", "Apache Airflow for ETL pipelines and scheduled jobs"),
    ("BigQuery", "Google BigQuery for data warehouse and analytics"),
    ("PostgreSQL", "Primary relational database for MAAC"),
    ("SendGrid", "Email delivery service for EDM integration"),
    ("Django Admin", "Admin panel for configuration management"),
    ("CDH", "Customer Data Hub — cross-platform data unification"),
    ("Redis", "Cache layer for session and state management"),
    ("LIFF", "LINE Front-end Framework for in-app web views"),
]

# ============================================================
# 10. Build knowledge graph nodes and edges
# ============================================================
nodes = []
edges = []
node_id_counter = [0]

def make_id():
    node_id_counter[0] += 1
    return node_id_counter[0]

# --- Platform node ---
platform_id = make_id()
nodes.append({
    "id": platform_id,
    "label": "MAAC",
    "type": "platform",
    "title": "MAAC (Marketing Automation & Analytics Cloud)\nCrescendo Lab's core SaaS platform for omnichannel CRM",
    "group": "platform",
})

# --- Module nodes ---
module_node_ids = {}
for mod_name, mod_key in MODULE_MAP.items():
    mid = make_id()
    inv_count = sum(1 for t in all_tickets if t["module"] == mod_name)
    mod_info = modules.get(mod_name, {})
    desc_parts = [f"Module: {mod_name}"]
    if inv_count:
        desc_parts.append(f"Known issues: {inv_count}")
    sub_h1_count = len(mod_info.get("sub_h1", []))
    if sub_h1_count:
        desc_parts.append(f"Sub-docs: {sub_h1_count}")

    nodes.append({
        "id": mid,
        "label": mod_name,
        "type": "module",
        "title": "\n".join(desc_parts),
        "group": "module",
    })
    module_node_ids[mod_name] = mid
    edges.append({
        "from": platform_id,
        "to": mid,
        "label": "contains",
        "type": "hierarchy",
    })

# --- Sub-feature nodes ---
subfeature_ids = {}
for mod_name, features in MODULE_SUBFEATURES.items():
    if mod_name not in module_node_ids:
        continue
    parent_id = module_node_ids[mod_name]
    for feat_name, feat_desc in features:
        fid = make_id()
        nodes.append({
            "id": fid,
            "label": feat_name,
            "type": "subfeature",
            "title": f"{feat_name}\n{feat_desc}",
            "group": "subfeature",
            "module": mod_name,
        })
        subfeature_ids[(mod_name, feat_name)] = fid
        edges.append({
            "from": parent_id,
            "to": fid,
            "label": "has feature",
            "type": "hierarchy",
        })

# --- PRD nodes ---
prd_ids = {}
for prd in prds:
    pid = make_id()
    clean_title = prd["title"].replace("PRD — ", "").replace("PRD   ", "PRD: ").strip()
    nodes.append({
        "id": pid,
        "label": clean_title[:40],
        "type": "spec",
        "title": f"PRD: {clean_title}\nModule: {prd['module']}",
        "group": "spec",
        "module": prd["module"],
    })
    prd_ids[prd["title"]] = pid
    # Connect to parent module
    if prd["module"] in module_node_ids:
        edges.append({
            "from": module_node_ids[prd["module"]],
            "to": pid,
            "label": "specified by",
            "type": "spec_rel",
        })

# --- System Design nodes ---
design_ids = {}
for sd in sys_designs:
    did = make_id()
    clean_title = sd["title"].strip()
    nodes.append({
        "id": did,
        "label": clean_title[:45],
        "type": "spec",
        "title": f"System Design: {clean_title}\nModule: {sd['module']}",
        "group": "spec",
        "module": sd["module"],
    })
    design_ids[sd["title"]] = did
    if sd["module"] in module_node_ids:
        edges.append({
            "from": module_node_ids[sd["module"]],
            "to": did,
            "label": "designed by",
            "type": "spec_rel",
        })

# --- Infrastructure nodes ---
infra_ids = {}
for infra_name, infra_desc in INFRA_NODES:
    iid = make_id()
    nodes.append({
        "id": iid,
        "label": infra_name,
        "type": "infra",
        "title": f"Infrastructure: {infra_name}\n{infra_desc}",
        "group": "infra",
    })
    infra_ids[infra_name] = iid

# --- Root Cause nodes ---
rc_node_ids = {}
RC_LABELS = {
    "airflow_pipeline": "Data Pipeline\nFailure",
    "data_inconsistency": "Data\nInconsistency",
    "api_external_dep": "External API\nDependency",
    "cache_state": "Cache/State\nIssue",
    "webhook_sync": "Webhook/Sync\nDelay",
    "permission_config": "Permission/\nConfig Error",
    "product_logic": "Product Logic\n(By Design)",
    "resource_constraint": "Resource\nConstraint",
    "user_misunderstanding": "User\nMisunderstanding",
    "encoding_format": "Encoding/\nFormat Issue",
    "quota_limit": "Quota/Limit\nExceeded",
    "other": "Other\nRoot Cause",
}

RC_DESCRIPTIONS = {
    "airflow_pipeline": "Airflow DAG failures, BigQuery-to-Postgres sync issues, ETL pipeline errors causing missing or stale report data",
    "data_inconsistency": "Discrepancies between different data sources/reports. Mismatched metrics across Insight, Deeplink Report, and external dashboards",
    "api_external_dep": "Issues caused by LINE API, Meta API, or other third-party service changes, rate limits, or policy restrictions",
    "cache_state": "Stale cache, cookies, or session data causing outdated behavior or display issues",
    "webhook_sync": "Webhook delivery delays, event processing timing issues, or race conditions in real-time data sync",
    "permission_config": "Missing permissions, disabled settings, or configuration errors in Django admin or system settings",
    "product_logic": "Behavior that is by design but misaligned with user expectations. Requires documentation clarification",
    "resource_constraint": "Issues deemed too costly to fix. Technical debt accepted due to limited engineering resources",
    "user_misunderstanding": "Customer misunderstanding of product functionality. Resolved by documentation or clarification",
    "encoding_format": "Character encoding, emoji support, template format, or Unicode handling issues",
    "quota_limit": "System or API rate limits, quotas, or capacity restrictions causing failures",
    "other": "Other root causes not fitting major categories",
}

for cat, ticket_titles in rc_clusters.items():
    rcid = make_id()
    nodes.append({
        "id": rcid,
        "label": RC_LABELS.get(cat, cat),
        "type": "rootcause",
        "title": f"Root Cause: {RC_LABELS.get(cat, cat).replace(chr(10), ' ')}\n{RC_DESCRIPTIONS.get(cat, '')}\nAffected tickets: {len(ticket_titles)}",
        "group": "rootcause",
        "count": len(ticket_titles),
    })
    rc_node_ids[cat] = rcid

# --- Issue nodes (grouped by module, with Asana links) ---
issue_node_ids = {}
for mod_name in MODULE_MAP:
    mod_tickets = [t for t in all_tickets if t["module"] == mod_name]
    if not mod_tickets:
        continue

    for ticket in mod_tickets:
        iid = make_id()
        title_parts = [ticket["title"][:60]]
        if ticket["priority"]:
            title_parts.append(f"Priority: {ticket['priority']}")
        if ticket["date"]:
            title_parts.append(f"Date: {ticket['date']}")
        if ticket["client"] and ticket["client"] not in ["N/A", "\\\\[REDACTED\\\\]", "\\[REDACTED\\]"]:
            title_parts.append(f"Client: {ticket['client']}")
        if ticket["owner"]:
            title_parts.append(f"Owner: {ticket['owner']}")
        if ticket["result"]:
            title_parts.append(f"Result: {ticket['result']}")
        if ticket["description"]:
            title_parts.append(f"---\n{ticket['description'][:200]}")
        if ticket["root_cause"]:
            title_parts.append(f"---\nRoot Cause: {ticket['root_cause'][:200]}")
        if ticket["solution"]:
            title_parts.append(f"Solution: {ticket['solution'][:200]}")
        if ticket["asana_id"]:
            title_parts.append(f"---\nAsana: {ticket['asana_id']}")

        short_label = ticket["title"][:35]
        if len(ticket["title"]) > 35:
            short_label += "..."

        nodes.append({
            "id": iid,
            "label": short_label,
            "type": "issue",
            "title": "\n".join(title_parts),
            "group": "issue",
            "module": mod_name,
            "priority": ticket["priority"],
            "asana_id": ticket["asana_id"],
            "asana_url": ticket["asana_url"],
        })
        issue_node_ids[ticket["title"]] = iid

        # Edge: module -> issue
        if mod_name in module_node_ids:
            edges.append({
                "from": module_node_ids[mod_name],
                "to": iid,
                "label": "has issue",
                "type": "issue_rel",
            })

        # Edge: issue -> root cause
        rc_norm = normalize_rc(ticket["root_cause"])
        for cat, keywords in RC_CATEGORIES.items():
            if any(kw in rc_norm for kw in keywords):
                if cat in rc_node_ids:
                    edges.append({
                        "from": iid,
                        "to": rc_node_ids[cat],
                        "label": "caused by",
                        "type": "causal",
                    })
                break

# ============================================================
# 11. Cross-module dependencies
# ============================================================
CROSS_MODULE_DEPS = [
    # (from_module, to_module, label, explanation)
    ("Contacts", "Segment", "provides data", "Contacts provide the data pool that Segments filter"),
    ("Segment", "Broadcast", "filters audience", "Segments define the target audience for Broadcasts"),
    ("Contacts", "Broadcast", "receives message", "Contacts are the recipients of Broadcast messages"),
    ("Template Library", "Broadcast", "provides templates", "Templates are used in Broadcast message content"),
    ("Template Library", "Auto-reply", "provides templates", "Templates are used in Auto-reply responses"),
    ("Tag Manager", "Segment", "tags for filtering", "Tags are primary attributes for Segment filters"),
    ("Tag Manager", "Contacts", "labels contacts", "Tags are applied to Contact profiles"),
    ("Deeplink", "Contacts", "acquires contacts", "Deeplinks drive new contact acquisition"),
    ("Deeplink", "Insight", "feeds analytics", "Deeplink clicks feed into Insight acquisition metrics"),
    ("Tracelink", "Deeplink", "wraps URLs", "Tracelinks wrap Deeplinks with tracking and LIFF"),
    ("Broadcast", "Insight", "feeds metrics", "Broadcast delivery stats feed into Insight reports"),
    ("Customer Journey", "Broadcast", "sends messages", "Journey action nodes send Broadcast messages"),
    ("Customer Journey", "Tag Manager", "applies tags", "Journey can add/remove tags on contacts"),
    ("Customer Journey", "Segment", "uses segments", "Journey filters use Segment-like conditions"),
    ("Auto-reply", "Contacts", "creates contacts", "Auto-reply to new users triggers contact creation"),
    ("Rich Menu", "Deeplink", "uses deeplinks", "Rich Menu buttons link to Deeplinks"),
    ("Prize Management", "Auto-reply", "uses templates", "Prize campaigns use message templates similar to Auto-reply"),
    ("Contacts", "Customer Journey", "enters journey", "Contacts enter Journey flows based on triggers"),
]

for from_mod, to_mod, label, explanation in CROSS_MODULE_DEPS:
    if from_mod in module_node_ids and to_mod in module_node_ids:
        edges.append({
            "from": module_node_ids[from_mod],
            "to": module_node_ids[to_mod],
            "label": label,
            "type": "data_flow",
            "title": explanation,
        })

# Infrastructure dependencies
INFRA_DEPS = [
    ("Insight", "Airflow", "depends on", "Insight reports rely on Airflow DAGs for data processing"),
    ("Insight", "BigQuery", "reads from", "Insight data is aggregated in BigQuery"),
    ("Insight", "PostgreSQL", "serves from", "Insight dashboards read from PostgreSQL reporting tables"),
    ("Contacts", "LINE API", "syncs via", "Contact sync via LINE webhook events"),
    ("Contacts", "CDH", "unifies via", "Contact Profile Unification across platforms via CDH"),
    ("Contacts", "PostgreSQL", "stores in", "Contact data stored in PostgreSQL"),
    ("Broadcast", "LINE API", "sends via", "Broadcast messages delivered via LINE Messaging API"),
    ("Auto-reply", "LINE API", "replies via", "Auto-reply messages sent via LINE API"),
    ("Auto-reply", "Meta API", "replies via", "Auto-reply for FB/IG via Meta API"),
    ("Deeplink", "LIFF", "opens via", "Deeplinks open LIFF pages for tracking"),
    ("Tracelink", "LIFF", "opens via", "Tracelinks use LIFF for data collection"),
    ("Tracelink", "Redis", "caches in", "Tracelink cookie state cached in Redis"),
    ("Customer Journey", "SendGrid", "sends email", "Journey EDM integration via SendGrid"),
    ("Customer Journey", "Airflow", "scheduled by", "Journey time-based triggers use Airflow"),
    ("Tag Manager", "PostgreSQL", "stores in", "Tag data persisted in PostgreSQL"),
    ("Prize Management", "LINE API", "sends via", "Prize messages sent via LINE Flex Message API"),
    ("Rich Menu", "LINE API", "manages via", "Rich Menu CRUD via LINE Rich Menu API"),
    ("Segment", "BigQuery", "queries from", "AI Segment queries contact data from BigQuery"),
]

for mod, infra, label, explanation in INFRA_DEPS:
    if mod in module_node_ids and infra in infra_ids:
        edges.append({
            "from": module_node_ids[mod],
            "to": infra_ids[infra],
            "label": label,
            "type": "infra_dep",
            "title": explanation,
        })

# Connect root causes to infrastructure
RC_INFRA_LINKS = [
    ("airflow_pipeline", "Airflow", "pipeline failure in"),
    ("airflow_pipeline", "BigQuery", "data sync failure from"),
    ("api_external_dep", "LINE API", "dependency on"),
    ("api_external_dep", "Meta API", "dependency on"),
    ("cache_state", "Redis", "stale state in"),
    ("permission_config", "Django Admin", "misconfigured in"),
]

for rc_cat, infra, label in RC_INFRA_LINKS:
    if rc_cat in rc_node_ids and infra in infra_ids:
        edges.append({
            "from": rc_node_ids[rc_cat],
            "to": infra_ids[infra],
            "label": label,
            "type": "infra_dep",
        })

# ============================================================
# 12. Summary stats
# ============================================================
print(f"\n{'='*60}")
print(f"📊 KNOWLEDGE GRAPH SUMMARY")
print(f"   Nodes: {len(nodes)}")
print(f"   Edges: {len(edges)}")
print(f"   Types: {dict(defaultdict(int, {n['type']: sum(1 for nn in nodes if nn['type']==n['type']) for n in nodes}))}")
print(f"   Edge types: {dict(defaultdict(int, {e['type']: sum(1 for ee in edges if ee['type']==e['type']) for e in edges}))}")

# ============================================================
# 13. Save graph data
# ============================================================
graph_data = {"nodes": nodes, "edges": edges}
with open("/tmp/graph_data_v4.json", "w") as f:
    json.dump(graph_data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Graph data saved to /tmp/graph_data_v4.json")
print(f"   Ready for HTML injection!")
