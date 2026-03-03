#!/usr/bin/env python3
"""
build_graph_v7.py — Enhanced Code-based Knowledge Graph Builder
P0: Data Entity layer + code_dep semantic differentiation
P1: Celery Task layer + enriched metadata

Scans actual codebases to extract:
  - Cross-module import types (model_ref, task_dep, const_ref, api_client, code_dep)
  - Django model definitions per module
  - Celery task definitions per module
  - Cross-module task dependencies
"""
import json, math, os, re, ast
from collections import defaultdict
from pathlib import Path

# ================================================================
# 0. PATHS
# ================================================================
BASE = Path(__file__).parent
RUBATO = BASE / "code" / "rubato-develop"

SKIP_DIRS = {
    "rubato", "static", "templates", "media", "locale", "common",
    "lib", "packages", "config", "scripts", "requirements", "docs",
    "__pycache__", "migrations", "tests", "test",
}

# ================================================================
# 1. DEEP CODE SCANNING — MAAC (rubato)
# ================================================================

def discover_maac_modules():
    """Find valid Django app directories in rubato."""
    mods = []
    for d in sorted(os.listdir(RUBATO)):
        dp = RUBATO / d
        if dp.is_dir() and d not in SKIP_DIRS and not d.startswith(".") and not d.startswith("__"):
            mods.append(d)
    return mods

def scan_python_imports(filepath, own_module, all_modules):
    """Parse a Python file and extract classified cross-module imports."""
    results = []  # list of {target, type, names}
    try:
        content = open(filepath).read()
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                parts = node.module.split(".")
                target = parts[0]
                if target not in all_modules or target == own_module:
                    continue
                sub = parts[1] if len(parts) > 1 else ""
                names = [a.name for a in node.names]
                if sub == "models":
                    itype = "model_ref"
                elif sub == "tasks":
                    itype = "task_dep"
                elif sub in ("constants", "enums", "choices"):
                    itype = "const_ref"
                elif sub in ("api", "views", "viewsets", "serializers"):
                    itype = "api_client"
                else:
                    itype = "code_dep"
                results.append({"target": target, "type": itype, "names": names, "sub": sub})
    except Exception:
        pass
    return results

def extract_django_models(module_path):
    """Extract Django model class names from models.py."""
    models = []
    mpath = module_path / "models.py"
    if not mpath.exists():
        return models
    try:
        content = open(mpath).read()
        for m in re.finditer(r"^class (\w+)\(.*\):", content, re.MULTILINE):
            name = m.group(1)
            if not name.endswith("Manager") and not name.endswith("Mixin") and not name.startswith("_"):
                models.append(name)
    except Exception:
        pass
    return models

def extract_celery_tasks(module_path):
    """Extract Celery @shared_task function names from tasks.py."""
    tasks = []
    tpath = module_path / "tasks.py"
    if not tpath.exists():
        return tasks
    try:
        content = open(tpath).read()
        for m in re.finditer(r"@(?:shared_task|app\.task|celery_app\.task).*?\ndef (\w+)", content, re.DOTALL):
            tasks.append(m.group(1))
    except Exception:
        pass
    return tasks

def deep_scan_maac():
    """
    Deep scan all MAAC modules.
    Returns:
      modules: {name: {desc, models, tasks, deps_by_type}}
      cross_deps: [(from_mod, to_mod, dep_type, key_names)]
    """
    all_mods = discover_maac_modules()
    mod_set = set(all_mods)
    modules = {}
    cross_deps = []  # (from, to, type, names)

    # Per-module aggregated dep types
    for mod in all_mods:
        mod_path = RUBATO / mod
        models = extract_django_models(mod_path)
        tasks = extract_celery_tasks(mod_path)

        # Scan all .py files for imports
        deps_by_type = defaultdict(lambda: defaultdict(set))  # target -> type -> names
        for root, dirs, files in os.walk(str(mod_path)):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for fname in files:
                if not fname.endswith(".py"):
                    continue
                fpath = os.path.join(root, fname)
                imps = scan_python_imports(fpath, mod, mod_set)
                for imp in imps:
                    for name in imp["names"]:
                        deps_by_type[imp["target"]][imp["type"]].add(name)

        modules[mod] = {
            "models": models,
            "tasks": tasks,
            "deps_by_type": {
                tgt: {dtype: sorted(names) for dtype, names in dtypes.items()}
                for tgt, dtypes in deps_by_type.items()
            },
        }

        # Build cross_deps list
        for tgt, dtypes in deps_by_type.items():
            for dtype, names in dtypes.items():
                cross_deps.append((mod, tgt, dtype, sorted(names)))

    return modules, cross_deps

