# Crescendo Lab — Code Architecture Knowledge Graph v7 (LLM-Optimized)

> Auto-generated from deep codebase analysis on 2026-03-03 16:20
> Repos: rubato (MAAC BE), Grazioso (MAAC FE), cantata (CAAC BE), Zeffiroso (CAAC FE), bebop (DAAC), polyrhythmic (CDH)
> Nodes: 155 | Edges: 915
> Edge breakdown: code_dep=319, const_ref=166, model_ref=125, hierarchy=123, task_dep=59, api_call=54, infra_dep=37, api_client=17, service_dep=11, data_sync=4
> Purpose: Verified architecture map with semantic dependency types — for LLM impact analysis, attribution & root-cause tracing.
> 🔗 Interactive graph: https://doc-2-md.vercel.app/

**📌 Deep-link convention:** Every module, product, infrastructure, and frontend page name in this document is a clickable link.
Links follow the pattern `https://doc-2-md.vercel.app/#node=<label>` and open the interactive knowledge graph focused on that node.
When referencing a module in conversation, include its link so the user can jump directly to the interactive view.

---

## 1. Product Suite

### [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **MAAC**: Marketing Automation & Analytics Cloud
- Tech: MAAC — Marketing Automation & Analytics Cloud
Tech: Django 3.2 + React 19 (TypeScript)
Repos: {'backend': 'rubato (Python/Django)', 'frontend': 'Grazioso (React/TS)'}
- Repos: rubato (Python/Django) + Grazioso (React/TS)

- Backend modules: 54
- Frontend pages: 26

