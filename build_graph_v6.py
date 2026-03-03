#!/usr/bin/env python3
"""
build_graph_v6.py — Code-based Knowledge Graph Builder
Extracts real architecture from 6 codebases (MAAC, CAAC, DAAC, CDH)
and builds a precise knowledge graph with verified cross-service dependencies.

No Asana tickets — pure system architecture from source code.
"""
import json
import math

# ================================================================
# 1. RAW DATA — extracted from actual codebase scanning
# ================================================================

# --- PRODUCTS ---
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

# --- MAAC Backend Modules (from rubato INSTALLED_APPS + urls.py) ---
MAAC_MODULES = {
    "accounts": {
        "desc": "User authentication, SSO, 2FA, session management",
        "deps": ["audience", "caac", "channel", "journey", "line", "notification", "organization", "sms"],
    },
    "audience": {
        "desc": "Contact management, segments, filters, ad platform audiences",
        "deps": ["accounts", "bigquery", "cdp", "google_analytics", "line", "organization", "sms", "system", "tag"],
    },
    "auto_reply": {
        "desc": "Keyword auto-reply across LINE/FB/WhatsApp channels",
        "deps": ["accounts", "channel", "fb", "google_analytics", "line", "organization", "tag", "whatsapp"],
    },
    "broadcast": {
        "desc": "Push messaging (LINE/SMS/WhatsApp), scheduling, A/B test",
        "deps": ["accounts", "audience", "channel", "google_analytics", "line", "message", "organization", "report", "system", "tag"],
    },
    "caac": {
        "desc": "CAAC integration bridge — connects Rubato to Cantata",
        "deps": ["accounts", "line", "organization"],
    },
    "cdp": {
        "desc": "Customer Data Platform — profile unification, data sync",
        "deps": ["accounts", "audience", "journey", "line", "organization", "tag"],
    },
    "channel": {
        "desc": "Multi-channel management (LINE/FB/IG/WhatsApp/Email/SMS)",
        "deps": ["accounts", "line", "message", "notification", "openapi", "organization", "sms", "system"],
    },
    "email_channel": {
        "desc": "Email campaign delivery via SendGrid, bounce handling",
        "deps": ["accounts", "channel", "journey", "line", "organization", "sms", "system"],
    },
    "fb": {
        "desc": "Facebook/Instagram messaging, comment auto-reply",
        "deps": ["accounts", "auto_reply", "channel", "google_analytics", "line", "organization", "tag"],
    },
    "journey": {
        "desc": "Customer journey automation (triggers, actions, conditions)",
        "deps": ["accounts", "audience", "cdp", "channel", "email_channel", "google_analytics", "line", "organization", "report", "sms", "system", "tag"],
    },
    "line": {
        "desc": "Core LINE integration — messaging, rich menu, Flex, LIFF",
        "deps": ["accounts", "audience", "auto_reply", "bigquery", "caac", "cdp", "channel", "email_channel", "fb", "form", "google_analytics", "journey", "message", "notification", "openapi", "organization", "prize", "receipt", "referral", "report", "sms", "system", "tag", "webhook", "whatsapp"],
    },
    "organization": {
        "desc": "Org/tenant management, billing, feature control, RBAC",
        "deps": ["accounts", "audience", "bigquery", "caac", "channel", "google_analytics", "journey", "line", "notification", "openapi", "payment"],
    },
    "tag": {
        "desc": "Tag management — contact tagging, auto-tagging rules",
        "deps": ["accounts", "audience", "cdp", "journey", "line", "organization", "report", "system"],
    },
    "report": {
        "desc": "Analytics & reporting — campaign performance, member stats",
        "deps": ["bigquery", "google_analytics", "line", "openapi", "payment", "sms_plus", "system", "tag"],
    },
    "prize": {
        "desc": "Prize/reward management, lottery, coupon distribution",
        "deps": ["accounts", "google_analytics", "line", "notification", "openapi", "organization", "report", "sforzando", "system", "tag", "webhook"],
    },
    "referral": {
        "desc": "Rapid Referral — MGM campaigns, invitation tracking",
        "deps": ["accounts", "line", "organization", "prize", "system", "tag"],
    },
    "openapi": {
        "desc": "Public OpenAPI — external developer API endpoints",
        "deps": ["accounts", "audience", "auto_reply", "channel", "email_channel", "google_analytics", "line", "notification", "organization", "payment", "prize", "report", "sms", "system", "tag", "webhook", "whatsapp"],
    },
    "webhook": {
        "desc": "Webhook delivery — event push to external systems",
        "deps": ["line", "openapi", "prize", "receipt", "system", "tag"],
    },
    "google_analytics": {
        "desc": "GA4/UTM tracking integration for campaigns",
        "deps": ["accounts", "line", "organization", "report", "system"],
    },
    "sms": {
        "desc": "SMS delivery — domestic/international SMS campaigns",
        "deps": ["audience", "channel", "google_analytics", "journey", "line", "openapi", "organization", "payment", "report", "system"],
    },
    "sms_plus": {
        "desc": "SMS Plus — enhanced SMS features, message records",
        "deps": ["line", "notification", "openapi", "organization", "payment", "sms", "whatsapp"],
    },
    "whatsapp": {
        "desc": "WhatsApp Business messaging, template management",
        "deps": ["auto_reply", "channel", "line", "message", "openapi", "organization", "tag"],
    },
    "message": {
        "desc": "Message rendering engine — builds LINE/FB/SMS/Email messages",
        "deps": ["channel", "google_analytics", "line", "organization", "system"],
    },
    "form": {
        "desc": "SurveyCake form integration, response tracking",
        "deps": ["line", "tag", "webhook"],
    },
    "receipt": {
        "desc": "Receipt registration campaign for loyalty programs",
        "deps": ["bigquery", "line", "openapi", "organization", "prize", "system", "webhook"],
    },
    "notification": {
        "desc": "In-app notification system for admin users",
        "deps": ["accounts"],
    },
    "payment": {
        "desc": "Payment & billing — subscription, invoice management",
        "deps": ["line", "notification", "organization"],
    },
    "system": {
        "desc": "System-wide utilities — campaign tracking, feature flags",
        "deps": ["accounts", "audience", "bigquery", "google_analytics", "line", "message", "notification", "referral", "tag"],
    },
    "ai_generation": {
        "desc": "AI content generation — copywriting, image generation",
        "deps": ["organization", "system"],
    },
    "extension": {
        "desc": "MAAC extension plugins — custom action nodes",
        "deps": ["accounts", "channel", "google_analytics", "journey", "line", "organization"],
    },
    "campaign": {
        "desc": "Campaign orchestration — multi-channel campaign management",
        "deps": ["accounts", "channel", "journey"],
    },
    "sforzando": {
        "desc": "Prize fulfillment partner integration",
        "deps": ["accounts", "line", "organization", "prize", "system", "tag"],
    },
    "nine_one_app": {
        "desc": "91App e-commerce integration",
        "deps": ["accounts", "line", "openapi", "organization", "payment", "system", "tag", "webhook"],
    },
    "shopify": {
        "desc": "Shopify e-commerce integration",
        "deps": ["accounts", "line", "system"],
    },
    "shopline": {
        "desc": "Shopline e-commerce integration",
        "deps": ["accounts", "line", "openapi", "organization", "payment", "system", "tag", "webhook"],
    },
    "cyberbiz": {
        "desc": "Cyberbiz e-commerce integration",
        "deps": ["accounts", "line"],
    },
}