# ================================================================
# 2. STATIC DATA (non-MAAC products keep manual structure)
# ================================================================

PRODUCTS = {
    "MAAC": {
        "desc": "Marketing Automation & Analytics Cloud",
        "tech": "Django 3.2 + React 19 (TypeScript)",
        "repos": {"backend": "rubato (Python/Django)", "frontend": "Grazioso (React/TS)"},
    },
    "CAAC": {
        "desc": "Conversation Automation & Analytics Cloud",
        "tech": "Go (Cantata) + React (Zeffiroso/TS)",
        "repos": {"backend": "cantata (Go)", "frontend": "Zeffiroso (React/TS)"},
    },
    "DAAC": {
        "desc": "Data Automation & Analytics Cloud",
        "tech": "Python (FastAPI) + React + AI Agent",
        "repos": {"backend": "bebop (Python/FastAPI)", "frontend": "bebop/frontend (React/TS)"},
    },
    "CDH": {
        "desc": "Customer Data Hub — Unified Contact Profile",
        "tech": "Python + Go (Polyrhythmic)",
        "repos": {"backend": "polyrhythmic (Python+Go)", "frontend": "N/A (API-only)"},
    },
}

# Module descriptions (used when code scan doesn't provide one)
MAAC_DESC = {
    "accounts": "User authentication, SSO, 2FA, session management",
    "audience": "Contact management, segments, filters, ad platform audiences",
    "auto_reply": "Keyword auto-reply across LINE/FB/WhatsApp channels",
    "broadcast": "Push messaging (LINE/SMS/WhatsApp), scheduling, A/B test",
    "caac": "CAAC integration bridge — connects Rubato to Cantata",
    "cdp": "Customer Data Platform — profile unification, data sync",
    "channel": "Multi-channel management (LINE/FB/IG/WhatsApp/Email/SMS)",
    "email_channel": "Email campaign delivery via SendGrid, bounce handling",
    "fb": "Facebook/Instagram messaging, comment auto-reply",
    "journey": "Customer journey automation (triggers, actions, conditions)",
    "line": "Core LINE integration — messaging, rich menu, Flex, LIFF",
    "organization": "Org/tenant management, billing, feature control, RBAC",
    "tag": "Tag management — contact tagging, auto-tagging rules",
    "report": "Analytics & reporting — campaign performance, member stats",
    "prize": "Prize/reward management, lottery, coupon distribution",
    "referral": "Rapid Referral — MGM campaigns, invitation tracking",
    "openapi": "Public OpenAPI — external developer API endpoints",
    "webhook": "Webhook delivery — event push to external systems",
    "google_analytics": "GA4/UTM tracking integration for campaigns",
    "sms": "SMS delivery — domestic/international SMS campaigns",
    "sms_plus": "SMS Plus — enhanced SMS features, message records",
    "whatsapp": "WhatsApp Business messaging, template management",
    "message": "Message rendering engine — builds LINE/FB/SMS/Email messages",
    "form": "SurveyCake form integration, response tracking",
    "receipt": "Receipt registration campaign for loyalty programs",
    "notification": "In-app notification system for admin users",
    "payment": "Payment & billing — subscription, invoice management",
    "system": "System-wide utilities — campaign tracking, feature flags",
    "ai_generation": "AI content generation — copywriting, image generation",
    "extension": "MAAC extension plugins — custom action nodes",
    "campaign": "Campaign orchestration — multi-channel campaign management",
    "sforzando": "Prize fulfillment partner integration",
    "nine_one_app": "91App e-commerce integration",
    "shopify": "Shopify e-commerce integration",
    "shopline": "Shopline e-commerce integration",
    "cyberbiz": "Cyberbiz e-commerce integration",
    "invoice": "Invoice management — receipt/reward redemption",
    "internal": "Internal admin tools — data migration, debugging",
    "smoke_test": "Automated smoke test — system health validation",
    "bigquery": "BigQuery data pipeline integration",
    "pubsub_pull": "PubSub consumer — event processing workers",
}