**Cross-product connections:**
- → [CAAC](https://doc-2-md.vercel.app/#node=CAAC): CAAC_CANTATA_URL (REST API)
- → [DAAC](https://doc-2-md.vercel.app/#node=DAAC): DAAC_API_URL (REST API)
- ← [CDH](https://doc-2-md.vercel.app/#node=CDH): RUBATO_HOST + RUBATO_DB_DSN
- ← [CAAC](https://doc-2-md.vercel.app/#node=CAAC): MAAC_URL (REST API)
- ← [DAAC](https://doc-2-md.vercel.app/#node=DAAC): MAAC_GCP_PROJECT_ID (BigQuery)

### [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **CAAC**: Conversation Automation & Analytics Cloud
- Tech: CAAC — Conversation Automation & Analytics Cloud
Tech: Go (Cantata) + React (Zeffiroso/TS)
Repos: {'backend': 'cantata (Go)', 'frontend': 'Zeffiroso (React/TS)'}
- Repos: cantata (Go) + Zeffiroso (React/TS)

- Backend modules: 13
- Frontend pages: 6

**Cross-product connections:**
- → [MAAC](https://doc-2-md.vercel.app/#node=MAAC): MAAC_URL (REST API)
- → [CDH](https://doc-2-md.vercel.app/#node=CDH): CDH_INTERNAL_URL (Unification V2)
- ← [MAAC](https://doc-2-md.vercel.app/#node=MAAC): CAAC_CANTATA_URL (REST API)
- ← [CDH](https://doc-2-md.vercel.app/#node=CDH): CANTATA_HOST + CANTATA_DB_DSN
- ← [DAAC](https://doc-2-md.vercel.app/#node=DAAC): CAAC_GCP_PROJECT_ID (BigQuery)

### [DAAC](https://doc-2-md.vercel.app/#node=DAAC)
- **DAAC**: Data Automation & Analytics Cloud
- Tech: DAAC — Data Automation & Analytics Cloud
Tech: Python (FastAPI) + React + AI Agent
Repos: {'backend': 'bebop (Python/FastAPI)', 'frontend': 'bebop/frontend (React/TS)'}
- Repos: bebop (Python/FastAPI)

- Backend modules: 9
- Frontend pages: 0

**Cross-product connections:**
- → [MAAC](https://doc-2-md.vercel.app/#node=MAAC): MAAC_GCP_PROJECT_ID (BigQuery)
- → [CAAC](https://doc-2-md.vercel.app/#node=CAAC): CAAC_GCP_PROJECT_ID (BigQuery)
- ← [MAAC](https://doc-2-md.vercel.app/#node=MAAC): DAAC_API_URL (REST API)

### [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **CDH**: Customer Data Hub — Unified Contact Profile
- Tech: CDH — Customer Data Hub — Unified Contact Profile
Tech: Python + Go (Polyrhythmic)
Repos: {'backend': 'polyrhythmic (Python+Go)', 'frontend': 'N/A (API-only)'}
- Repos: polyrhythmic (Python+Go)

- Backend modules: 11
- Frontend pages: 0

**Cross-product connections:**
- → [MAAC](https://doc-2-md.vercel.app/#node=MAAC): RUBATO_HOST + RUBATO_DB_DSN
- → [CAAC](https://doc-2-md.vercel.app/#node=CAAC): CANTATA_HOST + CANTATA_DB_DSN
- ← [CAAC](https://doc-2-md.vercel.app/#node=CAAC): CDH_INTERNAL_URL (Unification V2)

## 2. Module Architecture

### MAAC Modules (54 total)

| Module | Description | code_dep | model_ref | const_ref | task_dep | api_client |
|--------|-------------|----------|-----------|-----------|----------|------------|
| **[accounts](https://doc-2-md.vercel.app/#node=maac/accounts)** | User authentication, SSO, 2FA, session management | 8 | 2 | 3 | 2 |  |
| **[ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation)** | AI content generation — copywriting, image generation | 2 |  | 1 |  |  |
| **[api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc)** | MAAC module: api_doc |  |  |  |  |  |
| **[async_wrapper](https://doc-2-md.vercel.app/#node=maac/async_wrapper)** | MAAC module: async_wrapper |  |  |  |  |  |
| **[audience](https://doc-2-md.vercel.app/#node=maac/audience)** | Contact management, segments, filters, ad platform audiences | 8 | 6 | 5 |  |  |
| **[auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply)** | Keyword auto-reply across LINE/FB/WhatsApp channels | 9 | 2 | 4 | 1 |  |
| **[bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery)** | BigQuery data pipeline integration | 1 | 1 | 3 |  |  |
| **[broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast)** | Push messaging (LINE/SMS/WhatsApp), scheduling, A/B test | 10 | 1 | 5 |  |  |
| **[caac](https://doc-2-md.vercel.app/#node=maac/caac)** | CAAC integration bridge — connects Rubato to Cantata | 4 | 2 | 1 |  |  |
| **[campaign](https://doc-2-md.vercel.app/#node=maac/campaign)** | Campaign orchestration — multi-channel campaign management | 2 | 2 | 2 |  |  |
| **[cdp](https://doc-2-md.vercel.app/#node=maac/cdp)** | Customer Data Platform — profile unification, data sync | 6 | 1 | 2 | 2 |  |
| **[channel](https://doc-2-md.vercel.app/#node=maac/channel)** | Multi-channel management (LINE/FB/IG/WhatsApp/Email/SMS) | 5 | 3 | 4 | 1 |  |
| **[coupon](https://doc-2-md.vercel.app/#node=maac/coupon)** | MAAC module: coupon |  |  |  |  |  |
| **[cyberbiz](https://doc-2-md.vercel.app/#node=maac/cyberbiz)** | Cyberbiz e-commerce integration | 1 | 1 |  |  |  |
| **[email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel)** | Email campaign delivery via SendGrid, bounce handling | 8 |  | 4 | 1 |  |
| **[extension](https://doc-2-md.vercel.app/#node=maac/extension)** | MAAC extension plugins — custom action nodes | 6 | 1 | 6 |  |  |
| **[fb](https://doc-2-md.vercel.app/#node=maac/fb)** | Facebook/Instagram messaging, comment auto-reply | 7 | 1 | 4 | 1 |  |
| **[firestore](https://doc-2-md.vercel.app/#node=maac/firestore)** | MAAC module: firestore | 1 | 1 |  |  |  |
| **[form](https://doc-2-md.vercel.app/#node=maac/form)** | SurveyCake form integration, response tracking | 2 | 1 | 3 | 3 | 2 |
| **[google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics)** | GA4/UTM tracking integration for campaigns | 1 | 4 | 1 |  |  |
| **[integration](https://doc-2-md.vercel.app/#node=maac/integration)** | MAAC module: integration | 2 | 1 |  |  |  |
| **[interlude](https://doc-2-md.vercel.app/#node=maac/interlude)** | MAAC module: interlude | 4 | 1 |  |  |  |
| **[internal](https://doc-2-md.vercel.app/#node=maac/internal)** | Internal admin tools — data migration, debugging | 15 | 5 | 6 | 3 | 2 |
| **[invoice](https://doc-2-md.vercel.app/#node=maac/invoice)** | Invoice management — receipt/reward redemption |  |  |  |  |  |
| **[journey](https://doc-2-md.vercel.app/#node=maac/journey)** | Customer journey automation (triggers, actions, conditions) | 14 | 5 | 7 | 1 |  |
| **[line](https://doc-2-md.vercel.app/#node=maac/line)** | Core LINE integration — messaging, rich menu, Flex, LIFF | 32 | 19 | 19 | 10 | 3 |
| **[message](https://doc-2-md.vercel.app/#node=maac/message)** | Message rendering engine — builds LINE/FB/SMS/Email messages | 4 | 1 | 3 |  |  |
| **[nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app)** | 91App e-commerce integration | 8 | 4 | 3 | 4 | 1 |
| **[notification](https://doc-2-md.vercel.app/#node=maac/notification)** | In-app notification system for admin users | 1 |  |  |  |  |
| **[openapi](https://doc-2-md.vercel.app/#node=maac/openapi)** | Public OpenAPI — external developer API endpoints | 20 | 5 | 13 | 5 | 2 |
| **[organization](https://doc-2-md.vercel.app/#node=maac/organization)** | Org/tenant management, billing, feature control, RBAC | 15 | 2 | 7 | 1 |  |
| **[payment](https://doc-2-md.vercel.app/#node=maac/payment)** | Payment & billing — subscription, invoice management | 4 | 2 | 2 | 1 |  |
| **[prize](https://doc-2-md.vercel.app/#node=maac/prize)** | Prize/reward management, lottery, coupon distribution | 8 | 5 | 6 | 4 | 1 |
| **[pubsub](https://doc-2-md.vercel.app/#node=maac/pubsub)** | MAAC module: pubsub |  |  |  |  |  |
| **[pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull)** | PubSub consumer — event processing workers | 4 |  | 5 | 2 |  |
| **[receipt](https://doc-2-md.vercel.app/#node=maac/receipt)** | Receipt registration campaign for loyalty programs | 8 | 2 | 2 | 2 | 1 |
| **[referral](https://doc-2-md.vercel.app/#node=maac/referral)** | Rapid Referral — MGM campaigns, invitation tracking | 4 | 4 | 3 | 3 | 1 |
| **[report](https://doc-2-md.vercel.app/#node=maac/report)** | Analytics & reporting — campaign performance, member stats | 3 | 6 | 2 |  |  |
| **[sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando)** | Prize fulfillment partner integration | 4 | 4 | 1 | 2 | 1 |
| **[shopify](https://doc-2-md.vercel.app/#node=maac/shopify)** | Shopify e-commerce integration | 1 | 3 | 1 | 1 |  |
| **[shopline](https://doc-2-md.vercel.app/#node=maac/shopline)** | Shopline e-commerce integration | 6 | 3 | 2 | 3 | 1 |
| **[shortener](https://doc-2-md.vercel.app/#node=maac/shortener)** | MAAC module: shortener |  |  | 1 |  |  |
| **[smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test)** | Automated smoke test — system health validation | 7 | 5 | 6 |  |  |
| **[sms](https://doc-2-md.vercel.app/#node=maac/sms)** | SMS delivery — domestic/international SMS campaigns | 11 | 4 | 7 |  | 2 |
| **[sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus)** | SMS Plus — enhanced SMS features, message records | 9 |  | 3 |  |  |
| **[staticfiles](https://doc-2-md.vercel.app/#node=maac/staticfiles)** | MAAC module: staticfiles |  |  |  |  |  |
| **[stress_test](https://doc-2-md.vercel.app/#node=maac/stress_test)** | MAAC module: stress_test |  |  |  |  |  |
| **[system](https://doc-2-md.vercel.app/#node=maac/system)** | System-wide utilities — campaign tracking, feature flags | 7 | 6 | 4 | 2 |  |
| **[tag](https://doc-2-md.vercel.app/#node=maac/tag)** | Tag management — contact tagging, auto-tagging rules | 6 | 3 | 3 | 2 |  |
| **[verification](https://doc-2-md.vercel.app/#node=maac/verification)** | MAAC module: verification | 1 |  |  |  |  |
| **[wccs](https://doc-2-md.vercel.app/#node=maac/wccs)** | MAAC module: wccs | 4 |  | 4 | 1 |  |
| **[webhook](https://doc-2-md.vercel.app/#node=maac/webhook)** | Webhook delivery — event push to external systems | 4 | 4 | 1 |  |  |
| **[whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)** | WhatsApp Business messaging, template management | 7 |  | 6 | 1 |  |
| **[workflow](https://doc-2-md.vercel.app/#node=maac/workflow)** | MAAC module: workflow |  | 2 | 1 |  |  |

### CAAC Modules (13 total)

| Module | Description | code_dep | model_ref | const_ref | task_dep | api_client |
|--------|-------------|----------|-----------|-----------|----------|------------|
| **[aistrategy](https://doc-2-md.vercel.app/#node=caac/aistrategy)** | AI strategy configuration — model selection, prompts |  |  |  |  |  |
| **[aitask](https://doc-2-md.vercel.app/#node=caac/aitask)** | AI task execution — auto-reply suggestions, summarization | 3 |  |  |  |  |
| **[aiusage](https://doc-2-md.vercel.app/#node=caac/aiusage)** | AI usage tracking — token consumption, quota |  |  |  |  |  |
| **[auth](https://doc-2-md.vercel.app/#node=caac/auth)** | Authentication & authorization — SSO, 2FA |  |  |  |  |  |
| **[cat](https://doc-2-md.vercel.app/#node=caac/cat)** | CAT (Contact Attribution Tracking) — member journey tracking |  |  |  |  |  |
| **[cdp](https://doc-2-md.vercel.app/#node=caac/cdp)** | CDP integration — unified contact view within CAAC |  |  |  |  |  |
| **[chat](https://doc-2-md.vercel.app/#node=caac/chat)** | Core 1-on-1 chat — message routing, conversation lifecycle | 5 |  |  |  |  |
| **[dashboard](https://doc-2-md.vercel.app/#node=caac/dashboard)** | CAAC analytics dashboard — conversation metrics, team perfor |  |  |  |  |  |
| **[longrunningtask](https://doc-2-md.vercel.app/#node=caac/longrunningtask)** | Long-running operations — bulk exports, data migration | 1 |  |  |  |  |
| **[openapi](https://doc-2-md.vercel.app/#node=caac/openapi)** | CAAC public API for external integrations |  |  |  |  |  |
| **[organization](https://doc-2-md.vercel.app/#node=caac/organization)** | Organization management — channels, users, roles, AI feature | 1 |  |  |  |  |
| **[tag](https://doc-2-md.vercel.app/#node=caac/tag)** | Contact tagging within CAAC conversations |  |  |  |  |  |
| **[workertask](https://doc-2-md.vercel.app/#node=caac/workertask)** | Background worker tasks — message processing, sync jobs | 1 |  |  |  |  |

### DAAC Modules (9 total)

| Module | Description | code_dep | model_ref | const_ref | task_dep | api_client |
|--------|-------------|----------|-----------|-----------|----------|------------|
| **[agent_v2](https://doc-2-md.vercel.app/#node=daac/agent_v2)** | AI Agent — natural language data querying (OpenAI/Gemini) | 1 |  |  |  |  |
| **[auth](https://doc-2-md.vercel.app/#node=daac/auth)** | Authentication via Arioso SSO + Interlude |  |  |  |  |  |
| **[dashboard](https://doc-2-md.vercel.app/#node=daac/dashboard)** | Custom analytics dashboards — user-created visualizations | 1 |  |  |  |  |
| **[dbt](https://doc-2-md.vercel.app/#node=daac/dbt)** | dbt pipeline management — data transformation & modeling | 1 |  |  |  |  |
| **[file](https://doc-2-md.vercel.app/#node=daac/file)** | File management — upload/download for analysis results |  |  |  |  |  |
| **[infra](https://doc-2-md.vercel.app/#node=daac/infra)** | Infrastructure provisioning — Terraform client setup | 1 |  |  |  |  |
| **[journey](https://doc-2-md.vercel.app/#node=daac/journey)** | Journey analysis — customer path analysis via AI | 1 |  |  |  |  |
| **[organization](https://doc-2-md.vercel.app/#node=daac/organization)** | Org management — workspace, dbt config, Terraform infra | 1 |  |  |  |  |
| **[session](https://doc-2-md.vercel.app/#node=daac/session)** | AI analysis session — conversation state, context management | 2 |  |  |  |  |

### CDH Modules (11 total)

| Module | Description | code_dep | model_ref | const_ref | task_dep | api_client |
|--------|-------------|----------|-----------|-----------|----------|------------|
| **[broadcast](https://doc-2-md.vercel.app/#node=cdh/broadcast)** | CDH broadcast coordination — cross-product message dispatch |  |  |  |  |  |
| **[channel_entity_comment](https://doc-2-md.vercel.app/#node=cdh/channel_entity_comment)** | Channel entity commenting — AI-powered contact annotations |  |  |  |  |  |
| **[contact](https://doc-2-md.vercel.app/#node=cdh/contact)** | Unified contact profile — cross-product contact view | 1 |  |  |  |  |
| **[custom_field](https://doc-2-md.vercel.app/#node=cdh/custom_field)** | Custom contact fields — user-defined attributes |  |  |  |  |  |
| **[engagement_history](https://doc-2-md.vercel.app/#node=cdh/engagement_history)** | Engagement history — cross-channel interaction tracking |  |  |  |  |  |
| **[member](https://doc-2-md.vercel.app/#node=cdh/member)** | Member management — import/export, profile enrichment | 2 |  |  |  |  |
| **[richmenu](https://doc-2-md.vercel.app/#node=cdh/richmenu)** | LINE Rich Menu management via CDH |  |  |  |  |  |
| **[segment](https://doc-2-md.vercel.app/#node=cdh/segment)** | Cross-product audience segmentation via SQL/LLM |  |  |  |  |  |
| **[tag](https://doc-2-md.vercel.app/#node=cdh/tag)** | Cross-product tag synchronization | 1 |  |  |  |  |
| **[task](https://doc-2-md.vercel.app/#node=cdh/task)** | Background task execution — unification, sync, export jobs |  |  |  |  |  |
| **[unification](https://doc-2-md.vercel.app/#node=cdh/unification)** | Contact unification graph — merge/split profiles across chan | 2 |  |  |  |  |

## 3. Semantic Dependency Types

v7 differentiates generic `code_dep` into fine-grained relationship types:

- **`model_ref`** (125 edges) — Model Reference — imports Django/Go models from another module
- **`const_ref`** (166 edges) — Constant Reference — imports settings, constants, or enums
- **`task_dep`** (59 edges) — Task Dependency — calls or enqueues a Celery/async task
- **`api_client`** (17 edges) — API Client — uses an HTTP client to call another service
- **`code_dep`** (319 edges) — General Python/Go import dependency (catch-all)

### Semantic Dependency Distribution by Product

| Product | code_dep | model_ref | const_ref | task_dep | api_client | Total |
|---------|----------|-----------|-----------|----------|------------|-------|
| **MAAC** | 294 | 125 | 166 | 59 | 17 | 661 |
| **CAAC** | 11 | 0 | 0 | 0 | 0 | 11 |
| **DAAC** | 8 | 0 | 0 | 0 | 0 | 8 |
| **CDH** | 6 | 0 | 0 | 0 | 0 | 6 |

## 4. Module Details

### [MAAC/accounts](https://doc-2-md.vercel.app/#node=maac/accounts)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: User authentication, SSO, 2FA, session management
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **model_ref** → [organization](https://doc-2-md.vercel.app/#node=maac/organization), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **const_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **task_dep** → [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← model_ref** from: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [campaign](https://doc-2-md.vercel.app/#node=maac/campaign), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [cyberbiz](https://doc-2-md.vercel.app/#node=maac/cyberbiz), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [integration](https://doc-2-md.vercel.app/#node=maac/integration), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← const_ref** from: [extension](https://doc-2-md.vercel.app/#node=maac/extension), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test)
- **← api_client** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal)
- **Frontend pages**: [Organization Settings](https://doc-2-md.vercel.app/#node=page/Organization%20Settings)

### [MAAC/ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: AI content generation — copywriting, image generation
- **code_dep** → [organization](https://doc-2-md.vercel.app/#node=maac/organization), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **const_ref** → [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **← code_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **← const_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line)

### [MAAC/api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: api_doc
- **← code_dep** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [campaign](https://doc-2-md.vercel.app/#node=maac/campaign), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [form](https://doc-2-md.vercel.app/#node=maac/form), [integration](https://doc-2-md.vercel.app/#node=maac/integration), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)

### [MAAC/async_wrapper](https://doc-2-md.vercel.app/#node=maac/async_wrapper)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: async_wrapper
- **← code_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt)
- **← const_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line)

### [MAAC/audience](https://doc-2-md.vercel.app/#node=maac/audience)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Contact management, segments, filters, ad platform audiences
- **code_dep** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **const_ref** → [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← code_dep** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [firestore](https://doc-2-md.vercel.app/#node=maac/firestore), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← model_ref** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← const_ref** from: [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **← task_dep** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi)
- **Frontend pages**: [Members](https://doc-2-md.vercel.app/#node=page/Members), [Retarget](https://doc-2-md.vercel.app/#node=page/Retarget), [Segment](https://doc-2-md.vercel.app/#node=page/Segment)

### [MAAC/auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Keyword auto-reply across LINE/FB/WhatsApp channels
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [pubsub](https://doc-2-md.vercel.app/#node=maac/pubsub), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **const_ref** → [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **task_dep** → [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← code_dep** from: [fb](https://doc-2-md.vercel.app/#node=maac/fb), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **← const_ref** from: [fb](https://doc-2-md.vercel.app/#node=maac/fb), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **Frontend pages**: [Auto Reply](https://doc-2-md.vercel.app/#node=page/Auto%20Reply)

### [MAAC/bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: BigQuery data pipeline integration
- **code_dep** → [receipt](https://doc-2-md.vercel.app/#node=maac/receipt)
- **model_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **const_ref** → [audience](https://doc-2-md.vercel.app/#node=maac/audience), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← code_dep** from: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [report](https://doc-2-md.vercel.app/#node=maac/report), [system](https://doc-2-md.vercel.app/#node=maac/system)

### [MAAC/broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Push messaging (LINE/SMS/WhatsApp), scheduling, A/B test
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [report](https://doc-2-md.vercel.app/#node=maac/report), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts)
- **const_ref** → [audience](https://doc-2-md.vercel.app/#node=maac/audience), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **Frontend pages**: [Broadcast](https://doc-2-md.vercel.app/#node=page/Broadcast)

### [MAAC/caac](https://doc-2-md.vercel.app/#node=maac/caac)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: CAAC integration bridge — connects Rubato to Cantata
- **code_dep** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **const_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization)

### [MAAC/campaign](https://doc-2-md.vercel.app/#node=maac/campaign)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Campaign orchestration — multi-channel campaign management
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [journey](https://doc-2-md.vercel.app/#node=maac/journey)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [journey](https://doc-2-md.vercel.app/#node=maac/journey)
- **const_ref** → [channel](https://doc-2-md.vercel.app/#node=maac/channel), [journey](https://doc-2-md.vercel.app/#node=maac/journey)

### [MAAC/cdp](https://doc-2-md.vercel.app/#node=maac/cdp)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Customer Data Platform — profile unification, data sync
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts)
- **const_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **task_dep** → [journey](https://doc-2-md.vercel.app/#node=maac/journey), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← code_dep** from: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← const_ref** from: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **Frontend pages**: [Members](https://doc-2-md.vercel.app/#node=page/Members)

### [MAAC/channel](https://doc-2-md.vercel.app/#node=maac/channel)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Multi-channel management (LINE/FB/IG/WhatsApp/Email/SMS)
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **const_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **task_dep** → [notification](https://doc-2-md.vercel.app/#node=maac/notification)
- **← code_dep** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **← model_ref** from: [journey](https://doc-2-md.vercel.app/#node=maac/journey)
- **← const_ref** from: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [campaign](https://doc-2-md.vercel.app/#node=maac/campaign), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **Frontend pages**: [Channel Settings](https://doc-2-md.vercel.app/#node=page/Channel%20Settings)

### [MAAC/coupon](https://doc-2-md.vercel.app/#node=maac/coupon)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: coupon

### [MAAC/cyberbiz](https://doc-2-md.vercel.app/#node=maac/cyberbiz)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Cyberbiz e-commerce integration
- **code_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts)

### [MAAC/email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Email campaign delivery via SendGrid, bounce handling
- **code_dep** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **const_ref** → [channel](https://doc-2-md.vercel.app/#node=maac/channel), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **task_dep** → [journey](https://doc-2-md.vercel.app/#node=maac/journey)
- **← code_dep** from: [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi)
- **Frontend pages**: [Journey](https://doc-2-md.vercel.app/#node=page/Journey)

### [MAAC/extension](https://doc-2-md.vercel.app/#node=maac/extension)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC extension plugins — custom action nodes
- **code_dep** → [channel](https://doc-2-md.vercel.app/#node=maac/channel), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts)
- **const_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [journey](https://doc-2-md.vercel.app/#node=maac/journey)

### [MAAC/fb](https://doc-2-md.vercel.app/#node=maac/fb)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Facebook/Instagram messaging, comment auto-reply
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [pubsub](https://doc-2-md.vercel.app/#node=maac/pubsub)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts)
- **const_ref** → [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **task_dep** → [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← code_dep** from: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test)
- **← const_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **Frontend pages**: [Auto Reply](https://doc-2-md.vercel.app/#node=page/Auto%20Reply), [Retarget](https://doc-2-md.vercel.app/#node=page/Retarget)

### [MAAC/firestore](https://doc-2-md.vercel.app/#node=maac/firestore)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: firestore
- **code_dep** → [audience](https://doc-2-md.vercel.app/#node=maac/audience)
- **model_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system)

### [MAAC/form](https://doc-2-md.vercel.app/#node=maac/form)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: SurveyCake form integration, response tracking
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **model_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **const_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **task_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **api_client** → [line](https://doc-2-md.vercel.app/#node=maac/line), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← model_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **Frontend pages**: [SurveyCake (Form)](https://doc-2-md.vercel.app/#node=page/SurveyCake%20%28Form%29)

### [MAAC/google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: GA4/UTM tracking integration for campaigns
- **code_dep** → [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [report](https://doc-2-md.vercel.app/#node=maac/report)
- **const_ref** → [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← code_dep** from: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **← model_ref** from: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [report](https://doc-2-md.vercel.app/#node=maac/report), [system](https://doc-2-md.vercel.app/#node=maac/system), [workflow](https://doc-2-md.vercel.app/#node=maac/workflow)
- **← const_ref** from: [extension](https://doc-2-md.vercel.app/#node=maac/extension), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize)
- **Frontend pages**: [Insight (Dashboard)](https://doc-2-md.vercel.app/#node=page/Insight%20%28Dashboard%29), [Tracelink](https://doc-2-md.vercel.app/#node=page/Tracelink)

### [MAAC/integration](https://doc-2-md.vercel.app/#node=maac/integration)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: integration
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts)

### [MAAC/interlude](https://doc-2-md.vercel.app/#node=maac/interlude)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: interlude
- **code_dep** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts)
- **← code_dep** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus)
- **← const_ref** from: [extension](https://doc-2-md.vercel.app/#node=maac/extension), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [sms](https://doc-2-md.vercel.app/#node=maac/sms)

### [MAAC/internal](https://doc-2-md.vercel.app/#node=maac/internal)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Internal admin tools — data migration, debugging
- **code_dep** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **model_ref** → [audience](https://doc-2-md.vercel.app/#node=maac/audience), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **const_ref** → [audience](https://doc-2-md.vercel.app/#node=maac/audience), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **task_dep** → [audience](https://doc-2-md.vercel.app/#node=maac/audience), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **api_client** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [organization](https://doc-2-md.vercel.app/#node=maac/organization)

### [MAAC/invoice](https://doc-2-md.vercel.app/#node=maac/invoice)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Invoice management — receipt/reward redemption

### [MAAC/journey](https://doc-2-md.vercel.app/#node=maac/journey)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Customer journey automation (triggers, actions, conditions)
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [report](https://doc-2-md.vercel.app/#node=maac/report), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **const_ref** → [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **task_dep** → [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← code_dep** from: [campaign](https://doc-2-md.vercel.app/#node=maac/campaign), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [line](https://doc-2-md.vercel.app/#node=maac/line), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← model_ref** from: [campaign](https://doc-2-md.vercel.app/#node=maac/campaign), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test)
- **← const_ref** from: [campaign](https://doc-2-md.vercel.app/#node=maac/campaign), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **← task_dep** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **Frontend pages**: [Journey](https://doc-2-md.vercel.app/#node=page/Journey)

### [MAAC/line](https://doc-2-md.vercel.app/#node=maac/line)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Core LINE integration — messaging, rich menu, Flex, LIFF
- **code_dep** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation), [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [async_wrapper](https://doc-2-md.vercel.app/#node=maac/async_wrapper), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [firestore](https://doc-2-md.vercel.app/#node=maac/firestore), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [message](https://doc-2-md.vercel.app/#node=maac/message), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub](https://doc-2-md.vercel.app/#node=maac/pubsub), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [report](https://doc-2-md.vercel.app/#node=maac/report), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [form](https://doc-2-md.vercel.app/#node=maac/form), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [report](https://doc-2-md.vercel.app/#node=maac/report), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook), [workflow](https://doc-2-md.vercel.app/#node=maac/workflow)
- **const_ref** → [ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation), [async_wrapper](https://doc-2-md.vercel.app/#node=maac/async_wrapper), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [message](https://doc-2-md.vercel.app/#node=maac/message), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp), [workflow](https://doc-2-md.vercel.app/#node=maac/workflow)
- **task_dep** → [audience](https://doc-2-md.vercel.app/#node=maac/audience), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **api_client** → [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [referral](https://doc-2-md.vercel.app/#node=maac/referral)
- **← code_dep** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [cyberbiz](https://doc-2-md.vercel.app/#node=maac/cyberbiz), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [form](https://doc-2-md.vercel.app/#node=maac/form), [integration](https://doc-2-md.vercel.app/#node=maac/integration), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [message](https://doc-2-md.vercel.app/#node=maac/message), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [report](https://doc-2-md.vercel.app/#node=maac/report), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [verification](https://doc-2-md.vercel.app/#node=maac/verification), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **← model_ref** from: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [firestore](https://doc-2-md.vercel.app/#node=maac/firestore), [form](https://doc-2-md.vercel.app/#node=maac/form), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [message](https://doc-2-md.vercel.app/#node=maac/message), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [report](https://doc-2-md.vercel.app/#node=maac/report), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook), [workflow](https://doc-2-md.vercel.app/#node=maac/workflow)
- **← const_ref** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [form](https://doc-2-md.vercel.app/#node=maac/form), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [report](https://doc-2-md.vercel.app/#node=maac/report), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **← task_dep** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [form](https://doc-2-md.vercel.app/#node=maac/form), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← api_client** from: [form](https://doc-2-md.vercel.app/#node=maac/form), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **Frontend pages**: [Beacon](https://doc-2-md.vercel.app/#node=page/Beacon), [Bindlink](https://doc-2-md.vercel.app/#node=page/Bindlink), [DPM](https://doc-2-md.vercel.app/#node=page/DPM), [Deeplink](https://doc-2-md.vercel.app/#node=page/Deeplink), [Interaction Games](https://doc-2-md.vercel.app/#node=page/Interaction%20Games), [Rich Menu](https://doc-2-md.vercel.app/#node=page/Rich%20Menu), [Template Library](https://doc-2-md.vercel.app/#node=page/Template%20Library), [Widget](https://doc-2-md.vercel.app/#node=page/Widget)

### [MAAC/message](https://doc-2-md.vercel.app/#node=maac/message)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Message rendering engine — builds LINE/FB/SMS/Email messages
- **code_dep** → [channel](https://doc-2-md.vercel.app/#node=maac/channel), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **model_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **const_ref** → [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← code_dep** from: [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **← const_ref** from: [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **Frontend pages**: [Broadcast](https://doc-2-md.vercel.app/#node=page/Broadcast), [Template Library](https://doc-2-md.vercel.app/#node=page/Template%20Library)

### [MAAC/nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: 91App e-commerce integration
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [async_wrapper](https://doc-2-md.vercel.app/#node=maac/async_wrapper), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **const_ref** → [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **task_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **api_client** → [openapi](https://doc-2-md.vercel.app/#node=maac/openapi)
- **← code_dep** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← model_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← task_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line)

### [MAAC/notification](https://doc-2-md.vercel.app/#node=maac/notification)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: In-app notification system for admin users
- **code_dep** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts)
- **← code_dep** from: [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus)
- **← model_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [payment](https://doc-2-md.vercel.app/#node=maac/payment)
- **← const_ref** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← task_dep** from: [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize)

### [MAAC/openapi](https://doc-2-md.vercel.app/#node=maac/openapi)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Public OpenAPI — external developer API endpoints
- **code_dep** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation), [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [report](https://doc-2-md.vercel.app/#node=maac/report), [shortener](https://doc-2-md.vercel.app/#node=maac/shortener), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **model_ref** → [audience](https://doc-2-md.vercel.app/#node=maac/audience), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **const_ref** → [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **task_dep** → [audience](https://doc-2-md.vercel.app/#node=maac/audience), [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **api_client** → [line](https://doc-2-md.vercel.app/#node=maac/line), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **← code_dep** from: [channel](https://doc-2-md.vercel.app/#node=maac/channel), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **← model_ref** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [report](https://doc-2-md.vercel.app/#node=maac/report), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **← const_ref** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **← task_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app)
- **← api_client** from: [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **Frontend pages**: [API Token](https://doc-2-md.vercel.app/#node=page/API%20Token)

### [MAAC/organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Org/tenant management, billing, feature control, RBAC
- **code_dep** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation), [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **const_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification)
- **task_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **← model_ref** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **← const_ref** from: [ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi)
- **← task_dep** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal)
- **← api_client** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **Frontend pages**: [Organization Settings](https://doc-2-md.vercel.app/#node=page/Organization%20Settings)

### [MAAC/payment](https://doc-2-md.vercel.app/#node=maac/payment)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Payment & billing — subscription, invoice management
- **code_dep** → [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **model_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification)
- **const_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification)
- **task_dep** → [notification](https://doc-2-md.vercel.app/#node=maac/notification)
- **← code_dep** from: [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [report](https://doc-2-md.vercel.app/#node=maac/report), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus)
- **← model_ref** from: [report](https://doc-2-md.vercel.app/#node=maac/report)

### [MAAC/prize](https://doc-2-md.vercel.app/#node=maac/prize)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Prize/reward management, lottery, coupon distribution
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [report](https://doc-2-md.vercel.app/#node=maac/report), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **const_ref** → [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **task_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **api_client** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **← model_ref** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando)
- **← const_ref** from: [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [referral](https://doc-2-md.vercel.app/#node=maac/referral)
- **← task_dep** from: [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando)
- **← api_client** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **Frontend pages**: [Interaction Games](https://doc-2-md.vercel.app/#node=page/Interaction%20Games), [Prize](https://doc-2-md.vercel.app/#node=page/Prize)

### [MAAC/pubsub](https://doc-2-md.vercel.app/#node=maac/pubsub)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: pubsub
- **← code_dep** from: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)

### [MAAC/pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: PubSub consumer — event processing workers
- **code_dep** → [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **const_ref** → [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **task_dep** → [journey](https://doc-2-md.vercel.app/#node=maac/journey), [tag](https://doc-2-md.vercel.app/#node=maac/tag)

### [MAAC/receipt](https://doc-2-md.vercel.app/#node=maac/receipt)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Receipt registration campaign for loyalty programs
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [async_wrapper](https://doc-2-md.vercel.app/#node=maac/async_wrapper), [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **model_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [prize](https://doc-2-md.vercel.app/#node=maac/prize)
- **const_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **task_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **api_client** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← model_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **← const_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **Frontend pages**: [Receipt Register](https://doc-2-md.vercel.app/#node=page/Receipt%20Register)

### [MAAC/referral](https://doc-2-md.vercel.app/#node=maac/referral)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Rapid Referral — MGM campaigns, invitation tracking
- **code_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **const_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **task_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **api_client** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← model_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← api_client** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **Frontend pages**: [Referral V2](https://doc-2-md.vercel.app/#node=page/Referral%20V2)

### [MAAC/report](https://doc-2-md.vercel.app/#node=maac/report)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Analytics & reporting — campaign performance, member stats
- **code_dep** → [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [line](https://doc-2-md.vercel.app/#node=maac/line), [payment](https://doc-2-md.vercel.app/#node=maac/payment)
- **model_ref** → [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **const_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← code_dep** from: [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **← model_ref** from: [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **Frontend pages**: [Insight (Dashboard)](https://doc-2-md.vercel.app/#node=page/Insight%20%28Dashboard%29)

### [MAAC/sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Prize fulfillment partner integration
- **code_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize)
- **const_ref** → [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **task_dep** → [prize](https://doc-2-md.vercel.app/#node=maac/prize), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **api_client** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line), [prize](https://doc-2-md.vercel.app/#node=maac/prize)
- **Frontend pages**: [Prize](https://doc-2-md.vercel.app/#node=page/Prize)

### [MAAC/shopify](https://doc-2-md.vercel.app/#node=maac/shopify)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Shopify e-commerce integration
- **code_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **const_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **task_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← model_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line)

### [MAAC/shopline](https://doc-2-md.vercel.app/#node=maac/shopline)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Shopline e-commerce integration
- **code_dep** → [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **const_ref** → [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **task_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **api_client** → [openapi](https://doc-2-md.vercel.app/#node=maac/openapi)
- **← code_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← model_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← task_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line)

### [MAAC/shortener](https://doc-2-md.vercel.app/#node=maac/shortener)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: shortener
- **const_ref** → [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← code_dep** from: [openapi](https://doc-2-md.vercel.app/#node=maac/openapi)

### [MAAC/smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Automated smoke test — system health validation
- **code_dep** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **model_ref** → [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **const_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [tag](https://doc-2-md.vercel.app/#node=maac/tag)

### [MAAC/sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: SMS delivery — domestic/international SMS campaigns
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [report](https://doc-2-md.vercel.app/#node=maac/report), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **model_ref** → [audience](https://doc-2-md.vercel.app/#node=maac/audience), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **const_ref** → [audience](https://doc-2-md.vercel.app/#node=maac/audience), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **api_client** → [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi)
- **← code_dep** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus)
- **← model_ref** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← const_ref** from: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus)
- **← task_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← api_client** from: [openapi](https://doc-2-md.vercel.app/#node=maac/openapi)
- **Frontend pages**: [Broadcast](https://doc-2-md.vercel.app/#node=page/Broadcast), [SMS Plus](https://doc-2-md.vercel.app/#node=page/SMS%20Plus)

### [MAAC/sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: SMS Plus — enhanced SMS features, message records
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **const_ref** → [notification](https://doc-2-md.vercel.app/#node=maac/notification), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- **← model_ref** from: [report](https://doc-2-md.vercel.app/#node=maac/report)
- **Frontend pages**: [SMS Plus](https://doc-2-md.vercel.app/#node=page/SMS%20Plus)

### [MAAC/staticfiles](https://doc-2-md.vercel.app/#node=maac/staticfiles)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: staticfiles

### [MAAC/stress_test](https://doc-2-md.vercel.app/#node=maac/stress_test)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: stress_test

### [MAAC/system](https://doc-2-md.vercel.app/#node=maac/system)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: System-wide utilities — campaign tracking, feature flags
- **code_dep** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [firestore](https://doc-2-md.vercel.app/#node=maac/firestore), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [pubsub](https://doc-2-md.vercel.app/#node=maac/pubsub)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **const_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **task_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← code_dep** from: [ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **← model_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline)
- **← const_ref** from: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [report](https://doc-2-md.vercel.app/#node=maac/report), [shortener](https://doc-2-md.vercel.app/#node=maac/shortener), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp), [workflow](https://doc-2-md.vercel.app/#node=maac/workflow)
- **← task_dep** from: [line](https://doc-2-md.vercel.app/#node=maac/line)

### [MAAC/tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Tag management — contact tagging, auto-tagging rules
- **code_dep** → [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization)
- **model_ref** → [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [line](https://doc-2-md.vercel.app/#node=maac/line), [report](https://doc-2-md.vercel.app/#node=maac/report)
- **const_ref** → [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **task_dep** → [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← code_dep** from: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **← model_ref** from: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [report](https://doc-2-md.vercel.app/#node=maac/report), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← const_ref** from: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [form](https://doc-2-md.vercel.app/#node=maac/form), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← task_dep** from: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [form](https://doc-2-md.vercel.app/#node=maac/form), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [system](https://doc-2-md.vercel.app/#node=maac/system), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **← api_client** from: [form](https://doc-2-md.vercel.app/#node=maac/form)
- **Frontend pages**: [Members](https://doc-2-md.vercel.app/#node=page/Members), [Tag Manager](https://doc-2-md.vercel.app/#node=page/Tag%20Manager)

### [MAAC/verification](https://doc-2-md.vercel.app/#node=maac/verification)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: verification
- **code_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line)

### [MAAC/wccs](https://doc-2-md.vercel.app/#node=maac/wccs)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: wccs
- **code_dep** → [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [line](https://doc-2-md.vercel.app/#node=maac/line), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [pubsub](https://doc-2-md.vercel.app/#node=maac/pubsub)
- **const_ref** → [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **task_dep** → [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← code_dep** from: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [internal](https://doc-2-md.vercel.app/#node=maac/internal)

### [MAAC/webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: Webhook delivery — event push to external systems
- **code_dep** → [line](https://doc-2-md.vercel.app/#node=maac/line), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **model_ref** → [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [workflow](https://doc-2-md.vercel.app/#node=maac/workflow)
- **const_ref** → [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← code_dep** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline)
- **← model_ref** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← const_ref** from: [form](https://doc-2-md.vercel.app/#node=maac/form), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline)
- **← task_dep** from: [form](https://doc-2-md.vercel.app/#node=maac/form), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline)
- **Frontend pages**: [Webhook](https://doc-2-md.vercel.app/#node=page/Webhook)

### [MAAC/whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: WhatsApp Business messaging, template management
- **code_dep** → [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [pubsub](https://doc-2-md.vercel.app/#node=maac/pubsub)
- **const_ref** → [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [system](https://doc-2-md.vercel.app/#node=maac/system)
- **task_dep** → [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- **← code_dep** from: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus)
- **← const_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line)
- **← task_dep** from: [internal](https://doc-2-md.vercel.app/#node=maac/internal)
- **Frontend pages**: [Auto Reply](https://doc-2-md.vercel.app/#node=page/Auto%20Reply)

### [MAAC/workflow](https://doc-2-md.vercel.app/#node=maac/workflow)
- **Product**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)
- **Description**: MAAC module: workflow
- **model_ref** → [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line)
- **const_ref** → [system](https://doc-2-md.vercel.app/#node=maac/system)
- **← model_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- **← const_ref** from: [line](https://doc-2-md.vercel.app/#node=maac/line)

### [CAAC/aistrategy](https://doc-2-md.vercel.app/#node=caac/aistrategy)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: AI strategy configuration — model selection, prompts
- **← code_dep** from: [aitask](https://doc-2-md.vercel.app/#node=caac/aitask), [chat](https://doc-2-md.vercel.app/#node=caac/chat)
- **Frontend pages**: [AI Settings](https://doc-2-md.vercel.app/#node=caac_page/AI%20Settings)

### [CAAC/aitask](https://doc-2-md.vercel.app/#node=caac/aitask)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: AI task execution — auto-reply suggestions, summarization
- **code_dep** → [aistrategy](https://doc-2-md.vercel.app/#node=caac/aistrategy), [aiusage](https://doc-2-md.vercel.app/#node=caac/aiusage), [chat](https://doc-2-md.vercel.app/#node=caac/chat)
- **← code_dep** from: [organization](https://doc-2-md.vercel.app/#node=caac/organization)
- **Frontend pages**: [AI Settings](https://doc-2-md.vercel.app/#node=caac_page/AI%20Settings), [Chat](https://doc-2-md.vercel.app/#node=caac_page/Chat)

### [CAAC/aiusage](https://doc-2-md.vercel.app/#node=caac/aiusage)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: AI usage tracking — token consumption, quota
- **← code_dep** from: [aitask](https://doc-2-md.vercel.app/#node=caac/aitask), [chat](https://doc-2-md.vercel.app/#node=caac/chat), [workertask](https://doc-2-md.vercel.app/#node=caac/workertask)
- **Frontend pages**: [AI Settings](https://doc-2-md.vercel.app/#node=caac_page/AI%20Settings)

### [CAAC/auth](https://doc-2-md.vercel.app/#node=caac/auth)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: Authentication & authorization — SSO, 2FA
- **Frontend pages**: [Settings](https://doc-2-md.vercel.app/#node=caac_page/Settings)

### [CAAC/cat](https://doc-2-md.vercel.app/#node=caac/cat)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: CAT (Contact Attribution Tracking) — member journey tracking

### [CAAC/cdp](https://doc-2-md.vercel.app/#node=caac/cdp)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: CDP integration — unified contact view within CAAC
- **← code_dep** from: [chat](https://doc-2-md.vercel.app/#node=caac/chat)

### [CAAC/chat](https://doc-2-md.vercel.app/#node=caac/chat)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: Core 1-on-1 chat — message routing, conversation lifecycle
- **code_dep** → [aistrategy](https://doc-2-md.vercel.app/#node=caac/aistrategy), [aiusage](https://doc-2-md.vercel.app/#node=caac/aiusage), [cdp](https://doc-2-md.vercel.app/#node=caac/cdp), [organization](https://doc-2-md.vercel.app/#node=caac/organization), [tag](https://doc-2-md.vercel.app/#node=caac/tag)
- **← code_dep** from: [aitask](https://doc-2-md.vercel.app/#node=caac/aitask), [longrunningtask](https://doc-2-md.vercel.app/#node=caac/longrunningtask)
- **Frontend pages**: [Broadcast](https://doc-2-md.vercel.app/#node=caac_page/Broadcast), [Chat](https://doc-2-md.vercel.app/#node=caac_page/Chat), [Quick Template](https://doc-2-md.vercel.app/#node=caac_page/Quick%20Template)

### [CAAC/dashboard](https://doc-2-md.vercel.app/#node=caac/dashboard)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: CAAC analytics dashboard — conversation metrics, team performance
- **Frontend pages**: [Insights](https://doc-2-md.vercel.app/#node=caac_page/Insights)

### [CAAC/longrunningtask](https://doc-2-md.vercel.app/#node=caac/longrunningtask)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: Long-running operations — bulk exports, data migration
- **code_dep** → [chat](https://doc-2-md.vercel.app/#node=caac/chat)

### [CAAC/openapi](https://doc-2-md.vercel.app/#node=caac/openapi)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: CAAC public API for external integrations

### [CAAC/organization](https://doc-2-md.vercel.app/#node=caac/organization)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: Organization management — channels, users, roles, AI features
- **code_dep** → [aitask](https://doc-2-md.vercel.app/#node=caac/aitask)
- **← code_dep** from: [chat](https://doc-2-md.vercel.app/#node=caac/chat)
- **Frontend pages**: [Settings](https://doc-2-md.vercel.app/#node=caac_page/Settings)

### [CAAC/tag](https://doc-2-md.vercel.app/#node=caac/tag)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: Contact tagging within CAAC conversations
- **← code_dep** from: [chat](https://doc-2-md.vercel.app/#node=caac/chat)

### [CAAC/workertask](https://doc-2-md.vercel.app/#node=caac/workertask)
- **Product**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)
- **Description**: Background worker tasks — message processing, sync jobs
- **code_dep** → [aiusage](https://doc-2-md.vercel.app/#node=caac/aiusage)

### [DAAC/agent_v2](https://doc-2-md.vercel.app/#node=daac/agent_v2)
- **Product**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)
- **Description**: AI Agent — natural language data querying (OpenAI/Gemini)
- **code_dep** → [session](https://doc-2-md.vercel.app/#node=daac/session)

### [DAAC/auth](https://doc-2-md.vercel.app/#node=daac/auth)
- **Product**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)
- **Description**: Authentication via Arioso SSO + Interlude
- **← code_dep** from: [organization](https://doc-2-md.vercel.app/#node=daac/organization), [session](https://doc-2-md.vercel.app/#node=daac/session)

### [DAAC/dashboard](https://doc-2-md.vercel.app/#node=daac/dashboard)
- **Product**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)
- **Description**: Custom analytics dashboards — user-created visualizations
- **code_dep** → [organization](https://doc-2-md.vercel.app/#node=daac/organization)

### [DAAC/dbt](https://doc-2-md.vercel.app/#node=daac/dbt)
- **Product**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)
- **Description**: dbt pipeline management — data transformation & modeling
- **code_dep** → [organization](https://doc-2-md.vercel.app/#node=daac/organization)

### [DAAC/file](https://doc-2-md.vercel.app/#node=daac/file)
- **Product**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)
- **Description**: File management — upload/download for analysis results

### [DAAC/infra](https://doc-2-md.vercel.app/#node=daac/infra)
- **Product**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)
- **Description**: Infrastructure provisioning — Terraform client setup
- **code_dep** → [organization](https://doc-2-md.vercel.app/#node=daac/organization)

### [DAAC/journey](https://doc-2-md.vercel.app/#node=daac/journey)
- **Product**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)
- **Description**: Journey analysis — customer path analysis via AI
- **code_dep** → [session](https://doc-2-md.vercel.app/#node=daac/session)

### [DAAC/organization](https://doc-2-md.vercel.app/#node=daac/organization)
- **Product**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)
- **Description**: Org management — workspace, dbt config, Terraform infra
- **code_dep** → [auth](https://doc-2-md.vercel.app/#node=daac/auth)
- **← code_dep** from: [dashboard](https://doc-2-md.vercel.app/#node=daac/dashboard), [dbt](https://doc-2-md.vercel.app/#node=daac/dbt), [infra](https://doc-2-md.vercel.app/#node=daac/infra), [session](https://doc-2-md.vercel.app/#node=daac/session)

### [DAAC/session](https://doc-2-md.vercel.app/#node=daac/session)
- **Product**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)
- **Description**: AI analysis session — conversation state, context management
- **code_dep** → [auth](https://doc-2-md.vercel.app/#node=daac/auth), [organization](https://doc-2-md.vercel.app/#node=daac/organization)
- **← code_dep** from: [agent_v2](https://doc-2-md.vercel.app/#node=daac/agent_v2), [journey](https://doc-2-md.vercel.app/#node=daac/journey)

### [CDH/broadcast](https://doc-2-md.vercel.app/#node=cdh/broadcast)
- **Product**: [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **Description**: CDH broadcast coordination — cross-product message dispatch

### [CDH/channel_entity_comment](https://doc-2-md.vercel.app/#node=cdh/channel_entity_comment)
- **Product**: [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **Description**: Channel entity commenting — AI-powered contact annotations

### [CDH/contact](https://doc-2-md.vercel.app/#node=cdh/contact)
- **Product**: [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **Description**: Unified contact profile — cross-product contact view
- **code_dep** → [unification](https://doc-2-md.vercel.app/#node=cdh/unification)

### [CDH/custom_field](https://doc-2-md.vercel.app/#node=cdh/custom_field)
- **Product**: [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **Description**: Custom contact fields — user-defined attributes

### [CDH/engagement_history](https://doc-2-md.vercel.app/#node=cdh/engagement_history)
- **Product**: [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **Description**: Engagement history — cross-channel interaction tracking

### [CDH/member](https://doc-2-md.vercel.app/#node=cdh/member)
- **Product**: [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **Description**: Member management — import/export, profile enrichment
- **code_dep** → [tag](https://doc-2-md.vercel.app/#node=cdh/tag), [unification](https://doc-2-md.vercel.app/#node=cdh/unification)
- **← code_dep** from: [tag](https://doc-2-md.vercel.app/#node=cdh/tag), [unification](https://doc-2-md.vercel.app/#node=cdh/unification)

### [CDH/richmenu](https://doc-2-md.vercel.app/#node=cdh/richmenu)
- **Product**: [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **Description**: LINE Rich Menu management via CDH

### [CDH/segment](https://doc-2-md.vercel.app/#node=cdh/segment)
- **Product**: [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **Description**: Cross-product audience segmentation via SQL/LLM

### [CDH/tag](https://doc-2-md.vercel.app/#node=cdh/tag)
- **Product**: [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **Description**: Cross-product tag synchronization
- **code_dep** → [member](https://doc-2-md.vercel.app/#node=cdh/member)
- **← code_dep** from: [member](https://doc-2-md.vercel.app/#node=cdh/member), [unification](https://doc-2-md.vercel.app/#node=cdh/unification)

### [CDH/task](https://doc-2-md.vercel.app/#node=cdh/task)
- **Product**: [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **Description**: Background task execution — unification, sync, export jobs

### [CDH/unification](https://doc-2-md.vercel.app/#node=cdh/unification)
- **Product**: [CDH](https://doc-2-md.vercel.app/#node=CDH)
- **Description**: Contact unification graph — merge/split profiles across channels
- **code_dep** → [member](https://doc-2-md.vercel.app/#node=cdh/member), [tag](https://doc-2-md.vercel.app/#node=cdh/tag)
- **← code_dep** from: [contact](https://doc-2-md.vercel.app/#node=cdh/contact), [member](https://doc-2-md.vercel.app/#node=cdh/member)

## 5. Frontend → Backend Mapping

### MAAC Frontend Pages

| Page | Calls Backend Modules |
|------|----------------------|
| [API Token](https://doc-2-md.vercel.app/#node=page/API%20Token) | [openapi](https://doc-2-md.vercel.app/#node=maac/openapi) |
| [Auto Reply](https://doc-2-md.vercel.app/#node=page/Auto%20Reply) | [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp) |
| [Beacon](https://doc-2-md.vercel.app/#node=page/Beacon) | [line](https://doc-2-md.vercel.app/#node=maac/line) |
| [Bindlink](https://doc-2-md.vercel.app/#node=page/Bindlink) | [line](https://doc-2-md.vercel.app/#node=maac/line) |
| [Broadcast](https://doc-2-md.vercel.app/#node=page/Broadcast) | [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [message](https://doc-2-md.vercel.app/#node=maac/message), [sms](https://doc-2-md.vercel.app/#node=maac/sms) |
| [Channel Settings](https://doc-2-md.vercel.app/#node=page/Channel%20Settings) | [channel](https://doc-2-md.vercel.app/#node=maac/channel) |
| [DPM](https://doc-2-md.vercel.app/#node=page/DPM) | [line](https://doc-2-md.vercel.app/#node=maac/line) |
| [Deeplink](https://doc-2-md.vercel.app/#node=page/Deeplink) | [line](https://doc-2-md.vercel.app/#node=maac/line) |
| [Insight (Dashboard)](https://doc-2-md.vercel.app/#node=page/Insight%20%28Dashboard%29) | [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [report](https://doc-2-md.vercel.app/#node=maac/report) |
| [Interaction Games](https://doc-2-md.vercel.app/#node=page/Interaction%20Games) | [line](https://doc-2-md.vercel.app/#node=maac/line), [prize](https://doc-2-md.vercel.app/#node=maac/prize) |
| [Journey](https://doc-2-md.vercel.app/#node=page/Journey) | [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [journey](https://doc-2-md.vercel.app/#node=maac/journey) |
| [Members](https://doc-2-md.vercel.app/#node=page/Members) | [audience](https://doc-2-md.vercel.app/#node=maac/audience), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [tag](https://doc-2-md.vercel.app/#node=maac/tag) |
| [Organization Settings](https://doc-2-md.vercel.app/#node=page/Organization%20Settings) | [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [organization](https://doc-2-md.vercel.app/#node=maac/organization) |
| [Prize](https://doc-2-md.vercel.app/#node=page/Prize) | [prize](https://doc-2-md.vercel.app/#node=maac/prize), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando) |
| [Receipt Register](https://doc-2-md.vercel.app/#node=page/Receipt%20Register) | [receipt](https://doc-2-md.vercel.app/#node=maac/receipt) |
| [Referral V2](https://doc-2-md.vercel.app/#node=page/Referral%20V2) | [referral](https://doc-2-md.vercel.app/#node=maac/referral) |
| [Retarget](https://doc-2-md.vercel.app/#node=page/Retarget) | [audience](https://doc-2-md.vercel.app/#node=maac/audience), [fb](https://doc-2-md.vercel.app/#node=maac/fb) |
| [Rich Menu](https://doc-2-md.vercel.app/#node=page/Rich%20Menu) | [line](https://doc-2-md.vercel.app/#node=maac/line) |
| [SMS Plus](https://doc-2-md.vercel.app/#node=page/SMS%20Plus) | [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus) |
| [Segment](https://doc-2-md.vercel.app/#node=page/Segment) | [audience](https://doc-2-md.vercel.app/#node=maac/audience) |
| [SurveyCake (Form)](https://doc-2-md.vercel.app/#node=page/SurveyCake%20%28Form%29) | [form](https://doc-2-md.vercel.app/#node=maac/form) |
| [Tag Manager](https://doc-2-md.vercel.app/#node=page/Tag%20Manager) | [tag](https://doc-2-md.vercel.app/#node=maac/tag) |
| [Template Library](https://doc-2-md.vercel.app/#node=page/Template%20Library) | [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message) |
| [Tracelink](https://doc-2-md.vercel.app/#node=page/Tracelink) | [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics) |
| [Webhook](https://doc-2-md.vercel.app/#node=page/Webhook) | [webhook](https://doc-2-md.vercel.app/#node=maac/webhook) |
| [Widget](https://doc-2-md.vercel.app/#node=page/Widget) | [line](https://doc-2-md.vercel.app/#node=maac/line) |

### CAAC Frontend Pages

| Page | Calls Backend Modules |
|------|----------------------|
| [AI Settings](https://doc-2-md.vercel.app/#node=caac_page/AI%20Settings) | [aistrategy](https://doc-2-md.vercel.app/#node=caac/aistrategy), [aitask](https://doc-2-md.vercel.app/#node=caac/aitask), [aiusage](https://doc-2-md.vercel.app/#node=caac/aiusage) |
| [Broadcast](https://doc-2-md.vercel.app/#node=caac_page/Broadcast) | [chat](https://doc-2-md.vercel.app/#node=caac/chat) |
| [Chat](https://doc-2-md.vercel.app/#node=caac_page/Chat) | [aitask](https://doc-2-md.vercel.app/#node=caac/aitask), [chat](https://doc-2-md.vercel.app/#node=caac/chat) |
| [Insights](https://doc-2-md.vercel.app/#node=caac_page/Insights) | [dashboard](https://doc-2-md.vercel.app/#node=caac/dashboard) |
| [Quick Template](https://doc-2-md.vercel.app/#node=caac_page/Quick%20Template) | [chat](https://doc-2-md.vercel.app/#node=caac/chat) |
| [Settings](https://doc-2-md.vercel.app/#node=caac_page/Settings) | [auth](https://doc-2-md.vercel.app/#node=caac/auth), [organization](https://doc-2-md.vercel.app/#node=caac/organization) |

## 6. Infrastructure Dependencies

| Infrastructure | Description | Used by Products |
|---------------|-------------|-----------------|
| **[BigQuery](https://doc-2-md.vercel.app/#node=BigQuery)** | Analytics data warehouse, reporting | [MAAC](https://doc-2-md.vercel.app/#node=MAAC), [CAAC](https://doc-2-md.vercel.app/#node=CAAC), [DAAC](https://doc-2-md.vercel.app/#node=DAAC), [CDH](https://doc-2-md.vercel.app/#node=CDH) |
| **[Cloud Run Jobs](https://doc-2-md.vercel.app/#node=Cloud%20Run%20Jobs)** | Task execution for heavy processing | [CDH](https://doc-2-md.vercel.app/#node=CDH) |
| **[Cloud Storage (GCS)](https://doc-2-md.vercel.app/#node=Cloud%20Storage%20%28GCS%29)** | File/image storage | [MAAC](https://doc-2-md.vercel.app/#node=MAAC) |
| **[Cloud Tasks](https://doc-2-md.vercel.app/#node=Cloud%20Tasks)** | Deferred task execution | [MAAC](https://doc-2-md.vercel.app/#node=MAAC) |
| **[Datadog](https://doc-2-md.vercel.app/#node=Datadog)** | APM & distributed tracing | [MAAC](https://doc-2-md.vercel.app/#node=MAAC) |
| **[Elasticsearch](https://doc-2-md.vercel.app/#node=Elasticsearch)** | Message search & conversation indexing | [CAAC](https://doc-2-md.vercel.app/#node=CAAC) |
| **[FCM](https://doc-2-md.vercel.app/#node=FCM)** | Push notifications to mobile/browser | [CAAC](https://doc-2-md.vercel.app/#node=CAAC) |
| **[Firebase / Firestore](https://doc-2-md.vercel.app/#node=Firebase%20/%20Firestore)** | Real-time database for live features | [MAAC](https://doc-2-md.vercel.app/#node=MAAC) |
| **[GCS](https://doc-2-md.vercel.app/#node=GCS)** | File attachment storage | [CAAC](https://doc-2-md.vercel.app/#node=CAAC), [DAAC](https://doc-2-md.vercel.app/#node=DAAC), [CDH](https://doc-2-md.vercel.app/#node=CDH) |
| **[Google Analytics](https://doc-2-md.vercel.app/#node=Google%20Analytics)** | Campaign tracking & UTM parameters | [MAAC](https://doc-2-md.vercel.app/#node=MAAC) |
| **[Infobip](https://doc-2-md.vercel.app/#node=Infobip)** | WhatsApp/Voice gateway | [CAAC](https://doc-2-md.vercel.app/#node=CAAC) |
| **[LINE Messaging API](https://doc-2-md.vercel.app/#node=LINE%20Messaging%20API)** | LINE platform messaging, rich menu, LIFF | [MAAC](https://doc-2-md.vercel.app/#node=MAAC) |
| **[Meta API (FB/IG)](https://doc-2-md.vercel.app/#node=Meta%20API%20%28FB/IG%29)** | Facebook & Instagram messaging API | [MAAC](https://doc-2-md.vercel.app/#node=MAAC) |
| **[OpenAI](https://doc-2-md.vercel.app/#node=OpenAI)** | AI for segment tagging & entity commenting | [CDH](https://doc-2-md.vercel.app/#node=CDH) |
| **[OpenAI / Gemini](https://doc-2-md.vercel.app/#node=OpenAI%20/%20Gemini)** | AI model APIs for agent | [DAAC](https://doc-2-md.vercel.app/#node=DAAC) |
| **[PostgreSQL](https://doc-2-md.vercel.app/#node=PostgreSQL)** | Primary database (Django ORM) | [MAAC](https://doc-2-md.vercel.app/#node=MAAC), [CAAC](https://doc-2-md.vercel.app/#node=CAAC), [DAAC](https://doc-2-md.vercel.app/#node=DAAC), [CDH](https://doc-2-md.vercel.app/#node=CDH) |
| **[PubSub](https://doc-2-md.vercel.app/#node=PubSub)** | Event streaming for cross-service communication | [MAAC](https://doc-2-md.vercel.app/#node=MAAC), [CAAC](https://doc-2-md.vercel.app/#node=CAAC), [CDH](https://doc-2-md.vercel.app/#node=CDH) |
| **[RabbitMQ / Celery](https://doc-2-md.vercel.app/#node=RabbitMQ%20/%20Celery)** | Async task queue for background jobs | [MAAC](https://doc-2-md.vercel.app/#node=MAAC) |
| **[Redis](https://doc-2-md.vercel.app/#node=Redis)** | Cache layer, Celery broker, rate limiting | [MAAC](https://doc-2-md.vercel.app/#node=MAAC), [CAAC](https://doc-2-md.vercel.app/#node=CAAC) |
| **[SendGrid](https://doc-2-md.vercel.app/#node=SendGrid)** | Email delivery service | [MAAC](https://doc-2-md.vercel.app/#node=MAAC) |
| **[Sentry](https://doc-2-md.vercel.app/#node=Sentry)** | Error tracking & monitoring | [MAAC](https://doc-2-md.vercel.app/#node=MAAC) |
| **[Statsig](https://doc-2-md.vercel.app/#node=Statsig)** | Feature flag management | [MAAC](https://doc-2-md.vercel.app/#node=MAAC), [CDH](https://doc-2-md.vercel.app/#node=CDH) |
| **[Terraform](https://doc-2-md.vercel.app/#node=Terraform)** | Infrastructure as code for client provisioning | [DAAC](https://doc-2-md.vercel.app/#node=DAAC) |
| **[WhatsApp Cloud API](https://doc-2-md.vercel.app/#node=WhatsApp%20Cloud%20API)** | WhatsApp Business messaging via Infobip | [MAAC](https://doc-2-md.vercel.app/#node=MAAC) |
| **[dbt](https://doc-2-md.vercel.app/#node=dbt)** | Data transformation pipeline | [DAAC](https://doc-2-md.vercel.app/#node=DAAC) |

## 7. Shared Services

### [Arioso](https://doc-2-md.vercel.app/#node=Arioso)
- SSO authentication service — Google/MS OAuth
- Used by: [MAAC](https://doc-2-md.vercel.app/#node=MAAC), [CAAC](https://doc-2-md.vercel.app/#node=CAAC), [DAAC](https://doc-2-md.vercel.app/#node=DAAC)

### [Harmony](https://doc-2-md.vercel.app/#node=Harmony)
- Partner API & Google Ads integration
- Used by: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Interlude](https://doc-2-md.vercel.app/#node=Interlude)
- Admin center — billing, subscription, org provisioning
- Used by: [MAAC](https://doc-2-md.vercel.app/#node=MAAC), [CAAC](https://doc-2-md.vercel.app/#node=CAAC), [DAAC](https://doc-2-md.vercel.app/#node=DAAC)

### [MDS](https://doc-2-md.vercel.app/#node=MDS)
- Message Delivery Service
- Used by: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Monophony](https://doc-2-md.vercel.app/#node=Monophony)
- URL shortener service (maac.io)
- Used by: [MAAC](https://doc-2-md.vercel.app/#node=MAAC), [CAAC](https://doc-2-md.vercel.app/#node=CAAC)

### [Sforzando](https://doc-2-md.vercel.app/#node=Sforzando)
- Prize fulfillment & reward distribution
- Used by: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

## 8. Cross-Product Data Flow

### API Calls

```
MAAC (rubato (Python/Django) + Grazioso (React/TS)) ──[API]──→ CAAC (cantata (Go) + Zeffiroso (React/TS))  (CAAC_CANTATA_URL (REST API))
MAAC (rubato (Python/Django) + Grazioso (React/TS)) ──[API]──→ DAAC (bebop (Python/FastAPI))  (DAAC_API_URL (REST API))
CAAC (cantata (Go) + Zeffiroso (React/TS)) ──[API]──→ MAAC (rubato (Python/Django) + Grazioso (React/TS))  (MAAC_URL (REST API))
CAAC (cantata (Go) + Zeffiroso (React/TS)) ──[API]──→ CDH (polyrhythmic (Python+Go))  (CDH_INTERNAL_URL (Unification V2))
page/Insight (Dashboard) ──[API]──→ maac/report  (calls API)
page/Insight (Dashboard) ──[API]──→ maac/google_analytics  (calls API)
page/Members ──[API]──→ maac/audience  (calls API)
page/Members ──[API]──→ maac/cdp  (calls API)
page/Members ──[API]──→ maac/tag  (calls API)
page/Segment ──[API]──→ maac/audience  (calls API)
page/Tag Manager ──[API]──→ maac/tag  (calls API)
page/Broadcast ──[API]──→ maac/broadcast  (calls API)
page/Broadcast ──[API]──→ maac/message  (calls API)
page/Broadcast ──[API]──→ maac/sms  (calls API)
page/Auto Reply ──[API]──→ maac/auto_reply  (calls API)
page/Auto Reply ──[API]──→ maac/fb  (calls API)
page/Auto Reply ──[API]──→ maac/whatsapp  (calls API)
page/Template Library ──[API]──→ maac/message  (calls API)
page/Template Library ──[API]──→ maac/line  (calls API)
page/Rich Menu ──[API]──→ maac/line  (calls API)
page/Journey ──[API]──→ maac/journey  (calls API)
page/Journey ──[API]──→ maac/email_channel  (calls API)
page/Deeplink ──[API]──→ maac/line  (calls API)
page/Tracelink ──[API]──→ maac/google_analytics  (calls API)
page/Prize ──[API]──→ maac/prize  (calls API)
page/Prize ──[API]──→ maac/sforzando  (calls API)
page/Retarget ──[API]──→ maac/audience  (calls API)
page/Retarget ──[API]──→ maac/fb  (calls API)
page/Referral V2 ──[API]──→ maac/referral  (calls API)
page/Receipt Register ──[API]──→ maac/receipt  (calls API)
page/Webhook ──[API]──→ maac/webhook  (calls API)
page/SurveyCake (Form) ──[API]──→ maac/form  (calls API)
page/API Token ──[API]──→ maac/openapi  (calls API)
page/Widget ──[API]──→ maac/line  (calls API)
page/SMS Plus ──[API]──→ maac/sms_plus  (calls API)
page/SMS Plus ──[API]──→ maac/sms  (calls API)
page/Organization Settings ──[API]──→ maac/organization  (calls API)
page/Organization Settings ──[API]──→ maac/accounts  (calls API)
page/Channel Settings ──[API]──→ maac/channel  (calls API)
page/DPM ──[API]──→ maac/line  (calls API)
page/Beacon ──[API]──→ maac/line  (calls API)
page/Bindlink ──[API]──→ maac/line  (calls API)
page/Interaction Games ──[API]──→ maac/prize  (calls API)
page/Interaction Games ──[API]──→ maac/line  (calls API)
caac_page/Chat ──[API]──→ caac/chat  (calls API)
caac_page/Chat ──[API]──→ caac/aitask  (calls API)
caac_page/Broadcast ──[API]──→ caac/chat  (calls API)
caac_page/Insights ──[API]──→ caac/dashboard  (calls API)
caac_page/Quick Template ──[API]──→ caac/chat  (calls API)
caac_page/AI Settings ──[API]──→ caac/aistrategy  (calls API)
caac_page/AI Settings ──[API]──→ caac/aitask  (calls API)
caac_page/AI Settings ──[API]──→ caac/aiusage  (calls API)
caac_page/Settings ──[API]──→ caac/organization  (calls API)
caac_page/Settings ──[API]──→ caac/auth  (calls API)
```

### Data Sync

```
CDH ──[SYNC]──→ MAAC  (RUBATO_HOST + RUBATO_DB_DSN)
CDH ──[SYNC]──→ CAAC  (CANTATA_HOST + CANTATA_DB_DSN)
DAAC ──[SYNC]──→ MAAC  (MAAC_GCP_PROJECT_ID (BigQuery))
DAAC ──[SYNC]──→ CAAC  (CAAC_GCP_PROJECT_ID (BigQuery))
```

## 9. Impact Analysis Guide

### High-Impact Modules (most imported by others)

| Module | Product | Imported by N | code_dep | model_ref | const_ref | task_dep | api_client | Risk |
|--------|---------|---------------|----------|-----------|-----------|----------|------------|------|
| [line](https://doc-2-md.vercel.app/#node=maac/line) | MAAC | 115 | 37 | 28 | 30 | 12 | 8 | 🔴 Critical |
| [organization](https://doc-2-md.vercel.app/#node=maac/organization) | MAAC | 47 | 30 | 9 | 6 | 1 | 1 | 🔴 Critical |
| [tag](https://doc-2-md.vercel.app/#node=maac/tag) | MAAC | 47 | 7 | 9 | 14 | 16 | 1 | 🔴 Critical |
| [system](https://doc-2-md.vercel.app/#node=maac/system) | MAAC | 40 | 12 | 4 | 23 | 1 | 0 | 🔴 Critical |
| [accounts](https://doc-2-md.vercel.app/#node=maac/accounts) | MAAC | 39 | 11 | 24 | 3 | 0 | 1 | 🔴 Critical |
| [openapi](https://doc-2-md.vercel.app/#node=maac/openapi) | MAAC | 31 | 12 | 7 | 7 | 2 | 3 | 🔴 Critical |
| [channel](https://doc-2-md.vercel.app/#node=maac/channel) | MAAC | 28 | 11 | 1 | 16 | 0 | 0 | 🔴 Critical |
| [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc) | MAAC | 26 | 26 | 0 | 0 | 0 | 0 | 🔴 Critical |
| [audience](https://doc-2-md.vercel.app/#node=maac/audience) | MAAC | 26 | 10 | 6 | 7 | 3 | 0 | 🔴 Critical |
| [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics) | MAAC | 23 | 11 | 7 | 5 | 0 | 0 | 🔴 Critical |
| [journey](https://doc-2-md.vercel.app/#node=maac/journey) | MAAC | 23 | 9 | 2 | 6 | 6 | 0 | 🔴 Critical |
| [notification](https://doc-2-md.vercel.app/#node=maac/notification) | MAAC | 21 | 4 | 3 | 9 | 5 | 0 | 🔴 Critical |
| [webhook](https://doc-2-md.vercel.app/#node=maac/webhook) | MAAC | 21 | 5 | 2 | 7 | 7 | 0 | 🔴 Critical |
| [sms](https://doc-2-md.vercel.app/#node=maac/sms) | MAAC | 20 | 9 | 3 | 6 | 1 | 1 | 🔴 Critical |
| [interlude](https://doc-2-md.vercel.app/#node=maac/interlude) | MAAC | 18 | 14 | 0 | 4 | 0 | 0 | 🔴 Critical |
| [prize](https://doc-2-md.vercel.app/#node=maac/prize) | MAAC | 17 | 7 | 5 | 2 | 2 | 1 | 🔴 Critical |
| [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply) | MAAC | 11 | 6 | 0 | 5 | 0 | 0 | 🟡 High |
| [message](https://doc-2-md.vercel.app/#node=maac/message) | MAAC | 11 | 7 | 0 | 4 | 0 | 0 | 🟡 High |
| [cdp](https://doc-2-md.vercel.app/#node=maac/cdp) | MAAC | 10 | 4 | 0 | 6 | 0 | 0 | 🟡 High |
| [payment](https://doc-2-md.vercel.app/#node=maac/payment) | MAAC | 10 | 9 | 1 | 0 | 0 | 0 | 🟡 High |

### Hub Modules (most outgoing deps)

| Module | Product | Depends on N | Coupling |
|--------|---------|-------------|----------|
| [line](https://doc-2-md.vercel.app/#node=maac/line) | MAAC | 83 | 🔴 High |
| [openapi](https://doc-2-md.vercel.app/#node=maac/openapi) | MAAC | 45 | 🔴 High |
| [internal](https://doc-2-md.vercel.app/#node=maac/internal) | MAAC | 31 | 🔴 High |
| [journey](https://doc-2-md.vercel.app/#node=maac/journey) | MAAC | 27 | 🔴 High |
| [organization](https://doc-2-md.vercel.app/#node=maac/organization) | MAAC | 25 | 🔴 High |
| [prize](https://doc-2-md.vercel.app/#node=maac/prize) | MAAC | 24 | 🔴 High |
| [sms](https://doc-2-md.vercel.app/#node=maac/sms) | MAAC | 24 | 🔴 High |
| [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app) | MAAC | 20 | 🔴 High |
| [audience](https://doc-2-md.vercel.app/#node=maac/audience) | MAAC | 19 | 🔴 High |
| [system](https://doc-2-md.vercel.app/#node=maac/system) | MAAC | 19 | 🔴 High |
| [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test) | MAAC | 18 | 🔴 High |
| [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply) | MAAC | 16 | 🔴 High |
| [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast) | MAAC | 16 | 🔴 High |
| [accounts](https://doc-2-md.vercel.app/#node=maac/accounts) | MAAC | 15 | 🔴 High |
| [receipt](https://doc-2-md.vercel.app/#node=maac/receipt) | MAAC | 15 | 🔴 High |

## 10. Change Impact Chains

Format: `If you change X → these modules are directly affected`

### Changing [line](https://doc-2-md.vercel.app/#node=maac/line) (MAAC)
Directly affects 115 modules:
- via `code_dep`: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [cyberbiz](https://doc-2-md.vercel.app/#node=maac/cyberbiz), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [form](https://doc-2-md.vercel.app/#node=maac/form), [integration](https://doc-2-md.vercel.app/#node=maac/integration), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [message](https://doc-2-md.vercel.app/#node=maac/message), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [report](https://doc-2-md.vercel.app/#node=maac/report), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [verification](https://doc-2-md.vercel.app/#node=maac/verification), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- via `model_ref`: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [firestore](https://doc-2-md.vercel.app/#node=maac/firestore), [form](https://doc-2-md.vercel.app/#node=maac/form), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [message](https://doc-2-md.vercel.app/#node=maac/message), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [report](https://doc-2-md.vercel.app/#node=maac/report), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook), [workflow](https://doc-2-md.vercel.app/#node=maac/workflow)
- via `const_ref`: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [form](https://doc-2-md.vercel.app/#node=maac/form), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [report](https://doc-2-md.vercel.app/#node=maac/report), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- via `task_dep`: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [form](https://doc-2-md.vercel.app/#node=maac/form), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- via `api_client`: [form](https://doc-2-md.vercel.app/#node=maac/form), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [sms](https://doc-2-md.vercel.app/#node=maac/sms)

### Changing [organization](https://doc-2-md.vercel.app/#node=maac/organization) (MAAC)
Directly affects 47 modules:
- via `code_dep`: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [payment](https://doc-2-md.vercel.app/#node=maac/payment), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- via `model_ref`: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [line](https://doc-2-md.vercel.app/#node=maac/line), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- via `const_ref`: [ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi)
- via `task_dep`: [internal](https://doc-2-md.vercel.app/#node=maac/internal)
- via `api_client`: [line](https://doc-2-md.vercel.app/#node=maac/line)

### Changing [tag](https://doc-2-md.vercel.app/#node=maac/tag) (MAAC)
Directly affects 47 modules:
- via `code_dep`: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- via `model_ref`: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [report](https://doc-2-md.vercel.app/#node=maac/report), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [system](https://doc-2-md.vercel.app/#node=maac/system)
- via `const_ref`: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [form](https://doc-2-md.vercel.app/#node=maac/form), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [system](https://doc-2-md.vercel.app/#node=maac/system)
- via `task_dep`: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [form](https://doc-2-md.vercel.app/#node=maac/form), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [system](https://doc-2-md.vercel.app/#node=maac/system), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- via `api_client`: [form](https://doc-2-md.vercel.app/#node=maac/form)

### Changing [system](https://doc-2-md.vercel.app/#node=maac/system) (MAAC)
Directly affects 40 modules:
- via `code_dep`: [ai_generation](https://doc-2-md.vercel.app/#node=maac/ai_generation), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- via `model_ref`: [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline)
- via `const_ref`: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [report](https://doc-2-md.vercel.app/#node=maac/report), [shortener](https://doc-2-md.vercel.app/#node=maac/shortener), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [tag](https://doc-2-md.vercel.app/#node=maac/tag), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp), [workflow](https://doc-2-md.vercel.app/#node=maac/workflow)
- via `task_dep`: [line](https://doc-2-md.vercel.app/#node=maac/line)

### Changing [accounts](https://doc-2-md.vercel.app/#node=maac/accounts) (MAAC)
Directly affects 39 modules:
- via `code_dep`: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [notification](https://doc-2-md.vercel.app/#node=maac/notification), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [system](https://doc-2-md.vercel.app/#node=maac/system)
- via `model_ref`: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [campaign](https://doc-2-md.vercel.app/#node=maac/campaign), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [cyberbiz](https://doc-2-md.vercel.app/#node=maac/cyberbiz), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics), [integration](https://doc-2-md.vercel.app/#node=maac/integration), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [referral](https://doc-2-md.vercel.app/#node=maac/referral), [sforzando](https://doc-2-md.vercel.app/#node=maac/sforzando), [shopify](https://doc-2-md.vercel.app/#node=maac/shopify), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- via `const_ref`: [extension](https://doc-2-md.vercel.app/#node=maac/extension), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test)
- via `api_client`: [internal](https://doc-2-md.vercel.app/#node=maac/internal)

### Changing [openapi](https://doc-2-md.vercel.app/#node=maac/openapi) (MAAC)
Directly affects 31 modules:
- via `code_dep`: [channel](https://doc-2-md.vercel.app/#node=maac/channel), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- via `model_ref`: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [report](https://doc-2-md.vercel.app/#node=maac/report), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [webhook](https://doc-2-md.vercel.app/#node=maac/webhook)
- via `const_ref`: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- via `task_dep`: [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app)
- via `api_client`: [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [shopline](https://doc-2-md.vercel.app/#node=maac/shopline), [sms](https://doc-2-md.vercel.app/#node=maac/sms)

### Changing [channel](https://doc-2-md.vercel.app/#node=maac/channel) (MAAC)
Directly affects 28 modules:
- via `code_dep`: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)
- via `model_ref`: [journey](https://doc-2-md.vercel.app/#node=maac/journey)
- via `const_ref`: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [campaign](https://doc-2-md.vercel.app/#node=maac/campaign), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [pubsub_pull](https://doc-2-md.vercel.app/#node=maac/pubsub_pull), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [wccs](https://doc-2-md.vercel.app/#node=maac/wccs), [whatsapp](https://doc-2-md.vercel.app/#node=maac/whatsapp)

### Changing [api_doc](https://doc-2-md.vercel.app/#node=maac/api_doc) (MAAC)
Directly affects 26 modules:
- via `code_dep`: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [audience](https://doc-2-md.vercel.app/#node=maac/audience), [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [caac](https://doc-2-md.vercel.app/#node=maac/caac), [campaign](https://doc-2-md.vercel.app/#node=maac/campaign), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [channel](https://doc-2-md.vercel.app/#node=maac/channel), [email_channel](https://doc-2-md.vercel.app/#node=maac/email_channel), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [form](https://doc-2-md.vercel.app/#node=maac/form), [integration](https://doc-2-md.vercel.app/#node=maac/integration), [interlude](https://doc-2-md.vercel.app/#node=maac/interlude), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [receipt](https://doc-2-md.vercel.app/#node=maac/receipt), [smoke_test](https://doc-2-md.vercel.app/#node=maac/smoke_test), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [sms_plus](https://doc-2-md.vercel.app/#node=maac/sms_plus), [system](https://doc-2-md.vercel.app/#node=maac/system), [tag](https://doc-2-md.vercel.app/#node=maac/tag)

### Changing [audience](https://doc-2-md.vercel.app/#node=maac/audience) (MAAC)
Directly affects 26 modules:
- via `code_dep`: [accounts](https://doc-2-md.vercel.app/#node=maac/accounts), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [cdp](https://doc-2-md.vercel.app/#node=maac/cdp), [firestore](https://doc-2-md.vercel.app/#node=maac/firestore), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [tag](https://doc-2-md.vercel.app/#node=maac/tag)
- via `model_ref`: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [sms](https://doc-2-md.vercel.app/#node=maac/sms), [system](https://doc-2-md.vercel.app/#node=maac/system)
- via `const_ref`: [bigquery](https://doc-2-md.vercel.app/#node=maac/bigquery), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- via `task_dep`: [internal](https://doc-2-md.vercel.app/#node=maac/internal), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi)

### Changing [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics) (MAAC)
Directly affects 23 modules:
- via `code_dep`: [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply), [broadcast](https://doc-2-md.vercel.app/#node=maac/broadcast), [extension](https://doc-2-md.vercel.app/#node=maac/extension), [fb](https://doc-2-md.vercel.app/#node=maac/fb), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [message](https://doc-2-md.vercel.app/#node=maac/message), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [organization](https://doc-2-md.vercel.app/#node=maac/organization), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [sms](https://doc-2-md.vercel.app/#node=maac/sms)
- via `model_ref`: [audience](https://doc-2-md.vercel.app/#node=maac/audience), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize), [report](https://doc-2-md.vercel.app/#node=maac/report), [system](https://doc-2-md.vercel.app/#node=maac/system), [workflow](https://doc-2-md.vercel.app/#node=maac/workflow)
- via `const_ref`: [extension](https://doc-2-md.vercel.app/#node=maac/extension), [journey](https://doc-2-md.vercel.app/#node=maac/journey), [line](https://doc-2-md.vercel.app/#node=maac/line), [openapi](https://doc-2-md.vercel.app/#node=maac/openapi), [prize](https://doc-2-md.vercel.app/#node=maac/prize)

## 11. Product Dependency Matrix

Summary of how each product connects to others:

| From \ To | MAAC | CAAC | DAAC | CDH |
|-----------|------|------|------|-----|
| **MAAC** | — | api_call: CAAC_CANTATA_URL (REST API); ←api_call: MAAC_URL (REST API) | api_call: DAAC_API_URL (REST API); ←data_sync: MAAC_GCP_PROJECT_ID (BigQuery) | ←data_sync: RUBATO_HOST + RUBATO_DB_DSN |
| **CAAC** | api_call: MAAC_URL (REST API); ←api_call: CAAC_CANTATA_URL (REST API) | — | ←data_sync: CAAC_GCP_PROJECT_ID (BigQuery) | api_call: CDH_INTERNAL_URL (Unification V2); ←data_sync: CANTATA_HOST + CANTATA_DB_DSN |
| **DAAC** | data_sync: MAAC_GCP_PROJECT_ID (BigQuery); ←api_call: DAAC_API_URL (REST API) | data_sync: CAAC_GCP_PROJECT_ID (BigQuery) | — | — |
| **CDH** | data_sync: RUBATO_HOST + RUBATO_DB_DSN | data_sync: CANTATA_HOST + CANTATA_DB_DSN; ←api_call: CDH_INTERNAL_URL (Unification V2) | — | — |

## 12. Module-to-Infrastructure Mapping

Which modules depend on which infrastructure components:

### [BigQuery](https://doc-2-md.vercel.app/#node=BigQuery)
- Analytics data warehouse, reporting
- **Depended on by**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC), [CDH](https://doc-2-md.vercel.app/#node=CDH), [DAAC](https://doc-2-md.vercel.app/#node=DAAC), [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Cloud Run Jobs](https://doc-2-md.vercel.app/#node=Cloud%20Run%20Jobs)
- Task execution for heavy processing
- **Depended on by**: [CDH](https://doc-2-md.vercel.app/#node=CDH)

### [Cloud Storage (GCS)](https://doc-2-md.vercel.app/#node=Cloud%20Storage%20%28GCS%29)
- File/image storage
- **Depended on by**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Cloud Tasks](https://doc-2-md.vercel.app/#node=Cloud%20Tasks)
- Deferred task execution
- **Depended on by**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Datadog](https://doc-2-md.vercel.app/#node=Datadog)
- APM & distributed tracing
- **Depended on by**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Elasticsearch](https://doc-2-md.vercel.app/#node=Elasticsearch)
- Message search & conversation indexing
- **Depended on by**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)

### [FCM](https://doc-2-md.vercel.app/#node=FCM)
- Push notifications to mobile/browser
- **Depended on by**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)

### [Firebase / Firestore](https://doc-2-md.vercel.app/#node=Firebase%20/%20Firestore)
- Real-time database for live features
- **Depended on by**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [GCS](https://doc-2-md.vercel.app/#node=GCS)
- File attachment storage
- **Depended on by**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC), [CDH](https://doc-2-md.vercel.app/#node=CDH), [DAAC](https://doc-2-md.vercel.app/#node=DAAC)

### [Google Analytics](https://doc-2-md.vercel.app/#node=Google%20Analytics)
- Campaign tracking & UTM parameters
- **Depended on by**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Infobip](https://doc-2-md.vercel.app/#node=Infobip)
- WhatsApp/Voice gateway
- **Depended on by**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC)

### [LINE Messaging API](https://doc-2-md.vercel.app/#node=LINE%20Messaging%20API)
- LINE platform messaging, rich menu, LIFF
- **Depended on by**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Meta API (FB/IG)](https://doc-2-md.vercel.app/#node=Meta%20API%20%28FB/IG%29)
- Facebook & Instagram messaging API
- **Depended on by**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [OpenAI](https://doc-2-md.vercel.app/#node=OpenAI)
- AI for segment tagging & entity commenting
- **Depended on by**: [CDH](https://doc-2-md.vercel.app/#node=CDH)

### [OpenAI / Gemini](https://doc-2-md.vercel.app/#node=OpenAI%20/%20Gemini)
- AI model APIs for agent
- **Depended on by**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)

### [PostgreSQL](https://doc-2-md.vercel.app/#node=PostgreSQL)
- Primary database (Django ORM)
- **Depended on by**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC), [CDH](https://doc-2-md.vercel.app/#node=CDH), [DAAC](https://doc-2-md.vercel.app/#node=DAAC), [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [PubSub](https://doc-2-md.vercel.app/#node=PubSub)
- Event streaming for cross-service communication
- **Depended on by**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC), [CDH](https://doc-2-md.vercel.app/#node=CDH), [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [RabbitMQ / Celery](https://doc-2-md.vercel.app/#node=RabbitMQ%20/%20Celery)
- Async task queue for background jobs
- **Depended on by**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Redis](https://doc-2-md.vercel.app/#node=Redis)
- Cache layer, Celery broker, rate limiting
- **Depended on by**: [CAAC](https://doc-2-md.vercel.app/#node=CAAC), [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [SendGrid](https://doc-2-md.vercel.app/#node=SendGrid)
- Email delivery service
- **Depended on by**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Sentry](https://doc-2-md.vercel.app/#node=Sentry)
- Error tracking & monitoring
- **Depended on by**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Statsig](https://doc-2-md.vercel.app/#node=Statsig)
- Feature flag management
- **Depended on by**: [CDH](https://doc-2-md.vercel.app/#node=CDH), [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [Terraform](https://doc-2-md.vercel.app/#node=Terraform)
- Infrastructure as code for client provisioning
- **Depended on by**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)

### [WhatsApp Cloud API](https://doc-2-md.vercel.app/#node=WhatsApp%20Cloud%20API)
- WhatsApp Business messaging via Infobip
- **Depended on by**: [MAAC](https://doc-2-md.vercel.app/#node=MAAC)

### [dbt](https://doc-2-md.vercel.app/#node=dbt)
- Data transformation pipeline
- **Depended on by**: [DAAC](https://doc-2-md.vercel.app/#node=DAAC)

## 13. Semantic Dependency Hotspots

Modules with the most fine-grained semantic dependencies (model_ref + const_ref + task_dep + api_client):

| Module | Product | Total Semantic Edges | model_ref | const_ref | task_dep | api_client |
|--------|---------|---------------------|-----------|-----------|----------|------------|
| [line](https://doc-2-md.vercel.app/#node=maac/line) | MAAC | 129 | 47 | 49 | 22 | 11 |
| [tag](https://doc-2-md.vercel.app/#node=maac/tag) | MAAC | 48 | 12 | 17 | 18 | 1 |
| [openapi](https://doc-2-md.vercel.app/#node=maac/openapi) | MAAC | 44 | 12 | 20 | 7 | 5 |
| [system](https://doc-2-md.vercel.app/#node=maac/system) | MAAC | 40 | 10 | 27 | 3 | 0 |
| [accounts](https://doc-2-md.vercel.app/#node=maac/accounts) | MAAC | 35 | 26 | 6 | 2 | 1 |
| [audience](https://doc-2-md.vercel.app/#node=maac/audience) | MAAC | 27 | 12 | 12 | 3 | 0 |
| [journey](https://doc-2-md.vercel.app/#node=maac/journey) | MAAC | 27 | 7 | 13 | 7 | 0 |
| [organization](https://doc-2-md.vercel.app/#node=maac/organization) | MAAC | 27 | 11 | 13 | 2 | 1 |
| [prize](https://doc-2-md.vercel.app/#node=maac/prize) | MAAC | 26 | 10 | 8 | 6 | 2 |
| [channel](https://doc-2-md.vercel.app/#node=maac/channel) | MAAC | 25 | 4 | 20 | 1 | 0 |
| [sms](https://doc-2-md.vercel.app/#node=maac/sms) | MAAC | 24 | 7 | 13 | 1 | 3 |
| [webhook](https://doc-2-md.vercel.app/#node=maac/webhook) | MAAC | 21 | 6 | 8 | 7 | 0 |
| [google_analytics](https://doc-2-md.vercel.app/#node=maac/google_analytics) | MAAC | 17 | 11 | 6 | 0 | 0 |
| [notification](https://doc-2-md.vercel.app/#node=maac/notification) | MAAC | 17 | 3 | 9 | 5 | 0 |
| [internal](https://doc-2-md.vercel.app/#node=maac/internal) | MAAC | 16 | 5 | 6 | 3 | 2 |
| [nine_one_app](https://doc-2-md.vercel.app/#node=maac/nine_one_app) | MAAC | 14 | 5 | 3 | 5 | 1 |
| [referral](https://doc-2-md.vercel.app/#node=maac/referral) | MAAC | 14 | 6 | 3 | 3 | 2 |
| [auto_reply](https://doc-2-md.vercel.app/#node=maac/auto_reply) | MAAC | 12 | 2 | 9 | 1 | 0 |
| [cdp](https://doc-2-md.vercel.app/#node=maac/cdp) | MAAC | 11 | 1 | 8 | 2 | 0 |
| [report](https://doc-2-md.vercel.app/#node=maac/report) | MAAC | 11 | 9 | 2 | 0 | 0 |

---
*End of Code Architecture Knowledge Graph v7*