# --- MAAC External Packages (from rubato/packages/) ---
MAAC_INFRA = {
    "PostgreSQL": {"desc": "Primary database (Django ORM)", "used_by": ["all MAAC modules"]},
    "Redis": {"desc": "Cache layer, Celery broker, rate limiting", "used_by": ["broadcast", "line", "auto_reply", "journey"]},
    "RabbitMQ / Celery": {"desc": "Async task queue for background jobs", "used_by": ["broadcast", "journey", "line", "receipt", "sms"]},
    "BigQuery": {"desc": "Analytics data warehouse, reporting", "used_by": ["audience", "report", "bigquery", "receipt", "system"]},
    "Cloud Storage (GCS)": {"desc": "File/image storage", "used_by": ["line", "broadcast", "prize"]},
    "Cloud Tasks": {"desc": "Deferred task execution", "used_by": ["broadcast", "journey"]},
    "PubSub": {"desc": "Event streaming for cross-service communication", "used_by": ["pubsub_pull", "cdp", "auto_reply", "fb", "whatsapp"]},
    "SendGrid": {"desc": "Email delivery service", "used_by": ["email_channel"]},
    "LINE Messaging API": {"desc": "LINE platform messaging, rich menu, LIFF", "used_by": ["line", "auto_reply", "broadcast"]},
    "Meta API (FB/IG)": {"desc": "Facebook & Instagram messaging API", "used_by": ["fb"]},
    "WhatsApp Cloud API": {"desc": "WhatsApp Business messaging via Infobip", "used_by": ["whatsapp"]},
    "Google Analytics": {"desc": "Campaign tracking & UTM parameters", "used_by": ["google_analytics"]},
    "Firebase / Firestore": {"desc": "Real-time database for live features", "used_by": ["line", "audience"]},
    "Statsig": {"desc": "Feature flag management", "used_by": ["organization", "system"]},
    "Sentry": {"desc": "Error tracking & monitoring", "used_by": ["all MAAC modules"]},
    "Datadog": {"desc": "APM & distributed tracing", "used_by": ["all MAAC modules"]},
}