# CAAC, DAAC, CDH modules (keep from v6 — Go/Python static analysis)
CAAC_MODULES = {
    "chat":            {"desc": "Core 1-on-1 chat — message routing, conversation lifecycle", "deps": ["aistrategy", "aiusage", "cdp", "organization", "tag"]},
    "aitask":          {"desc": "AI task execution — auto-reply suggestions, summarization", "deps": ["aistrategy", "aiusage", "chat"]},
    "aistrategy":      {"desc": "AI strategy configuration — model selection, prompts", "deps": []},
    "aiusage":         {"desc": "AI usage tracking — token consumption, quota", "deps": []},
    "auth":            {"desc": "Authentication & authorization — SSO, 2FA", "deps": []},
    "cdp":             {"desc": "CDP integration — unified contact view within CAAC", "deps": []},
    "dashboard":       {"desc": "CAAC analytics dashboard — conversation metrics, team performance", "deps": []},
    "organization":    {"desc": "Organization management — channels, users, roles, AI features", "deps": ["aitask"]},
    "tag":             {"desc": "Contact tagging within CAAC conversations", "deps": []},
    "openapi":         {"desc": "CAAC public API for external integrations", "deps": []},
    "workertask":      {"desc": "Background worker tasks — message processing, sync jobs", "deps": ["aiusage"]},
    "longrunningtask": {"desc": "Long-running operations — bulk exports, data migration", "deps": ["chat"]},
    "cat":             {"desc": "CAT (Contact Attribution Tracking) — member journey tracking", "deps": []},
}

DAAC_MODULES = {
    "session":      {"desc": "AI analysis session — conversation state, context management", "deps": ["auth", "organization"]},
    "dashboard":    {"desc": "Custom analytics dashboards — user-created visualizations", "deps": ["organization"]},
    "agent_v2":     {"desc": "AI Agent — natural language data querying (OpenAI/Gemini)", "deps": ["session"]},
    "file":         {"desc": "File management — upload/download for analysis results", "deps": []},
    "journey":      {"desc": "Journey analysis — customer path analysis via AI", "deps": ["session"]},
    "auth":         {"desc": "Authentication via Arioso SSO + Interlude", "deps": []},
    "organization": {"desc": "Org management — workspace, dbt config, Terraform infra", "deps": ["auth"]},
    "dbt":          {"desc": "dbt pipeline management — data transformation & modeling", "deps": ["organization"]},
    "infra":        {"desc": "Infrastructure provisioning — Terraform client setup", "deps": ["organization"]},
}

CDH_MODULES = {
    "unification":            {"desc": "Contact unification graph — merge/split profiles across channels", "deps": ["member", "tag"]},
    "contact":                {"desc": "Unified contact profile — cross-product contact view", "deps": ["unification"]},
    "member":                 {"desc": "Member management — import/export, profile enrichment", "deps": ["tag", "unification"]},
    "tag":                    {"desc": "Cross-product tag synchronization", "deps": ["member"]},
    "segment":                {"desc": "Cross-product audience segmentation via SQL/LLM", "deps": []},
    "engagement_history":     {"desc": "Engagement history — cross-channel interaction tracking", "deps": []},
    "broadcast":              {"desc": "CDH broadcast coordination — cross-product message dispatch", "deps": []},
    "richmenu":               {"desc": "LINE Rich Menu management via CDH", "deps": []},
    "custom_field":           {"desc": "Custom contact fields — user-defined attributes", "deps": []},
    "task":                   {"desc": "Background task execution — unification, sync, export jobs", "deps": []},
    "channel_entity_comment": {"desc": "Channel entity commenting — AI-powered contact annotations", "deps": []},
}

# Infrastructure (unchanged from v6)
MAAC_INFRA = {
    "PostgreSQL": {"desc": "Primary database (Django ORM)"},
    "Redis": {"desc": "Cache layer, Celery broker, rate limiting"},
    "RabbitMQ / Celery": {"desc": "Async task queue for background jobs"},
    "BigQuery": {"desc": "Analytics data warehouse, reporting"},
    "Cloud Storage (GCS)": {"desc": "File/image storage"},
    "Cloud Tasks": {"desc": "Deferred task execution"},
    "PubSub": {"desc": "Event streaming for cross-service communication"},
    "SendGrid": {"desc": "Email delivery service"},
    "LINE Messaging API": {"desc": "LINE platform messaging, rich menu, LIFF"},
    "Meta API (FB/IG)": {"desc": "Facebook & Instagram messaging API"},
    "WhatsApp Cloud API": {"desc": "WhatsApp Business messaging via Infobip"},
    "Google Analytics": {"desc": "Campaign tracking & UTM parameters"},
    "Firebase / Firestore": {"desc": "Real-time database for live features"},
    "Statsig": {"desc": "Feature flag management"},
    "Sentry": {"desc": "Error tracking & monitoring"},
    "Datadog": {"desc": "APM & distributed tracing"},
}
CAAC_INFRA = {
    "PostgreSQL": {"desc": "Primary database (Go SQL)"},
    "Redis": {"desc": "Session cache, rate limiting, pub/sub"},
    "Elasticsearch": {"desc": "Message search & conversation indexing"},
    "BigQuery": {"desc": "Analytics data export"},
    "GCS": {"desc": "File attachment storage"},
    "PubSub": {"desc": "Event streaming (PBEC events)"},
    "Infobip": {"desc": "WhatsApp/Voice gateway"},
    "FCM": {"desc": "Push notifications to mobile/browser"},
}
DAAC_INFRA = {
    "PostgreSQL": {"desc": "Primary database"},
    "BigQuery": {"desc": "Data warehouse — the core query target for AI Agent"},
    "GCS": {"desc": "File storage for analysis results"},
    "dbt": {"desc": "Data transformation pipeline"},
    "Terraform": {"desc": "Infrastructure as code for client provisioning"},
    "OpenAI / Gemini": {"desc": "AI model APIs for agent"},
}
CDH_INFRA = {
    "PostgreSQL": {"desc": "Primary database (SQLAlchemy + raw SQL)"},
    "BigQuery": {"desc": "Data warehouse for engagement history & analytics"},
    "GCS": {"desc": "File storage for import/export"},
    "PubSub": {"desc": "Event streaming — profile changes, tag updates"},
    "Cloud Run Jobs": {"desc": "Task execution for heavy processing"},
    "OpenAI": {"desc": "AI for segment tagging & entity commenting"},
    "Statsig": {"desc": "Feature flag management"},
}