# --- CAAC Backend Modules (from cantata/internal/app/service/) ---
CAAC_MODULES = {
    "chat": {
        "desc": "Core 1-on-1 chat — message routing, conversation lifecycle",
        "deps": ["aistrategy", "aiusage", "cdp", "organization", "tag"],
        "domains": ["ai", "aitask", "auth", "cdp", "chat", "engagement", "infobip", "maac", "organization", "pbec", "productfeed", "tag", "voice"],
    },
    "aitask": {
        "desc": "AI task execution — auto-reply suggestions, summarization",
        "deps": ["aistrategy", "aiusage", "chat"],
        "domains": ["ai", "aitask", "chat", "engagement", "organization", "pbec", "productfeed"],
    },
    "aistrategy": {
        "desc": "AI strategy configuration — model selection, prompts",
        "deps": [],
        "domains": ["ai", "aitask", "chat", "organization"],
    },
    "aiusage": {
        "desc": "AI usage tracking — token consumption, quota",
        "deps": [],
        "domains": ["ai", "organization", "pbec"],
    },
    "auth": {
        "desc": "Authentication & authorization — SSO, 2FA",
        "deps": [],
        "domains": ["auth", "chat", "organization"],
    },
    "cdp": {
        "desc": "CDP integration — unified contact view within CAAC",
        "deps": [],
        "domains": ["auth", "cdp", "chat", "organization", "tag"],
    },
    "dashboard": {
        "desc": "CAAC analytics dashboard — conversation metrics, team performance",
        "deps": [],
        "domains": ["chat", "dashboard", "organization", "tag"],
    },
    "organization": {
        "desc": "Organization management — channels, users, roles, AI features",
        "deps": ["aitask"],
        "domains": ["ai", "aitask", "auth", "cdp", "chat", "maac", "organization", "productfeed", "tag", "voice"],
    },
    "tag": {
        "desc": "Contact tagging within CAAC conversations",
        "deps": [],
        "domains": ["cdp", "chat", "engagement", "organization", "tag"],
    },
    "openapi": {
        "desc": "CAAC public API for external integrations",
        "deps": [],
        "domains": ["auth", "chat", "openapi", "organization"],
    },
    "workertask": {
        "desc": "Background worker tasks — message processing, sync jobs",
        "deps": ["aiusage"],
        "domains": ["ai", "aitask", "chat", "maac", "openapi", "organization", "pbec", "productfeed"],
    },
    "longrunningtask": {
        "desc": "Long-running operations — bulk exports, data migration",
        "deps": ["chat"],
        "domains": ["ai", "aitask", "cdp", "chat", "engagement", "organization", "tag"],
    },
    "cat": {
        "desc": "CAT (Contact Attribution Tracking) — member journey tracking",
        "deps": [],
        "domains": ["auth", "cat", "chat", "organization"],
    },
}

# CAAC Router Handlers (from cantata/internal/router/)
CAAC_HANDLERS = [
    "ai_action", "ai_agent", "ai_feature_setting", "ai_resolve",
    "assignment", "assignment_general_setting", "auto_assignment",
    "auth", "booking", "cat", "cdp",
    "chat_ai_assistant", "chat_booking", "chat_channel_quick_template",
    "chat_conversation", "chat_emotion_level", "chat_group",
    "chat_member", "chat_message", "chat_nine_one", "chat_openai", "chat_workduo",
    "collaborator", "conversation_summary",
    "dashboard_channel_contact", "dashboard_commerce", "dashboard_conversation",
    "dashboard_efficiency", "dashboard_tag", "dashboard_team",
    "feature_flag", "infobip",
    "keyword", "manual_assignment", "member_engagement", "member_note",
    "openapi", "organization_channel", "organization_org", "organization_role", "organization_user",
    "platform", "product_feed", "redirect",
    "tag_tag", "tag_tagmember", "team", "theme",
    "unification", "unification_setting", "utm_setting", "ux",
    "voice_quota_status", "webhook", "webpush_notification",
]

# --- CAAC Infrastructure ---
CAAC_INFRA = {
    "PostgreSQL": {"desc": "Primary database (Go SQL)", "used_by": ["all CAAC services"]},
    "Redis": {"desc": "Session cache, rate limiting, pub/sub", "used_by": ["chat", "auth"]},
    "Elasticsearch": {"desc": "Message search & conversation indexing", "used_by": ["chat"]},
    "BigQuery": {"desc": "Analytics data export", "used_by": ["dashboard"]},
    "GCS": {"desc": "File attachment storage", "used_by": ["chat"]},
    "PubSub": {"desc": "Event streaming (PBEC events)", "used_by": ["chat", "workertask"]},
    "Infobip": {"desc": "WhatsApp/Voice gateway", "used_by": ["chat"]},
    "FCM": {"desc": "Push notifications to mobile/browser", "used_by": ["chat"]},
}

# --- DAAC Backend Modules (from bebop) ---
DAAC_MODULES = {
    "session": {
        "desc": "AI analysis session — conversation state, context management",
        "deps": ["auth", "organization"],
    },
    "dashboard": {
        "desc": "Custom analytics dashboards — user-created visualizations",
        "deps": ["organization"],
    },
    "agent_v2": {
        "desc": "AI Agent — natural language data querying (OpenAI/Gemini)",
        "deps": ["session"],
        "tools": ["journey analysis", "SQL query", "data stats", "file read", "parameter query"],
    },
    "file": {
        "desc": "File management — upload/download for analysis results",
        "deps": [],
    },
    "journey": {
        "desc": "Journey analysis — customer path analysis via AI",
        "deps": ["session"],
    },
    "auth": {
        "desc": "Authentication via Arioso SSO + Interlude",
        "deps": [],
    },
    "organization": {
        "desc": "Org management — workspace, dbt config, Terraform infra",
        "deps": ["auth"],
    },
    "dbt": {
        "desc": "dbt pipeline management — data transformation & modeling",
        "deps": ["organization"],
    },
    "infra": {
        "desc": "Infrastructure provisioning — Terraform client setup",
        "deps": ["organization"],
    },
}

DAAC_INFRA = {
    "PostgreSQL": {"desc": "Primary database", "used_by": ["all DAAC services"]},
    "BigQuery": {"desc": "Data warehouse — the core query target for AI Agent", "used_by": ["agent_v2", "dbt", "journey"]},
    "GCS": {"desc": "File storage for analysis results", "used_by": ["file"]},
    "dbt": {"desc": "Data transformation pipeline", "used_by": ["dbt", "organization"]},
    "Terraform": {"desc": "Infrastructure as code for client provisioning", "used_by": ["infra"]},
    "OpenAI / Gemini": {"desc": "AI model APIs for agent", "used_by": ["agent_v2"]},
}