CROSS_PRODUCT = [
    {"from": "MAAC", "to": "CAAC", "label": "CAAC_CANTATA_URL\n(REST API)", "type": "api_call"},
    {"from": "MAAC", "to": "DAAC", "label": "DAAC_API_URL\n(REST API)", "type": "api_call"},
    {"from": "CDH",  "to": "MAAC", "label": "RUBATO_HOST +\nRUBATO_DB_DSN", "type": "data_sync"},
    {"from": "CDH",  "to": "CAAC", "label": "CANTATA_HOST +\nCANTATA_DB_DSN", "type": "data_sync"},
    {"from": "CAAC", "to": "MAAC", "label": "MAAC_URL\n(REST API)", "type": "api_call"},
    {"from": "CAAC", "to": "CDH",  "label": "CDH_INTERNAL_URL\n(Unification V2)", "type": "api_call"},
    {"from": "DAAC", "to": "MAAC", "label": "MAAC_GCP_PROJECT_ID\n(BigQuery)", "type": "data_sync"},
    {"from": "DAAC", "to": "CAAC", "label": "CAAC_GCP_PROJECT_ID\n(BigQuery)", "type": "data_sync"},
]

SHARED_SERVICES = {
    "Interlude":  {"desc": "Admin center — billing, subscription, org provisioning", "used_by": ["MAAC", "CAAC", "DAAC"]},
    "Arioso":     {"desc": "SSO authentication service — Google/MS OAuth", "used_by": ["MAAC", "CAAC", "DAAC"]},
    "Harmony":    {"desc": "Partner API & Google Ads integration", "used_by": ["MAAC"]},
    "Sforzando":  {"desc": "Prize fulfillment & reward distribution", "used_by": ["MAAC"]},
    "Monophony":  {"desc": "URL shortener service (maac.io)", "used_by": ["MAAC", "CAAC"]},
    "MDS":        {"desc": "Message Delivery Service", "used_by": ["MAAC"]},
}

# Frontend -> Backend mapping (unchanged)
MAAC_FE_PAGES = {
    "Insight (Dashboard)": ["report", "google_analytics"],
    "Members": ["audience", "cdp", "tag"],
    "Segment": ["audience"],
    "Tag Manager": ["tag"],
    "Broadcast": ["broadcast", "message", "sms"],
    "Auto Reply": ["auto_reply", "fb", "whatsapp"],
    "Template Library": ["message", "line"],
    "Rich Menu": ["line"],
    "Journey": ["journey", "email_channel"],
    "Deeplink": ["line"],
    "Tracelink": ["google_analytics"],
    "Prize": ["prize", "sforzando"],
    "Retarget": ["audience", "fb"],
    "Referral V2": ["referral"],
    "Receipt Register": ["receipt"],
    "Webhook": ["webhook"],
    "SurveyCake (Form)": ["form"],
    "API Token": ["openapi"],
    "Widget": ["line"],
    "SMS Plus": ["sms_plus", "sms"],
    "Organization Settings": ["organization", "accounts"],
    "Channel Settings": ["channel"],
    "DPM": ["line"],
    "Beacon": ["line"],
    "Bindlink": ["line"],
    "Interaction Games": ["prize", "line"],
}

CAAC_FE_PAGES = {
    "Chat": ["chat", "aitask"],
    "Broadcast": ["chat"],
    "Insights": ["dashboard"],
    "Quick Template": ["chat"],
    "AI Settings": ["aistrategy", "aitask", "aiusage"],
    "Settings": ["organization", "auth"],
}


# ================================================================
# 3. BUILD GRAPH
# ================================================================
def build_graph(maac_scan):
    nodes = []
    edges = []
    nid = 0
    nmap = {}

    def add_node(label, ntype, group, title="", product="", desc="", **extra):
        nonlocal nid
        if label in nmap:
            return nmap[label]
        nid += 1
        nmap[label] = nid
        node = {
            "id": nid, "label": label, "type": ntype, "group": group,
            "title": title or label, "product": product, "desc": desc or title or label,
        }
        node.update(extra)
        nodes.append(node)
        return nid

    def add_edge(fid, tid, label, etype, arrows="to"):
        edges.append({"from": fid, "to": tid, "label": label, "type": etype, "arrows": arrows})

    # ── Company ──
    company_id = add_node("Crescendo Lab", "company", "company",
                          "Crescendo Lab — SaaS Product Suite\nProducts: MAAC, CAAC, DAAC, CDH",
                          desc="Crescendo Lab SaaS Product Suite")

    # ── Products ──
    pids = {}
    for pname, pinfo in PRODUCTS.items():
        pid = add_node(pname, "product", "product",
                       f"{pname} — {pinfo['desc']}\nTech: {pinfo['tech']}\nRepos: {pinfo['repos']}",
                       product=pname, desc=pinfo["desc"],
                       tech=pinfo["tech"], repos=pinfo["repos"])
        pids[pname] = pid
        add_edge(company_id, pid, "offers", "hierarchy")

    # ── MAAC Modules (from deep scan) ──
    maac_modules_data, maac_cross_deps = maac_scan
    for mname, minfo in sorted(maac_modules_data.items()):
        desc = MAAC_DESC.get(mname, f"MAAC module: {mname}")
        model_count = len(minfo["models"])
        task_count = len(minfo["tasks"])
        top_models = minfo["models"][:8]
        top_tasks = minfo["tasks"][:6]

        title_parts = [f"MAAC Module: {mname}", desc]
        if top_models:
            title_parts.append(f"Models ({model_count}): {', '.join(top_models)}")
        if top_tasks:
            title_parts.append(f"Celery Tasks ({task_count}): {', '.join(top_tasks)}")

        mid = add_node(f"maac/{mname}", "module", "maac_module",
                       "\n".join(title_parts),
                       product="MAAC", desc=desc,
                       models=minfo["models"],
                       tasks=minfo["tasks"],
                       model_count=model_count,
                       task_count=task_count)
        add_edge(pids["MAAC"], mid, "contains", "hierarchy")

    # MAAC cross-module deps (differentiated by type)
    seen_edges = set()
    for from_mod, to_mod, dep_type, names in maac_cross_deps:
        src = nmap.get(f"maac/{from_mod}")
        tgt = nmap.get(f"maac/{to_mod}")
        if not src or not tgt or src == tgt:
            continue
        edge_key = (src, tgt, dep_type)
        if edge_key in seen_edges:
            continue
        seen_edges.add(edge_key)

        # Build label with top referenced names
        top_names = names[:3]
        if dep_type == "model_ref":
            label = f"models: {', '.join(top_names)}"
        elif dep_type == "task_dep":
            label = f"tasks: {', '.join(top_names)}"
        elif dep_type == "const_ref":
            label = f"constants"
        elif dep_type == "api_client":
            label = f"views/api"
        else:
            label = "imports"
        add_edge(src, tgt, label, dep_type)

    # ── CAAC Modules ──
    for mname, minfo in CAAC_MODULES.items():
        mid = add_node(f"caac/{mname}", "module", "caac_module",
                       f"CAAC Service: {mname}\n{minfo['desc']}",
                       product="CAAC", desc=minfo["desc"])
        add_edge(pids["CAAC"], mid, "contains", "hierarchy")
    for mname, minfo in CAAC_MODULES.items():
        src = nmap.get(f"caac/{mname}")
        for dep in minfo["deps"]:
            tgt = nmap.get(f"caac/{dep}")
            if tgt and src != tgt:
                add_edge(src, tgt, "imports", "code_dep")

    # ── DAAC Modules ──
    for mname, minfo in DAAC_MODULES.items():
        mid = add_node(f"daac/{mname}", "module", "daac_module",
                       f"DAAC Service: {mname}\n{minfo['desc']}",
                       product="DAAC", desc=minfo["desc"])
        add_edge(pids["DAAC"], mid, "contains", "hierarchy")
    for mname, minfo in DAAC_MODULES.items():
        src = nmap.get(f"daac/{mname}")
        for dep in minfo["deps"]:
            tgt = nmap.get(f"daac/{dep}")
            if tgt and src != tgt:
                add_edge(src, tgt, "imports", "code_dep")

    # ── CDH Modules ──
    for mname, minfo in CDH_MODULES.items():
        mid = add_node(f"cdh/{mname}", "module", "cdh_module",
                       f"CDH App: {mname}\n{minfo['desc']}",
                       product="CDH", desc=minfo["desc"])
        add_edge(pids["CDH"], mid, "contains", "hierarchy")
    for mname, minfo in CDH_MODULES.items():
        src = nmap.get(f"cdh/{mname}")
        for dep in minfo["deps"]:
            tgt = nmap.get(f"cdh/{dep}")
            if tgt and src != tgt:
                add_edge(src, tgt, "imports", "code_dep")

    # ── Infrastructure ──
    all_infra = {}
    for src_infra, prod in [(MAAC_INFRA, "MAAC"), (CAAC_INFRA, "CAAC"), (DAAC_INFRA, "DAAC"), (CDH_INFRA, "CDH")]:
        for iname, iinfo in src_infra.items():
            if iname not in all_infra:
                all_infra[iname] = {"desc": iinfo["desc"], "products": set()}
            all_infra[iname]["products"].add(prod)

    for iname, iinfo in all_infra.items():
        iid = add_node(iname, "infra", "infra",
                       f"Infrastructure: {iname}\n{iinfo['desc']}\nUsed by: {', '.join(sorted(iinfo['products']))}",
                       desc=iinfo["desc"])
        for prod in iinfo["products"]:
            if prod in pids:
                add_edge(pids[prod], iid, "uses", "infra_dep")

    # ── Shared Services ──
    for sname, sinfo in SHARED_SERVICES.items():
        sid = add_node(sname, "shared_service", "shared_service",
                       f"Shared Service: {sname}\n{sinfo['desc']}\nUsed by: {', '.join(sinfo['used_by'])}",
                       desc=sinfo["desc"])
        for prod in sinfo["used_by"]:
            if prod in pids:
                add_edge(pids[prod], sid, "integrates", "service_dep")

    # ── Cross-Product ──
    for conn in CROSS_PRODUCT:
        fid = pids.get(conn["from"])
        tid = pids.get(conn["to"])
        if fid and tid:
            add_edge(fid, tid, conn["label"], conn["type"])

    # ── MAAC Frontend Pages ──
    for page_name, backends in MAAC_FE_PAGES.items():
        fid = add_node(f"page/{page_name}", "frontend_page", "maac_frontend",
                       f"MAAC Frontend Page: {page_name}\nConnects to: {', '.join(backends)}",
                       product="MAAC", desc=f"Frontend page: {page_name}")
        add_edge(pids["MAAC"], fid, "renders", "hierarchy")
        for bmod in backends:
            bid = nmap.get(f"maac/{bmod}")
            if bid:
                add_edge(fid, bid, "calls API", "api_call")

    # ── CAAC Frontend Pages ──
    for page_name, backends in CAAC_FE_PAGES.items():
        fid = add_node(f"caac_page/{page_name}", "frontend_page", "caac_frontend",
                       f"CAAC Frontend Page: {page_name}\nConnects to: {', '.join(backends)}",
                       product="CAAC", desc=f"Frontend page: {page_name}")
        add_edge(pids["CAAC"], fid, "renders", "hierarchy")
        for bmod in backends:
            bid = nmap.get(f"caac/{bmod}")
            if bid:
                add_edge(fid, bid, "calls API", "api_call")

    return {"nodes": nodes, "edges": edges}