# --- CDH Modules (from polyrhythmic) ---
CDH_MODULES = {
    "unification": {
        "desc": "Contact unification graph — merge/split profiles across channels",
        "deps": ["member", "tag"],
    },
    "contact": {
        "desc": "Unified contact profile — cross-product contact view",
        "deps": ["unification"],
    },
    "member": {
        "desc": "Member management — import/export, profile enrichment",
        "deps": ["tag", "unification"],
    },
    "tag": {
        "desc": "Cross-product tag synchronization",
        "deps": ["member"],
    },
    "segment": {
        "desc": "Cross-product audience segmentation via SQL/LLM",
        "deps": [],
    },
    "engagement_history": {
        "desc": "Engagement history — cross-channel interaction tracking",
        "deps": [],
    },
    "broadcast": {
        "desc": "CDH broadcast coordination — cross-product message dispatch",
        "deps": [],
    },
    "richmenu": {
        "desc": "LINE Rich Menu management via CDH",
        "deps": [],
    },
    "custom_field": {
        "desc": "Custom contact fields — user-defined attributes",
        "deps": [],
    },
    "task": {
        "desc": "Background task execution — unification, sync, export jobs",
        "deps": [],
    },
    "channel_entity_comment": {
        "desc": "Channel entity commenting — AI-powered contact annotations",
        "deps": [],
    },
}

CDH_INFRA = {
    "PostgreSQL": {"desc": "Primary database (SQLAlchemy + raw SQL)", "used_by": ["all CDH modules"]},
    "BigQuery": {"desc": "Data warehouse for engagement history & analytics", "used_by": ["engagement_history", "segment"]},
    "GCS": {"desc": "File storage for import/export", "used_by": ["member"]},
    "PubSub": {"desc": "Event streaming — profile changes, tag updates", "used_by": ["unification", "member", "tag"]},
    "Cloud Run Jobs": {"desc": "Task execution for heavy processing", "used_by": ["task"]},
    "OpenAI": {"desc": "AI for segment tagging & entity commenting", "used_by": ["segment", "channel_entity_comment"]},
    "Statsig": {"desc": "Feature flag management", "used_by": ["all CDH modules"]},
}

# --- CROSS-PRODUCT CONNECTIONS (verified from settings/config files) ---
CROSS_PRODUCT = [
    # Rubato (MAAC) -> Cantata (CAAC)
    {"from": "MAAC", "to": "CAAC", "label": "CAAC_CANTATA_URL\n(REST API)", "type": "api_call"},
    # Rubato (MAAC) -> Bebop (DAAC)
    {"from": "MAAC", "to": "DAAC", "label": "DAAC_API_URL\n(REST API)", "type": "api_call"},
    # CDH -> MAAC (reads rubato DB + API)
    {"from": "CDH", "to": "MAAC", "label": "RUBATO_HOST +\nRUBATO_DB_DSN", "type": "data_sync"},
    # CDH -> CAAC (reads cantata DB + API)
    {"from": "CDH", "to": "CAAC", "label": "CANTATA_HOST +\nCANTATA_DB_DSN", "type": "data_sync"},
    # CAAC -> MAAC
    {"from": "CAAC", "to": "MAAC", "label": "MAAC_URL\n(REST API)", "type": "api_call"},
    # CAAC -> CDH
    {"from": "CAAC", "to": "CDH", "label": "CDH_INTERNAL_URL\n(Unification V2)", "type": "api_call"},
    # DAAC -> MAAC (GCP project data)
    {"from": "DAAC", "to": "MAAC", "label": "MAAC_GCP_PROJECT_ID\n(BigQuery)", "type": "data_sync"},
    # DAAC -> CAAC (GCP project data)
    {"from": "DAAC", "to": "CAAC", "label": "CAAC_GCP_PROJECT_ID\n(BigQuery)", "type": "data_sync"},
]