# ================================================================
# 4. LAYOUT — Concentric circles (same as v6)
# ================================================================
def apply_layout(data):
    nodes = data["nodes"]
    edges = data["edges"]

    parent_of = {}
    for e in edges:
        if e["type"] == "hierarchy":
            parent_of[e["to"]] = e["from"]

    by_type = {}
    for n in nodes:
        by_type.setdefault(n["type"], []).append(n)

    RINGS = {
        "company": 0,
        "product": 250,
        "shared_service": 420,
        "infra": 550,
        "module": 680,
        "frontend_page": 980,
    }

    for n in by_type.get("company", []):
        n["x"] = 0
        n["y"] = 0

    products = by_type.get("product", [])
    product_angles = {}
    for i, n in enumerate(products):
        a = (i / len(products)) * 2 * math.pi - math.pi / 2
        product_angles[n["id"]] = a
        n["x"] = math.cos(a) * RINGS["product"]
        n["y"] = math.sin(a) * RINGS["product"]

    for i, n in enumerate(by_type.get("shared_service", [])):
        a = (i / max(1, len(by_type.get("shared_service", [])))) * 2 * math.pi + math.pi * 0.3
        n["x"] = math.cos(a) * RINGS["shared_service"]
        n["y"] = math.sin(a) * RINGS["shared_service"]

    for i, n in enumerate(by_type.get("infra", [])):
        a = (i / max(1, len(by_type.get("infra", [])))) * 2 * math.pi + math.pi * 0.15
        n["x"] = math.cos(a) * RINGS["infra"]
        n["y"] = math.sin(a) * RINGS["infra"]

    modules = by_type.get("module", [])
    mods_by_product = {}
    for n in modules:
        pid = parent_of.get(n["id"])
        mods_by_product.setdefault(pid, []).append(n)

    for pid, mods in mods_by_product.items():
        base_a = product_angles.get(pid, 0)
        spread = math.pi * 0.8 if len(mods) > 8 else math.pi * 0.5
        for i, n in enumerate(mods):
            a = base_a - spread / 2 + (spread / max(1, len(mods) - 1)) * i
            n["x"] = math.cos(a) * RINGS["module"]
            n["y"] = math.sin(a) * RINGS["module"]

    pages = by_type.get("frontend_page", [])
    pages_by_product = {}
    for n in pages:
        pid = parent_of.get(n["id"])
        pages_by_product.setdefault(pid, []).append(n)

    for pid, pgs in pages_by_product.items():
        base_a = product_angles.get(pid, 0)
        spread = math.pi * 0.7
        for i, n in enumerate(pgs):
            a = base_a - spread / 2 + (spread / max(1, len(pgs) - 1)) * i
            n["x"] = math.cos(a) * RINGS["frontend_page"]
            n["y"] = math.sin(a) * RINGS["frontend_page"]

    return data