# --- SHARED SERVICES (from rubato/packages/) ---
SHARED_SERVICES = {
    "Interlude": {"desc": "Admin center — billing, subscription, org provisioning", "used_by": ["MAAC", "CAAC", "DAAC"]},
    "Arioso": {"desc": "SSO authentication service — Google/MS OAuth", "used_by": ["MAAC", "CAAC", "DAAC"]},
    "Harmony": {"desc": "Partner API & Google Ads integration", "used_by": ["MAAC"]},
    "Sforzando": {"desc": "Prize fulfillment & reward distribution", "used_by": ["MAAC"]},
    "Monophony": {"desc": "URL shortener service (maac.io)", "used_by": ["MAAC", "CAAC"]},
    "MDS": {"desc": "Message Delivery Service", "used_by": ["MAAC"]},
}

# ================================================================
# 2. BUILD GRAPH
# ================================================================
def build_graph():
    nodes = []
    edges = []
    nid = 0
    nmap = {}

    def add_node(label, ntype, group, title="", product="", desc=""):
        nonlocal nid
        if label in nmap:
            return nmap[label]
        nid += 1
        nmap[label] = nid
        nodes.append({
            "id": nid, "label": label, "type": ntype, "group": group,
            "title": title or label, "product": product, "desc": desc or title or label,
        })
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
                       product=pname, desc=pinfo["desc"])
        pids[pname] = pid
        add_edge(company_id, pid, "offers", "hierarchy")

    # ── MAAC Modules ──
    for mname, minfo in MAAC_MODULES.items():
        mid = add_node(f"maac/{mname}", "module", "maac_module",
                       f"MAAC Module: {mname}\n{minfo['desc']}\nDeps: {', '.join(minfo['deps'][:5])}{'...' if len(minfo['deps'])>5 else ''}",
                       product="MAAC", desc=minfo["desc"])
        add_edge(pids["MAAC"], mid, "contains", "hierarchy")

    # MAAC cross-module deps
    for mname, minfo in MAAC_MODULES.items():
        src = nmap.get(f"maac/{mname}")
        if not src:
            continue
        for dep in minfo["deps"]:
            tgt = nmap.get(f"maac/{dep}")
            if tgt and src != tgt:
                add_edge(src, tgt, "imports", "code_dep")

    # ── CAAC Modules ──
    for mname, minfo in CAAC_MODULES.items():
        mid = add_node(f"caac/{mname}", "module", "caac_module",
                       f"CAAC Service: {mname}\n{minfo['desc']}\nDomains: {', '.join(minfo.get('domains', [])[:5])}",
                       product="CAAC", desc=minfo["desc"])
        add_edge(pids["CAAC"], mid, "contains", "hierarchy")

    for mname, minfo in CAAC_MODULES.items():
        src = nmap.get(f"caac/{mname}")
        if not src:
            continue
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
        if not src:
            continue
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
        if not src:
            continue
        for dep in minfo["deps"]:
            tgt = nmap.get(f"cdh/{dep}")
            if tgt and src != tgt:
                add_edge(src, tgt, "imports", "code_dep")

    # ── Infrastructure ──
    all_infra = {}
    for iname, iinfo in {**MAAC_INFRA, **CAAC_INFRA, **DAAC_INFRA, **CDH_INFRA}.items():
        if iname not in all_infra:
            all_infra[iname] = {"desc": iinfo["desc"], "products": set()}

    # Map infra to products
    for iname in MAAC_INFRA: all_infra[iname]["products"].add("MAAC")
    for iname in CAAC_INFRA: all_infra[iname]["products"].add("CAAC")
    for iname in DAAC_INFRA: all_infra[iname]["products"].add("DAAC")
    for iname in CDH_INFRA: all_infra[iname]["products"].add("CDH")

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

    # ── Cross-Product Connections ──
    for conn in CROSS_PRODUCT:
        fid = pids.get(conn["from"])
        tid = pids.get(conn["to"])
        if fid and tid:
            add_edge(fid, tid, conn["label"], conn["type"])

    # ── MAAC Frontend Pages -> Backend Modules (from Grazioso routes + shared/api) ──
    frontend_to_backend = {
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
    for page_name, backends in frontend_to_backend.items():
        fid = add_node(f"page/{page_name}", "frontend_page", "maac_frontend",
                       f"MAAC Frontend Page: {page_name}\nConnects to: {', '.join(backends)}",
                       product="MAAC", desc=f"Frontend page: {page_name}")
        add_edge(pids["MAAC"], fid, "renders", "hierarchy")
        for bmod in backends:
            bid = nmap.get(f"maac/{bmod}")
            if bid:
                add_edge(fid, bid, "calls API", "api_call")

    # ── CAAC Frontend Pages -> Backend (from Zeffiroso routes) ──
    caac_pages = {
        "Chat": ["chat", "aitask"],
        "Broadcast": ["chat"],
        "Insights": ["dashboard"],
        "Quick Template": ["chat"],
        "AI Settings": ["aistrategy", "aitask", "aiusage"],
        "Settings": ["organization", "auth"],
    }
    for page_name, backends in caac_pages.items():
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
# 3. LAYOUT — Concentric circles
# ================================================================
def apply_layout(data):
    nodes = data["nodes"]
    edges = data["edges"]

    # Build parent map from hierarchy edges
    parent_of = {}
    for e in edges:
        if e["type"] == "hierarchy":
            parent_of[e["to"]] = e["from"]

    # Group by type
    by_type = {}
    for n in nodes:
        by_type.setdefault(n["type"], []).append(n)

    # Ring radii
    RINGS = {
        "company": 0,
        "product": 250,
        "shared_service": 420,
        "infra": 550,
        "module": 680,
        "frontend_page": 980,
    }

    # Company at center
    for n in by_type.get("company", []):
        n["x"] = 0
        n["y"] = 0

    # Products evenly spaced
    products = by_type.get("product", [])
    product_angles = {}
    for i, n in enumerate(products):
        a = (i / len(products)) * 2 * math.pi - math.pi / 2
        product_angles[n["id"]] = a
        n["x"] = math.cos(a) * RINGS["product"]
        n["y"] = math.sin(a) * RINGS["product"]

    # Shared services spread
    for i, n in enumerate(by_type.get("shared_service", [])):
        a = (i / max(1, len(by_type.get("shared_service", [])))) * 2 * math.pi + math.pi * 0.3
        n["x"] = math.cos(a) * RINGS["shared_service"]
        n["y"] = math.sin(a) * RINGS["shared_service"]

    # Infrastructure spread
    for i, n in enumerate(by_type.get("infra", [])):
        a = (i / max(1, len(by_type.get("infra", [])))) * 2 * math.pi + math.pi * 0.15
        n["x"] = math.cos(a) * RINGS["infra"]
        n["y"] = math.sin(a) * RINGS["infra"]

    # Modules — cluster around their product
    modules = by_type.get("module", [])
    mods_by_product = {}
    for n in modules:
        pid = parent_of.get(n["id"])
        mods_by_product.setdefault(pid, []).append(n)

    module_angles = {}
    for pid, mods in mods_by_product.items():
        base_a = product_angles.get(pid, 0)
        spread = math.pi * 0.8 if len(mods) > 8 else math.pi * 0.5
        for i, n in enumerate(mods):
            a = base_a - spread / 2 + (spread / max(1, len(mods) - 1)) * i
            module_angles[n["id"]] = a
            n["x"] = math.cos(a) * RINGS["module"]
            n["y"] = math.sin(a) * RINGS["module"]

    # Frontend pages — cluster around their product
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
# 4. MAIN
# ================================================================
if __name__ == "__main__":
    print("🔍 Building code-based knowledge graph...")
    data = build_graph()
    data = apply_layout(data)

    out = "/tmp/graph_data_v6.json"
    with open(out, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ {len(data['nodes'])} nodes, {len(data['edges'])} edges")
    print(f"   Written to {out}")

    # Stats
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