# ================================================================
# 5. MAIN
# ================================================================
if __name__ == "__main__":
    print("🔍 Phase 1: Deep scanning MAAC codebase (rubato)...")
    maac_scan = deep_scan_maac()
    maac_modules_data, maac_cross_deps = maac_scan

    total_models = sum(len(m["models"]) for m in maac_modules_data.values())
    total_tasks = sum(len(m["tasks"]) for m in maac_modules_data.values())
    print(f"   Found {len(maac_modules_data)} modules, {total_models} models, {total_tasks} Celery tasks")

    dep_type_counts = defaultdict(int)
    for _, _, dtype, _ in maac_cross_deps:
        dep_type_counts[dtype] += 1
    print(f"   Dependency types: {dict(dep_type_counts)}")

    print("\n🔨 Phase 2: Building enhanced knowledge graph...")
    data = build_graph(maac_scan)
    data = apply_layout(data)

    out = "/tmp/graph_data_v7.json"
    with open(out, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ {len(data['nodes'])} nodes, {len(data['edges'])} edges")
    print(f"   Written to {out}")

    by_type = {}
    for n in data["nodes"]:
        by_type.setdefault(n["type"], []).append(n)
    for t, ns in sorted(by_type.items(), key=lambda x: -len(x[1])):
        print(f"   {t}: {len(ns)}")

    by_etype = {}
    for e in data["edges"]:
        by_etype.setdefault(e["type"], []).append(e)
    for t, es in sorted(by_etype.items(), key=lambda x: -len(x[1])):
        print(f"   edge/{t}: {len(es)}")
