# Crescendo Lab — Code Architecture Knowledge Graph v7 (LLM-Optimized)

> Auto-generated from deep codebase analysis on 2026-03-03 16:12
> Repos: rubato (MAAC BE), Grazioso (MAAC FE), cantata (CAAC BE), Zeffiroso (CAAC FE), bebop (DAAC), polyrhythmic (CDH)
> Nodes: 155 | Edges: 915
> Edge breakdown: code_dep=319, const_ref=166, model_ref=125, hierarchy=123, task_dep=59, api_call=54, infra_dep=37, api_client=17, service_dep=11, data_sync=4
> Purpose: Verified architecture map with semantic dependency types — for LLM impact analysis, attribution & root-cause tracing.

---

## 1. Product Suite

### MAAC
- **MAAC**: Marketing Automation & Analytics Cloud
- Tech: MAAC — Marketing Automation & Analytics Cloud
Tech: Django 3.2 + React 19 (TypeScript)
Repos: {'backend': 'rubato (Python/Django)', 'frontend': 'Grazioso (React/TS)'}
- Repos: rubato (Python/Django) + Grazioso (React/TS)

- Backend modules: 54
- Frontend pages: 26

**Cross-product connections:**
- → CAAC: CAAC_CANTATA_URL (REST API)
- → DAAC: DAAC_API_URL (REST API)
- ← CDH: RUBATO_HOST + RUBATO_DB_DSN
- ← CAAC: MAAC_URL (REST API)
- ← DAAC: MAAC_GCP_PROJECT_ID (BigQuery)

### CAAC
- **CAAC**: Conversation Automation & Analytics Cloud
- Tech: CAAC — Conversation Automation & Analytics Cloud
Tech: Go (Cantata) + React (Zeffiroso/TS)
Repos: {'backend': 'cantata (Go)', 'frontend': 'Zeffiroso (React/TS)'}
- Repos: cantata (Go) + Zeffiroso (React/TS)

- Backend modules: 13
- Frontend pages: 6

**Cross-product connections:**
- → MAAC: MAAC_URL (REST API)
- → CDH: CDH_INTERNAL_URL (Unification V2)
- ← MAAC: CAAC_CANTATA_URL (REST API)
- ← CDH: CANTATA_HOST + CANTATA_DB_DSN
- ← DAAC: CAAC_GCP_PROJECT_ID (BigQuery)

### DAAC
- **DAAC**: Data Automation & Analytics Cloud
- Tech: DAAC — Data Automation & Analytics Cloud
Tech: Python (FastAPI) + React + AI Agent
Repos: {'backend': 'bebop (Python/FastAPI)', 'frontend': 'bebop/frontend (React/TS)'}
- Repos: bebop (Python/FastAPI)

- Backend modules: 9
- Frontend pages: 0

**Cross-product connections:**
- → MAAC: MAAC_GCP_PROJECT_ID (BigQuery)
- → CAAC: CAAC_GCP_PROJECT_ID (BigQuery)
- ← MAAC: DAAC_API_URL (REST API)

### CDH
- **CDH**: Customer Data Hub — Unified Contact Profile
- Tech: CDH — Customer Data Hub — Unified Contact Profile
Tech: Python + Go (Polyrhythmic)
Repos: {'backend': 'polyrhythmic (Python+Go)', 'frontend': 'N/A (API-only)'}
- Repos: polyrhythmic (Python+Go)

- Backend modules: 11
- Frontend pages: 0

**Cross-product connections:**
- → MAAC: RUBATO_HOST + RUBATO_DB_DSN
- → CAAC: CANTATA_HOST + CANTATA_DB_DSN
- ← CAAC: CDH_INTERNAL_URL (Unification V2)

## 2. Module Architecture

### MAAC Modules (54 total)

| Module | Description | code_dep | model_ref | const_ref | task_dep | api_client |
|--------|-------------|----------|-----------|-----------|----------|------------|
| **accounts** | User authentication, SSO, 2FA, session management | 8 | 2 | 3 | 2 |  |
| **ai_generation** | AI content generation — copywriting, image generation | 2 |  | 1 |  |  |
| **api_doc** | MAAC module: api_doc |  |  |  |  |  |
| **async_wrapper** | MAAC module: async_wrapper |  |  |  |  |  |
| **audience** | Contact management, segments, filters, ad platform audiences | 8 | 6 | 5 |  |  |
| **auto_reply** | Keyword auto-reply across LINE/FB/WhatsApp channels | 9 | 2 | 4 | 1 |  |
| **bigquery** | BigQuery data pipeline integration | 1 | 1 | 3 |  |  |
| **broadcast** | Push messaging (LINE/SMS/WhatsApp), scheduling, A/B test | 10 | 1 | 5 |  |  |
| **caac** | CAAC integration bridge — connects Rubato to Cantata | 4 | 2 | 1 |  |  |
| **campaign** | Campaign orchestration — multi-channel campaign management | 2 | 2 | 2 |  |  |
| **cdp** | Customer Data Platform — profile unification, data sync | 6 | 1 | 2 | 2 |  |
| **channel** | Multi-channel management (LINE/FB/IG/WhatsApp/Email/SMS) | 5 | 3 | 4 | 1 |  |
| **coupon** | MAAC module: coupon |  |  |  |  |  |
| **cyberbiz** | Cyberbiz e-commerce integration | 1 | 1 |  |  |  |
| **email_channel** | Email campaign delivery via SendGrid, bounce handling | 8 |  | 4 | 1 |  |
| **extension** | MAAC extension plugins — custom action nodes | 6 | 1 | 6 |  |  |
| **fb** | Facebook/Instagram messaging, comment auto-reply | 7 | 1 | 4 | 1 |  |
| **firestore** | MAAC module: firestore | 1 | 1 |  |  |  |
| **form** | SurveyCake form integration, response tracking | 2 | 1 | 3 | 3 | 2 |
| **google_analytics** | GA4/UTM tracking integration for campaigns | 1 | 4 | 1 |  |  |
| **integration** | MAAC module: integration | 2 | 1 |  |  |  |
| **interlude** | MAAC module: interlude | 4 | 1 |  |  |  |
| **internal** | Internal admin tools — data migration, debugging | 15 | 5 | 6 | 3 | 2 |
| **invoice** | Invoice management — receipt/reward redemption |  |  |  |  |  |
| **journey** | Customer journey automation (triggers, actions, conditions) | 14 | 5 | 7 | 1 |  |
| **line** | Core LINE integration — messaging, rich menu, Flex, LIFF | 32 | 19 | 19 | 10 | 3 |
| **message** | Message rendering engine — builds LINE/FB/SMS/Email messages | 4 | 1 | 3 |  |  |
| **nine_one_app** | 91App e-commerce integration | 8 | 4 | 3 | 4 | 1 |
| **notification** | In-app notification system for admin users | 1 |  |  |  |  |
| **openapi** | Public OpenAPI — external developer API endpoints | 20 | 5 | 13 | 5 | 2 |
| **organization** | Org/tenant management, billing, feature control, RBAC | 15 | 2 | 7 | 1 |  |
| **payment** | Payment & billing — subscription, invoice management | 4 | 2 | 2 | 1 |  |
| **prize** | Prize/reward management, lottery, coupon distribution | 8 | 5 | 6 | 4 | 1 |
| **pubsub** | MAAC module: pubsub |  |  |  |  |  |
| **pubsub_pull** | PubSub consumer — event processing workers | 4 |  | 5 | 2 |  |
| **receipt** | Receipt registration campaign for loyalty programs | 8 | 2 | 2 | 2 | 1 |
| **referral** | Rapid Referral — MGM campaigns, invitation tracking | 4 | 4 | 3 | 3 | 1 |
| **report** | Analytics & reporting — campaign performance, member stats | 3 | 6 | 2 |  |  |
| **sforzando** | Prize fulfillment partner integration | 4 | 4 | 1 | 2 | 1 |
| **shopify** | Shopify e-commerce integration | 1 | 3 | 1 | 1 |  |
| **shopline** | Shopline e-commerce integration | 6 | 3 | 2 | 3 | 1 |
| **shortener** | MAAC module: shortener |  |  | 1 |  |  |
| **smoke_test** | Automated smoke test — system health validation | 7 | 5 | 6 |  |  |
| **sms** | SMS delivery — domestic/international SMS campaigns | 11 | 4 | 7 |  | 2 |
| **sms_plus** | SMS Plus — enhanced SMS features, message records | 9 |  | 3 |  |  |
| **staticfiles** | MAAC module: staticfiles |  |  |  |  |  |
| **stress_test** | MAAC module: stress_test |  |  |  |  |  |
| **system** | System-wide utilities — campaign tracking, feature flags | 7 | 6 | 4 | 2 |  |
| **tag** | Tag management — contact tagging, auto-tagging rules | 6 | 3 | 3 | 2 |  |
| **verification** | MAAC module: verification | 1 |  |  |  |  |
| **wccs** | MAAC module: wccs | 4 |  | 4 | 1 |  |
| **webhook** | Webhook delivery — event push to external systems | 4 | 4 | 1 |  |  |
| **whatsapp** | WhatsApp Business messaging, template management | 7 |  | 6 | 1 |  |
| **workflow** | MAAC module: workflow |  | 2 | 1 |  |  |

### CAAC Modules (13 total)

| Module | Description | code_dep | model_ref | const_ref | task_dep | api_client |
|--------|-------------|----------|-----------|-----------|----------|------------|
| **aistrategy** | AI strategy configuration — model selection, prompts |  |  |  |  |  |
| **aitask** | AI task execution — auto-reply suggestions, summarization | 3 |  |  |  |  |
| **aiusage** | AI usage tracking — token consumption, quota |  |  |  |  |  |
| **auth** | Authentication & authorization — SSO, 2FA |  |  |  |  |  |
| **cat** | CAT (Contact Attribution Tracking) — member journey tracking |  |  |  |  |  |
| **cdp** | CDP integration — unified contact view within CAAC |  |  |  |  |  |
| **chat** | Core 1-on-1 chat — message routing, conversation lifecycle | 5 |  |  |  |  |
| **dashboard** | CAAC analytics dashboard — conversation metrics, team perfor |  |  |  |  |  |
| **longrunningtask** | Long-running operations — bulk exports, data migration | 1 |  |  |  |  |
| **openapi** | CAAC public API for external integrations |  |  |  |  |  |
| **organization** | Organization management — channels, users, roles, AI feature | 1 |  |  |  |  |
| **tag** | Contact tagging within CAAC conversations |  |  |  |  |  |
| **workertask** | Background worker tasks — message processing, sync jobs | 1 |  |  |  |  |

### DAAC Modules (9 total)

| Module | Description | code_dep | model_ref | const_ref | task_dep | api_client |
|--------|-------------|----------|-----------|-----------|----------|------------|
| **agent_v2** | AI Agent — natural language data querying (OpenAI/Gemini) | 1 |  |  |  |  |
| **auth** | Authentication via Arioso SSO + Interlude |  |  |  |  |  |
| **dashboard** | Custom analytics dashboards — user-created visualizations | 1 |  |  |  |  |
| **dbt** | dbt pipeline management — data transformation & modeling | 1 |  |  |  |  |
| **file** | File management — upload/download for analysis results |  |  |  |  |  |
| **infra** | Infrastructure provisioning — Terraform client setup | 1 |  |  |  |  |
| **journey** | Journey analysis — customer path analysis via AI | 1 |  |  |  |  |
| **organization** | Org management — workspace, dbt config, Terraform infra | 1 |  |  |  |  |
| **session** | AI analysis session — conversation state, context management | 2 |  |  |  |  |

### CDH Modules (11 total)

| Module | Description | code_dep | model_ref | const_ref | task_dep | api_client |
|--------|-------------|----------|-----------|-----------|----------|------------|
| **broadcast** | CDH broadcast coordination — cross-product message dispatch |  |  |  |  |  |
| **channel_entity_comment** | Channel entity commenting — AI-powered contact annotations |  |  |  |  |  |
| **contact** | Unified contact profile — cross-product contact view | 1 |  |  |  |  |
| **custom_field** | Custom contact fields — user-defined attributes |  |  |  |  |  |
| **engagement_history** | Engagement history — cross-channel interaction tracking |  |  |  |  |  |
| **member** | Member management — import/export, profile enrichment | 2 |  |  |  |  |
| **richmenu** | LINE Rich Menu management via CDH |  |  |  |  |  |
| **segment** | Cross-product audience segmentation via SQL/LLM |  |  |  |  |  |
| **tag** | Cross-product tag synchronization | 1 |  |  |  |  |
| **task** | Background task execution — unification, sync, export jobs |  |  |  |  |  |
| **unification** | Contact unification graph — merge/split profiles across chan | 2 |  |  |  |  |

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

### MAAC/accounts
- **Product**: MAAC
- **Description**: User authentication, SSO, 2FA, session management
- **code_dep** → api_doc, audience, caac, channel, interlude, line, organization, sms
- **model_ref** → organization, sms
- **const_ref** → line, notification, sms
- **task_dep** → journey, line
- **← code_dep** from: audience, caac, email_channel, interlude, internal, line, notification, openapi, organization, smoke_test, system
- **← model_ref** from: audience, auto_reply, broadcast, caac, campaign, cdp, channel, cyberbiz, extension, fb, google_analytics, integration, interlude, journey, line, nine_one_app, organization, prize, referral, sforzando, shopify, shopline, system, tag
- **← const_ref** from: extension, organization, smoke_test
- **← api_client** from: internal
- **Frontend pages**: Organization Settings

### MAAC/ai_generation
- **Product**: MAAC
- **Description**: AI content generation — copywriting, image generation
- **code_dep** → organization, system
- **const_ref** → organization
- **← code_dep** from: line, openapi, organization
- **← const_ref** from: line

### MAAC/api_doc
- **Product**: MAAC
- **Description**: MAAC module: api_doc
- **← code_dep** from: accounts, audience, auto_reply, broadcast, caac, campaign, cdp, channel, email_channel, fb, form, integration, interlude, internal, journey, line, nine_one_app, openapi, organization, prize, receipt, smoke_test, sms, sms_plus, system, tag

### MAAC/async_wrapper
- **Product**: MAAC
- **Description**: MAAC module: async_wrapper
- **← code_dep** from: line, nine_one_app, receipt
- **← const_ref** from: line

### MAAC/audience
- **Product**: MAAC
- **Description**: Contact management, segments, filters, ad platform audiences
- **code_dep** → accounts, api_doc, bigquery, cdp, line, organization, system, tag
- **model_ref** → accounts, google_analytics, line, organization, sms, tag
- **const_ref** → cdp, line, organization, sms, system
- **← code_dep** from: accounts, broadcast, cdp, firestore, internal, journey, line, openapi, sms, tag
- **← model_ref** from: internal, journey, line, openapi, sms, system
- **← const_ref** from: bigquery, broadcast, internal, line, openapi, organization, sms
- **← task_dep** from: internal, line, openapi
- **Frontend pages**: Members, Retarget, Segment

### MAAC/auto_reply
- **Product**: MAAC
- **Description**: Keyword auto-reply across LINE/FB/WhatsApp channels
- **code_dep** → api_doc, channel, fb, google_analytics, line, organization, pubsub, wccs, whatsapp
- **model_ref** → accounts, line
- **const_ref** → channel, line, system, tag
- **task_dep** → tag
- **← code_dep** from: fb, internal, line, openapi, wccs, whatsapp
- **← const_ref** from: fb, line, openapi, wccs, whatsapp
- **Frontend pages**: Auto Reply

### MAAC/bigquery
- **Product**: MAAC
- **Description**: BigQuery data pipeline integration
- **code_dep** → receipt
- **model_ref** → line
- **const_ref** → audience, line, system
- **← code_dep** from: audience, line, organization, receipt, report, system

### MAAC/broadcast
- **Product**: MAAC
- **Description**: Push messaging (LINE/SMS/WhatsApp), scheduling, A/B test
- **code_dep** → api_doc, audience, channel, google_analytics, line, message, organization, report, system, tag
- **model_ref** → accounts
- **const_ref** → audience, channel, line, message, system
- **Frontend pages**: Broadcast

### MAAC/caac
- **Product**: MAAC
- **Description**: CAAC integration bridge — connects Rubato to Cantata
- **code_dep** → accounts, api_doc, line, organization
- **model_ref** → accounts, line
- **const_ref** → line
- **← code_dep** from: accounts, line, organization

### MAAC/campaign
- **Product**: MAAC
- **Description**: Campaign orchestration — multi-channel campaign management
- **code_dep** → api_doc, journey
- **model_ref** → accounts, journey
- **const_ref** → channel, journey

### MAAC/cdp
- **Product**: MAAC
- **Description**: Customer Data Platform — profile unification, data sync
- **code_dep** → api_doc, audience, interlude, journey, line, organization
- **model_ref** → accounts
- **const_ref** → line, tag
- **task_dep** → journey, tag
- **← code_dep** from: audience, journey, line, tag
- **← const_ref** from: audience, journey, line, pubsub_pull, smoke_test, tag
- **Frontend pages**: Members

### MAAC/channel
- **Product**: MAAC
- **Description**: Multi-channel management (LINE/FB/IG/WhatsApp/Email/SMS)
- **code_dep** → api_doc, line, message, openapi, organization
- **model_ref** → accounts, line, organization
- **const_ref** → line, notification, sms, system
- **task_dep** → notification
- **← code_dep** from: accounts, auto_reply, broadcast, email_channel, extension, internal, journey, message, openapi, organization, whatsapp
- **← model_ref** from: journey
- **← const_ref** from: auto_reply, broadcast, campaign, email_channel, extension, fb, internal, journey, line, message, openapi, organization, pubsub_pull, sms, wccs, whatsapp
- **Frontend pages**: Channel Settings

### MAAC/coupon
- **Product**: MAAC
- **Description**: MAAC module: coupon

### MAAC/cyberbiz
- **Product**: MAAC
- **Description**: Cyberbiz e-commerce integration
- **code_dep** → line
- **model_ref** → accounts

### MAAC/email_channel
- **Product**: MAAC
- **Description**: Email campaign delivery via SendGrid, bounce handling
- **code_dep** → accounts, api_doc, channel, extension, journey, line, organization, sms
- **const_ref** → channel, journey, line, system
- **task_dep** → journey
- **← code_dep** from: journey, line, openapi
- **Frontend pages**: Journey

### MAAC/extension
- **Product**: MAAC
- **Description**: MAAC extension plugins — custom action nodes
- **code_dep** → channel, google_analytics, interlude, journey, line, organization
- **model_ref** → accounts
- **const_ref** → accounts, channel, google_analytics, interlude, journey, line
- **← code_dep** from: email_channel, journey

### MAAC/fb
- **Product**: MAAC
- **Description**: Facebook/Instagram messaging, comment auto-reply
- **code_dep** → api_doc, auto_reply, google_analytics, line, message, organization, pubsub
- **model_ref** → accounts
- **const_ref** → auto_reply, channel, line, system
- **task_dep** → tag
- **← code_dep** from: auto_reply, smoke_test
- **← const_ref** from: line
- **Frontend pages**: Auto Reply, Retarget

### MAAC/firestore
- **Product**: MAAC
- **Description**: MAAC module: firestore
- **code_dep** → audience
- **model_ref** → line
- **← code_dep** from: line, system

### MAAC/form
- **Product**: MAAC
- **Description**: SurveyCake form integration, response tracking
- **code_dep** → api_doc, line
- **model_ref** → line
- **const_ref** → line, tag, webhook
- **task_dep** → line, tag, webhook
- **api_client** → line, tag
- **← model_ref** from: line
- **Frontend pages**: SurveyCake (Form)

### MAAC/google_analytics
- **Product**: MAAC
- **Description**: GA4/UTM tracking integration for campaigns
- **code_dep** → organization
- **model_ref** → accounts, line, organization, report
- **const_ref** → system
- **← code_dep** from: auto_reply, broadcast, extension, fb, journey, line, message, openapi, organization, prize, sms
- **← model_ref** from: audience, line, openapi, prize, report, system, workflow
- **← const_ref** from: extension, journey, line, openapi, prize
- **Frontend pages**: Insight (Dashboard), Tracelink

### MAAC/integration
- **Product**: MAAC
- **Description**: MAAC module: integration
- **code_dep** → api_doc, line
- **model_ref** → accounts

### MAAC/interlude
- **Product**: MAAC
- **Description**: MAAC module: interlude
- **code_dep** → accounts, api_doc, organization, payment
- **model_ref** → accounts
- **← code_dep** from: accounts, cdp, extension, internal, journey, line, nine_one_app, openapi, organization, payment, shopline, smoke_test, sms, sms_plus
- **← const_ref** from: extension, openapi, organization, sms

### MAAC/internal
- **Product**: MAAC
- **Description**: Internal admin tools — data migration, debugging
- **code_dep** → accounts, api_doc, audience, auto_reply, channel, interlude, line, message, nine_one_app, openapi, organization, prize, sms, wccs, webhook
- **model_ref** → audience, line, openapi, prize, webhook
- **const_ref** → audience, channel, line, openapi, organization, system
- **task_dep** → audience, organization, whatsapp
- **api_client** → accounts, line
- **← code_dep** from: organization

### MAAC/invoice
- **Product**: MAAC
- **Description**: Invoice management — receipt/reward redemption

### MAAC/journey
- **Product**: MAAC
- **Description**: Customer journey automation (triggers, actions, conditions)
- **code_dep** → api_doc, audience, cdp, channel, email_channel, extension, google_analytics, interlude, line, organization, report, sms, system, tag
- **model_ref** → accounts, audience, channel, line, tag
- **const_ref** → cdp, channel, google_analytics, line, organization, system, tag
- **task_dep** → tag
- **← code_dep** from: campaign, cdp, email_channel, extension, line, pubsub_pull, smoke_test, sms, tag
- **← model_ref** from: campaign, smoke_test
- **← const_ref** from: campaign, email_channel, extension, organization, smoke_test, sms
- **← task_dep** from: accounts, cdp, email_channel, line, pubsub_pull, tag
- **Frontend pages**: Journey

### MAAC/line
- **Product**: MAAC
- **Description**: Core LINE integration — messaging, rich menu, Flex, LIFF
- **code_dep** → accounts, ai_generation, api_doc, async_wrapper, audience, auto_reply, bigquery, caac, cdp, email_channel, firestore, google_analytics, interlude, journey, message, nine_one_app, openapi, organization, payment, prize, pubsub, receipt, referral, report, sforzando, shopify, shopline, sms, system, tag, webhook, whatsapp
- **model_ref** → accounts, audience, form, google_analytics, nine_one_app, notification, openapi, organization, prize, receipt, referral, report, shopify, shopline, sms, system, tag, webhook, workflow
- **const_ref** → ai_generation, async_wrapper, audience, auto_reply, cdp, channel, fb, google_analytics, message, notification, openapi, organization, receipt, sms, system, tag, webhook, whatsapp, workflow
- **task_dep** → audience, journey, nine_one_app, notification, openapi, shopline, sms, system, tag, webhook
- **api_client** → organization, prize, referral
- **← code_dep** from: accounts, audience, auto_reply, broadcast, caac, cdp, channel, cyberbiz, email_channel, extension, fb, form, integration, internal, journey, message, nine_one_app, openapi, organization, payment, prize, pubsub_pull, receipt, referral, report, sforzando, shopify, shopline, smoke_test, sms, sms_plus, system, tag, verification, wccs, webhook, whatsapp
- **← model_ref** from: audience, auto_reply, bigquery, caac, channel, firestore, form, google_analytics, internal, journey, message, nine_one_app, openapi, organization, payment, prize, receipt, referral, report, sforzando, shopify, shopline, smoke_test, sms, system, tag, webhook, workflow
- **← const_ref** from: accounts, audience, auto_reply, bigquery, broadcast, caac, cdp, channel, email_channel, extension, fb, form, internal, journey, message, openapi, organization, payment, prize, pubsub_pull, receipt, referral, report, shopify, smoke_test, sms, system, tag, wccs, whatsapp
- **← task_dep** from: accounts, form, nine_one_app, openapi, organization, prize, receipt, referral, shopify, shopline, system, tag
- **← api_client** from: form, internal, openapi, prize, receipt, referral, sforzando, sms
- **Frontend pages**: Beacon, Bindlink, DPM, Deeplink, Interaction Games, Rich Menu, Template Library, Widget

### MAAC/message
- **Product**: MAAC
- **Description**: Message rendering engine — builds LINE/FB/SMS/Email messages
- **code_dep** → channel, google_analytics, line, organization
- **model_ref** → line
- **const_ref** → channel, line, system
- **← code_dep** from: broadcast, channel, fb, internal, line, system, whatsapp
- **← const_ref** from: broadcast, line, system, whatsapp
- **Frontend pages**: Broadcast, Template Library

### MAAC/nine_one_app
- **Product**: MAAC
- **Description**: 91App e-commerce integration
- **code_dep** → api_doc, async_wrapper, interlude, line, openapi, organization, payment, webhook
- **model_ref** → accounts, line, openapi, system
- **const_ref** → openapi, tag, webhook
- **task_dep** → line, openapi, tag, webhook
- **api_client** → openapi
- **← code_dep** from: internal, line
- **← model_ref** from: line
- **← task_dep** from: line

### MAAC/notification
- **Product**: MAAC
- **Description**: In-app notification system for admin users
- **code_dep** → accounts
- **← code_dep** from: openapi, organization, payment, sms_plus
- **← model_ref** from: line, openapi, payment
- **← const_ref** from: accounts, channel, line, openapi, organization, payment, prize, sms_plus, system
- **← task_dep** from: channel, line, openapi, payment, prize

### MAAC/openapi
- **Product**: MAAC
- **Description**: Public OpenAPI — external developer API endpoints
- **code_dep** → accounts, ai_generation, api_doc, audience, auto_reply, channel, email_channel, google_analytics, interlude, line, notification, organization, payment, prize, report, shortener, sms, system, tag, whatsapp
- **model_ref** → audience, google_analytics, line, notification, tag
- **const_ref** → audience, auto_reply, channel, google_analytics, interlude, line, notification, organization, prize, sms, system, tag, webhook
- **task_dep** → audience, line, notification, tag, webhook
- **api_client** → line, sms
- **← code_dep** from: channel, internal, line, nine_one_app, organization, prize, pubsub_pull, receipt, shopline, sms, sms_plus, whatsapp
- **← model_ref** from: internal, line, nine_one_app, report, smoke_test, sms, webhook
- **← const_ref** from: internal, line, nine_one_app, smoke_test, sms, sms_plus, whatsapp
- **← task_dep** from: line, nine_one_app
- **← api_client** from: nine_one_app, shopline, sms
- **Frontend pages**: API Token

### MAAC/organization
- **Product**: MAAC
- **Description**: Org/tenant management, billing, feature control, RBAC
- **code_dep** → accounts, ai_generation, api_doc, bigquery, caac, channel, google_analytics, interlude, internal, line, notification, openapi, payment, sms, webhook
- **model_ref** → accounts, line
- **const_ref** → accounts, audience, channel, interlude, journey, line, notification
- **task_dep** → line
- **← code_dep** from: accounts, ai_generation, audience, auto_reply, broadcast, caac, cdp, channel, email_channel, extension, fb, google_analytics, interlude, internal, journey, line, message, nine_one_app, openapi, payment, prize, receipt, referral, sforzando, shopline, sms, sms_plus, tag, wccs, whatsapp
- **← model_ref** from: accounts, audience, channel, google_analytics, line, prize, sforzando, smoke_test, sms
- **← const_ref** from: ai_generation, audience, internal, journey, line, openapi
- **← task_dep** from: internal
- **← api_client** from: line
- **Frontend pages**: Organization Settings

### MAAC/payment
- **Product**: MAAC
- **Description**: Payment & billing — subscription, invoice management
- **code_dep** → interlude, line, notification, organization
- **model_ref** → line, notification
- **const_ref** → line, notification
- **task_dep** → notification
- **← code_dep** from: interlude, line, nine_one_app, openapi, organization, report, shopline, sms, sms_plus
- **← model_ref** from: report

### MAAC/prize
- **Product**: MAAC
- **Description**: Prize/reward management, lottery, coupon distribution
- **code_dep** → api_doc, google_analytics, line, openapi, organization, report, sforzando, system
- **model_ref** → accounts, google_analytics, line, organization, tag
- **const_ref** → google_analytics, line, notification, system, tag, webhook
- **task_dep** → line, notification, tag, webhook
- **api_client** → line
- **← code_dep** from: internal, line, openapi, receipt, referral, sforzando, webhook
- **← model_ref** from: internal, line, receipt, referral, sforzando
- **← const_ref** from: openapi, referral
- **← task_dep** from: referral, sforzando
- **← api_client** from: line
- **Frontend pages**: Interaction Games, Prize

### MAAC/pubsub
- **Product**: MAAC
- **Description**: MAAC module: pubsub
- **← code_dep** from: auto_reply, fb, line, system, wccs, whatsapp

### MAAC/pubsub_pull
- **Product**: MAAC
- **Description**: PubSub consumer — event processing workers
- **code_dep** → journey, line, openapi, sms
- **const_ref** → cdp, channel, line, system, tag
- **task_dep** → journey, tag

### MAAC/receipt
- **Product**: MAAC
- **Description**: Receipt registration campaign for loyalty programs
- **code_dep** → api_doc, async_wrapper, bigquery, line, openapi, organization, prize, system
- **model_ref** → line, prize
- **const_ref** → line, webhook
- **task_dep** → line, webhook
- **api_client** → line
- **← code_dep** from: bigquery, line
- **← model_ref** from: line, webhook
- **← const_ref** from: line
- **Frontend pages**: Receipt Register

### MAAC/referral
- **Product**: MAAC
- **Description**: Rapid Referral — MGM campaigns, invitation tracking
- **code_dep** → line, organization, prize, system
- **model_ref** → accounts, line, prize, tag
- **const_ref** → line, prize, tag
- **task_dep** → line, prize, tag
- **api_client** → line
- **← code_dep** from: line
- **← model_ref** from: line, system
- **← api_client** from: line
- **Frontend pages**: Referral V2

### MAAC/report
- **Product**: MAAC
- **Description**: Analytics & reporting — campaign performance, member stats
- **code_dep** → bigquery, line, payment
- **model_ref** → google_analytics, line, openapi, payment, sms_plus, tag
- **const_ref** → line, system
- **← code_dep** from: broadcast, journey, line, openapi, prize, sms
- **← model_ref** from: google_analytics, line, tag
- **Frontend pages**: Insight (Dashboard)

### MAAC/sforzando
- **Product**: MAAC
- **Description**: Prize fulfillment partner integration
- **code_dep** → line, organization, prize, system
- **model_ref** → accounts, line, organization, prize
- **const_ref** → tag
- **task_dep** → prize, tag
- **api_client** → line
- **← code_dep** from: line, prize
- **Frontend pages**: Prize

### MAAC/shopify
- **Product**: MAAC
- **Description**: Shopify e-commerce integration
- **code_dep** → line
- **model_ref** → accounts, line, system
- **const_ref** → line
- **task_dep** → line
- **← code_dep** from: line
- **← model_ref** from: line

### MAAC/shopline
- **Product**: MAAC
- **Description**: Shopline e-commerce integration
- **code_dep** → interlude, line, openapi, organization, payment, webhook
- **model_ref** → accounts, line, system
- **const_ref** → tag, webhook
- **task_dep** → line, tag, webhook
- **api_client** → openapi
- **← code_dep** from: line
- **← model_ref** from: line
- **← task_dep** from: line

### MAAC/shortener
- **Product**: MAAC
- **Description**: MAAC module: shortener
- **const_ref** → system
- **← code_dep** from: openapi

### MAAC/smoke_test
- **Product**: MAAC
- **Description**: Automated smoke test — system health validation
- **code_dep** → accounts, api_doc, fb, interlude, journey, line, tag
- **model_ref** → journey, line, openapi, organization, tag
- **const_ref** → accounts, cdp, journey, line, openapi, tag

### MAAC/sms
- **Product**: MAAC
- **Description**: SMS delivery — domestic/international SMS campaigns
- **code_dep** → api_doc, audience, google_analytics, interlude, journey, line, openapi, organization, payment, report, system
- **model_ref** → audience, line, openapi, organization
- **const_ref** → audience, channel, interlude, journey, line, openapi, system
- **api_client** → line, openapi
- **← code_dep** from: accounts, email_channel, internal, journey, line, openapi, organization, pubsub_pull, sms_plus
- **← model_ref** from: accounts, audience, line
- **← const_ref** from: accounts, audience, channel, line, openapi, sms_plus
- **← task_dep** from: line
- **← api_client** from: openapi
- **Frontend pages**: Broadcast, SMS Plus

### MAAC/sms_plus
- **Product**: MAAC
- **Description**: SMS Plus — enhanced SMS features, message records
- **code_dep** → api_doc, interlude, line, notification, openapi, organization, payment, sms, whatsapp
- **const_ref** → notification, openapi, sms
- **← model_ref** from: report
- **Frontend pages**: SMS Plus

### MAAC/staticfiles
- **Product**: MAAC
- **Description**: MAAC module: staticfiles

### MAAC/stress_test
- **Product**: MAAC
- **Description**: MAAC module: stress_test

### MAAC/system
- **Product**: MAAC
- **Description**: System-wide utilities — campaign tracking, feature flags
- **code_dep** → accounts, api_doc, bigquery, firestore, line, message, pubsub
- **model_ref** → accounts, audience, google_analytics, line, referral, tag
- **const_ref** → line, message, notification, tag
- **task_dep** → line, tag
- **← code_dep** from: ai_generation, audience, broadcast, journey, line, openapi, prize, receipt, referral, sforzando, sms, webhook
- **← model_ref** from: line, nine_one_app, shopify, shopline
- **← const_ref** from: audience, auto_reply, bigquery, broadcast, channel, email_channel, fb, google_analytics, internal, journey, line, message, openapi, prize, pubsub_pull, report, shortener, sms, tag, wccs, webhook, whatsapp, workflow
- **← task_dep** from: line

### MAAC/tag
- **Product**: MAAC
- **Description**: Tag management — contact tagging, auto-tagging rules
- **code_dep** → api_doc, audience, cdp, journey, line, organization
- **model_ref** → accounts, line, report
- **const_ref** → cdp, line, system
- **task_dep** → journey, line
- **← code_dep** from: audience, broadcast, journey, line, openapi, smoke_test, webhook
- **← model_ref** from: audience, journey, line, openapi, prize, referral, report, smoke_test, system
- **← const_ref** from: auto_reply, cdp, form, journey, line, nine_one_app, openapi, prize, pubsub_pull, referral, sforzando, shopline, smoke_test, system
- **← task_dep** from: auto_reply, cdp, fb, form, journey, line, nine_one_app, openapi, prize, pubsub_pull, referral, sforzando, shopline, system, wccs, whatsapp
- **← api_client** from: form
- **Frontend pages**: Members, Tag Manager

### MAAC/verification
- **Product**: MAAC
- **Description**: MAAC module: verification
- **code_dep** → line

### MAAC/wccs
- **Product**: MAAC
- **Description**: MAAC module: wccs
- **code_dep** → auto_reply, line, organization, pubsub
- **const_ref** → auto_reply, channel, line, system
- **task_dep** → tag
- **← code_dep** from: auto_reply, internal

### MAAC/webhook
- **Product**: MAAC
- **Description**: Webhook delivery — event push to external systems
- **code_dep** → line, prize, system, tag
- **model_ref** → line, openapi, receipt, workflow
- **const_ref** → system
- **← code_dep** from: internal, line, nine_one_app, organization, shopline
- **← model_ref** from: internal, line
- **← const_ref** from: form, line, nine_one_app, openapi, prize, receipt, shopline
- **← task_dep** from: form, line, nine_one_app, openapi, prize, receipt, shopline
- **Frontend pages**: Webhook

### MAAC/whatsapp
- **Product**: MAAC
- **Description**: WhatsApp Business messaging, template management
- **code_dep** → auto_reply, channel, line, message, openapi, organization, pubsub
- **const_ref** → auto_reply, channel, line, message, openapi, system
- **task_dep** → tag
- **← code_dep** from: auto_reply, line, openapi, sms_plus
- **← const_ref** from: line
- **← task_dep** from: internal
- **Frontend pages**: Auto Reply

### MAAC/workflow
- **Product**: MAAC
- **Description**: MAAC module: workflow
- **model_ref** → google_analytics, line
- **const_ref** → system
- **← model_ref** from: line, webhook
- **← const_ref** from: line

### CAAC/aistrategy
- **Product**: CAAC
- **Description**: AI strategy configuration — model selection, prompts
- **← code_dep** from: aitask, chat
- **Frontend pages**: AI Settings

### CAAC/aitask
- **Product**: CAAC
- **Description**: AI task execution — auto-reply suggestions, summarization
- **code_dep** → aistrategy, aiusage, chat
- **← code_dep** from: organization
- **Frontend pages**: AI Settings, Chat

### CAAC/aiusage
- **Product**: CAAC
- **Description**: AI usage tracking — token consumption, quota
- **← code_dep** from: aitask, chat, workertask
- **Frontend pages**: AI Settings

### CAAC/auth
- **Product**: CAAC
- **Description**: Authentication & authorization — SSO, 2FA
- **Frontend pages**: Settings

### CAAC/cat
- **Product**: CAAC
- **Description**: CAT (Contact Attribution Tracking) — member journey tracking

### CAAC/cdp
- **Product**: CAAC
- **Description**: CDP integration — unified contact view within CAAC
- **← code_dep** from: chat

### CAAC/chat
- **Product**: CAAC
- **Description**: Core 1-on-1 chat — message routing, conversation lifecycle
- **code_dep** → aistrategy, aiusage, cdp, organization, tag
- **← code_dep** from: aitask, longrunningtask
- **Frontend pages**: Broadcast, Chat, Quick Template

### CAAC/dashboard
- **Product**: CAAC
- **Description**: CAAC analytics dashboard — conversation metrics, team performance
- **Frontend pages**: Insights

### CAAC/longrunningtask
- **Product**: CAAC
- **Description**: Long-running operations — bulk exports, data migration
- **code_dep** → chat

### CAAC/openapi
- **Product**: CAAC
- **Description**: CAAC public API for external integrations

### CAAC/organization
- **Product**: CAAC
- **Description**: Organization management — channels, users, roles, AI features
- **code_dep** → aitask
- **← code_dep** from: chat
- **Frontend pages**: Settings

### CAAC/tag
- **Product**: CAAC
- **Description**: Contact tagging within CAAC conversations
- **← code_dep** from: chat

### CAAC/workertask
- **Product**: CAAC
- **Description**: Background worker tasks — message processing, sync jobs
- **code_dep** → aiusage

### DAAC/agent_v2
- **Product**: DAAC
- **Description**: AI Agent — natural language data querying (OpenAI/Gemini)
- **code_dep** → session

### DAAC/auth
- **Product**: DAAC
- **Description**: Authentication via Arioso SSO + Interlude
- **← code_dep** from: organization, session

### DAAC/dashboard
- **Product**: DAAC
- **Description**: Custom analytics dashboards — user-created visualizations
- **code_dep** → organization

### DAAC/dbt
- **Product**: DAAC
- **Description**: dbt pipeline management — data transformation & modeling
- **code_dep** → organization

### DAAC/file
- **Product**: DAAC
- **Description**: File management — upload/download for analysis results

### DAAC/infra
- **Product**: DAAC
- **Description**: Infrastructure provisioning — Terraform client setup
- **code_dep** → organization

### DAAC/journey
- **Product**: DAAC
- **Description**: Journey analysis — customer path analysis via AI
- **code_dep** → session

### DAAC/organization
- **Product**: DAAC
- **Description**: Org management — workspace, dbt config, Terraform infra
- **code_dep** → auth
- **← code_dep** from: dashboard, dbt, infra, session

### DAAC/session
- **Product**: DAAC
- **Description**: AI analysis session — conversation state, context management
- **code_dep** → auth, organization
- **← code_dep** from: agent_v2, journey

### CDH/broadcast
- **Product**: CDH
- **Description**: CDH broadcast coordination — cross-product message dispatch

### CDH/channel_entity_comment
- **Product**: CDH
- **Description**: Channel entity commenting — AI-powered contact annotations

### CDH/contact
- **Product**: CDH
- **Description**: Unified contact profile — cross-product contact view
- **code_dep** → unification

### CDH/custom_field
- **Product**: CDH
- **Description**: Custom contact fields — user-defined attributes

### CDH/engagement_history
- **Product**: CDH
- **Description**: Engagement history — cross-channel interaction tracking

### CDH/member
- **Product**: CDH
- **Description**: Member management — import/export, profile enrichment
- **code_dep** → tag, unification
- **← code_dep** from: tag, unification

### CDH/richmenu
- **Product**: CDH
- **Description**: LINE Rich Menu management via CDH

### CDH/segment
- **Product**: CDH
- **Description**: Cross-product audience segmentation via SQL/LLM

### CDH/tag
- **Product**: CDH
- **Description**: Cross-product tag synchronization
- **code_dep** → member
- **← code_dep** from: member, unification

### CDH/task
- **Product**: CDH
- **Description**: Background task execution — unification, sync, export jobs

### CDH/unification
- **Product**: CDH
- **Description**: Contact unification graph — merge/split profiles across channels
- **code_dep** → member, tag
- **← code_dep** from: contact, member

## 5. Frontend → Backend Mapping

### MAAC Frontend Pages

| Page | Calls Backend Modules |
|------|----------------------|
| API Token | openapi |
| Auto Reply | auto_reply, fb, whatsapp |
| Beacon | line |
| Bindlink | line |
| Broadcast | broadcast, message, sms |
| Channel Settings | channel |
| DPM | line |
| Deeplink | line |
| Insight (Dashboard) | google_analytics, report |
| Interaction Games | line, prize |
| Journey | email_channel, journey |
| Members | audience, cdp, tag |
| Organization Settings | accounts, organization |
| Prize | prize, sforzando |
| Receipt Register | receipt |
| Referral V2 | referral |
| Retarget | audience, fb |
| Rich Menu | line |
| SMS Plus | sms, sms_plus |
| Segment | audience |
| SurveyCake (Form) | form |
| Tag Manager | tag |
| Template Library | line, message |
| Tracelink | google_analytics |
| Webhook | webhook |
| Widget | line |

### CAAC Frontend Pages

| Page | Calls Backend Modules |
|------|----------------------|
| AI Settings | aistrategy, aitask, aiusage |
| Broadcast | chat |
| Chat | aitask, chat |
| Insights | dashboard |
| Quick Template | chat |
| Settings | auth, organization |

## 6. Infrastructure Dependencies

| Infrastructure | Description | Used by Products |
|---------------|-------------|-----------------|
| **BigQuery** | Analytics data warehouse, reporting | MAAC, CAAC, DAAC, CDH |
| **Cloud Run Jobs** | Task execution for heavy processing | CDH |
| **Cloud Storage (GCS)** | File/image storage | MAAC |
| **Cloud Tasks** | Deferred task execution | MAAC |
| **Datadog** | APM & distributed tracing | MAAC |
| **Elasticsearch** | Message search & conversation indexing | CAAC |
| **FCM** | Push notifications to mobile/browser | CAAC |
| **Firebase / Firestore** | Real-time database for live features | MAAC |
| **GCS** | File attachment storage | CAAC, DAAC, CDH |
| **Google Analytics** | Campaign tracking & UTM parameters | MAAC |
| **Infobip** | WhatsApp/Voice gateway | CAAC |
| **LINE Messaging API** | LINE platform messaging, rich menu, LIFF | MAAC |
| **Meta API (FB/IG)** | Facebook & Instagram messaging API | MAAC |
| **OpenAI** | AI for segment tagging & entity commenting | CDH |
| **OpenAI / Gemini** | AI model APIs for agent | DAAC |
| **PostgreSQL** | Primary database (Django ORM) | MAAC, CAAC, DAAC, CDH |
| **PubSub** | Event streaming for cross-service communication | MAAC, CAAC, CDH |
| **RabbitMQ / Celery** | Async task queue for background jobs | MAAC |
| **Redis** | Cache layer, Celery broker, rate limiting | MAAC, CAAC |
| **SendGrid** | Email delivery service | MAAC |
| **Sentry** | Error tracking & monitoring | MAAC |
| **Statsig** | Feature flag management | MAAC, CDH |
| **Terraform** | Infrastructure as code for client provisioning | DAAC |
| **WhatsApp Cloud API** | WhatsApp Business messaging via Infobip | MAAC |
| **dbt** | Data transformation pipeline | DAAC |

## 7. Shared Services

### Arioso
- SSO authentication service — Google/MS OAuth
- Used by: MAAC, CAAC, DAAC

### Harmony
- Partner API & Google Ads integration
- Used by: MAAC

### Interlude
- Admin center — billing, subscription, org provisioning
- Used by: MAAC, CAAC, DAAC

### MDS
- Message Delivery Service
- Used by: MAAC

### Monophony
- URL shortener service (maac.io)
- Used by: MAAC, CAAC

### Sforzando
- Prize fulfillment & reward distribution
- Used by: MAAC

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
| line | MAAC | 115 | 37 | 28 | 30 | 12 | 8 | 🔴 Critical |
| organization | MAAC | 47 | 30 | 9 | 6 | 1 | 1 | 🔴 Critical |
| tag | MAAC | 47 | 7 | 9 | 14 | 16 | 1 | 🔴 Critical |
| system | MAAC | 40 | 12 | 4 | 23 | 1 | 0 | 🔴 Critical |
| accounts | MAAC | 39 | 11 | 24 | 3 | 0 | 1 | 🔴 Critical |
| openapi | MAAC | 31 | 12 | 7 | 7 | 2 | 3 | 🔴 Critical |
| channel | MAAC | 28 | 11 | 1 | 16 | 0 | 0 | 🔴 Critical |
| api_doc | MAAC | 26 | 26 | 0 | 0 | 0 | 0 | 🔴 Critical |
| audience | MAAC | 26 | 10 | 6 | 7 | 3 | 0 | 🔴 Critical |
| google_analytics | MAAC | 23 | 11 | 7 | 5 | 0 | 0 | 🔴 Critical |
| journey | MAAC | 23 | 9 | 2 | 6 | 6 | 0 | 🔴 Critical |
| notification | MAAC | 21 | 4 | 3 | 9 | 5 | 0 | 🔴 Critical |
| webhook | MAAC | 21 | 5 | 2 | 7 | 7 | 0 | 🔴 Critical |
| sms | MAAC | 20 | 9 | 3 | 6 | 1 | 1 | 🔴 Critical |
| interlude | MAAC | 18 | 14 | 0 | 4 | 0 | 0 | 🔴 Critical |
| prize | MAAC | 17 | 7 | 5 | 2 | 2 | 1 | 🔴 Critical |
| auto_reply | MAAC | 11 | 6 | 0 | 5 | 0 | 0 | 🟡 High |
| message | MAAC | 11 | 7 | 0 | 4 | 0 | 0 | 🟡 High |
| cdp | MAAC | 10 | 4 | 0 | 6 | 0 | 0 | 🟡 High |
| payment | MAAC | 10 | 9 | 1 | 0 | 0 | 0 | 🟡 High |

### Hub Modules (most outgoing deps)

| Module | Product | Depends on N | Coupling |
|--------|---------|-------------|----------|
| line | MAAC | 83 | 🔴 High |
| openapi | MAAC | 45 | 🔴 High |
| internal | MAAC | 31 | 🔴 High |
| journey | MAAC | 27 | 🔴 High |
| organization | MAAC | 25 | 🔴 High |
| prize | MAAC | 24 | 🔴 High |
| sms | MAAC | 24 | 🔴 High |
| nine_one_app | MAAC | 20 | 🔴 High |
| audience | MAAC | 19 | 🔴 High |
| system | MAAC | 19 | 🔴 High |
| smoke_test | MAAC | 18 | 🔴 High |
| auto_reply | MAAC | 16 | 🔴 High |
| broadcast | MAAC | 16 | 🔴 High |
| accounts | MAAC | 15 | 🔴 High |
| receipt | MAAC | 15 | 🔴 High |

## 10. Change Impact Chains

Format: `If you change X → these modules are directly affected`

### Changing `line` (MAAC)
Directly affects 115 modules:
- via `code_dep`: accounts, audience, auto_reply, broadcast, caac, cdp, channel, cyberbiz, email_channel, extension, fb, form, integration, internal, journey, message, nine_one_app, openapi, organization, payment, prize, pubsub_pull, receipt, referral, report, sforzando, shopify, shopline, smoke_test, sms, sms_plus, system, tag, verification, wccs, webhook, whatsapp
- via `model_ref`: audience, auto_reply, bigquery, caac, channel, firestore, form, google_analytics, internal, journey, message, nine_one_app, openapi, organization, payment, prize, receipt, referral, report, sforzando, shopify, shopline, smoke_test, sms, system, tag, webhook, workflow
- via `const_ref`: accounts, audience, auto_reply, bigquery, broadcast, caac, cdp, channel, email_channel, extension, fb, form, internal, journey, message, openapi, organization, payment, prize, pubsub_pull, receipt, referral, report, shopify, smoke_test, sms, system, tag, wccs, whatsapp
- via `task_dep`: accounts, form, nine_one_app, openapi, organization, prize, receipt, referral, shopify, shopline, system, tag
- via `api_client`: form, internal, openapi, prize, receipt, referral, sforzando, sms

### Changing `organization` (MAAC)
Directly affects 47 modules:
- via `code_dep`: accounts, ai_generation, audience, auto_reply, broadcast, caac, cdp, channel, email_channel, extension, fb, google_analytics, interlude, internal, journey, line, message, nine_one_app, openapi, payment, prize, receipt, referral, sforzando, shopline, sms, sms_plus, tag, wccs, whatsapp
- via `model_ref`: accounts, audience, channel, google_analytics, line, prize, sforzando, smoke_test, sms
- via `const_ref`: ai_generation, audience, internal, journey, line, openapi
- via `task_dep`: internal
- via `api_client`: line

### Changing `tag` (MAAC)
Directly affects 47 modules:
- via `code_dep`: audience, broadcast, journey, line, openapi, smoke_test, webhook
- via `model_ref`: audience, journey, line, openapi, prize, referral, report, smoke_test, system
- via `const_ref`: auto_reply, cdp, form, journey, line, nine_one_app, openapi, prize, pubsub_pull, referral, sforzando, shopline, smoke_test, system
- via `task_dep`: auto_reply, cdp, fb, form, journey, line, nine_one_app, openapi, prize, pubsub_pull, referral, sforzando, shopline, system, wccs, whatsapp
- via `api_client`: form

### Changing `system` (MAAC)
Directly affects 40 modules:
- via `code_dep`: ai_generation, audience, broadcast, journey, line, openapi, prize, receipt, referral, sforzando, sms, webhook
- via `model_ref`: line, nine_one_app, shopify, shopline
- via `const_ref`: audience, auto_reply, bigquery, broadcast, channel, email_channel, fb, google_analytics, internal, journey, line, message, openapi, prize, pubsub_pull, report, shortener, sms, tag, wccs, webhook, whatsapp, workflow
- via `task_dep`: line

### Changing `accounts` (MAAC)
Directly affects 39 modules:
- via `code_dep`: audience, caac, email_channel, interlude, internal, line, notification, openapi, organization, smoke_test, system
- via `model_ref`: audience, auto_reply, broadcast, caac, campaign, cdp, channel, cyberbiz, extension, fb, google_analytics, integration, interlude, journey, line, nine_one_app, organization, prize, referral, sforzando, shopify, shopline, system, tag
- via `const_ref`: extension, organization, smoke_test
- via `api_client`: internal

### Changing `openapi` (MAAC)
Directly affects 31 modules:
- via `code_dep`: channel, internal, line, nine_one_app, organization, prize, pubsub_pull, receipt, shopline, sms, sms_plus, whatsapp
- via `model_ref`: internal, line, nine_one_app, report, smoke_test, sms, webhook
- via `const_ref`: internal, line, nine_one_app, smoke_test, sms, sms_plus, whatsapp
- via `task_dep`: line, nine_one_app
- via `api_client`: nine_one_app, shopline, sms

### Changing `channel` (MAAC)
Directly affects 28 modules:
- via `code_dep`: accounts, auto_reply, broadcast, email_channel, extension, internal, journey, message, openapi, organization, whatsapp
- via `model_ref`: journey
- via `const_ref`: auto_reply, broadcast, campaign, email_channel, extension, fb, internal, journey, line, message, openapi, organization, pubsub_pull, sms, wccs, whatsapp

### Changing `api_doc` (MAAC)
Directly affects 26 modules:
- via `code_dep`: accounts, audience, auto_reply, broadcast, caac, campaign, cdp, channel, email_channel, fb, form, integration, interlude, internal, journey, line, nine_one_app, openapi, organization, prize, receipt, smoke_test, sms, sms_plus, system, tag

### Changing `audience` (MAAC)
Directly affects 26 modules:
- via `code_dep`: accounts, broadcast, cdp, firestore, internal, journey, line, openapi, sms, tag
- via `model_ref`: internal, journey, line, openapi, sms, system
- via `const_ref`: bigquery, broadcast, internal, line, openapi, organization, sms
- via `task_dep`: internal, line, openapi

### Changing `google_analytics` (MAAC)
Directly affects 23 modules:
- via `code_dep`: auto_reply, broadcast, extension, fb, journey, line, message, openapi, organization, prize, sms
- via `model_ref`: audience, line, openapi, prize, report, system, workflow
- via `const_ref`: extension, journey, line, openapi, prize

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

### BigQuery
- Analytics data warehouse, reporting
- **Depended on by**: CAAC, CDH, DAAC, MAAC

### Cloud Run Jobs
- Task execution for heavy processing
- **Depended on by**: CDH

### Cloud Storage (GCS)
- File/image storage
- **Depended on by**: MAAC

### Cloud Tasks
- Deferred task execution
- **Depended on by**: MAAC

### Datadog
- APM & distributed tracing
- **Depended on by**: MAAC

### Elasticsearch
- Message search & conversation indexing
- **Depended on by**: CAAC

### FCM
- Push notifications to mobile/browser
- **Depended on by**: CAAC

### Firebase / Firestore
- Real-time database for live features
- **Depended on by**: MAAC

### GCS
- File attachment storage
- **Depended on by**: CAAC, CDH, DAAC

### Google Analytics
- Campaign tracking & UTM parameters
- **Depended on by**: MAAC

### Infobip
- WhatsApp/Voice gateway
- **Depended on by**: CAAC

### LINE Messaging API
- LINE platform messaging, rich menu, LIFF
- **Depended on by**: MAAC

### Meta API (FB/IG)
- Facebook & Instagram messaging API
- **Depended on by**: MAAC

### OpenAI
- AI for segment tagging & entity commenting
- **Depended on by**: CDH

### OpenAI / Gemini
- AI model APIs for agent
- **Depended on by**: DAAC

### PostgreSQL
- Primary database (Django ORM)
- **Depended on by**: CAAC, CDH, DAAC, MAAC

### PubSub
- Event streaming for cross-service communication
- **Depended on by**: CAAC, CDH, MAAC

### RabbitMQ / Celery
- Async task queue for background jobs
- **Depended on by**: MAAC

### Redis
- Cache layer, Celery broker, rate limiting
- **Depended on by**: CAAC, MAAC

### SendGrid
- Email delivery service
- **Depended on by**: MAAC

### Sentry
- Error tracking & monitoring
- **Depended on by**: MAAC

### Statsig
- Feature flag management
- **Depended on by**: CDH, MAAC

### Terraform
- Infrastructure as code for client provisioning
- **Depended on by**: DAAC

### WhatsApp Cloud API
- WhatsApp Business messaging via Infobip
- **Depended on by**: MAAC

### dbt
- Data transformation pipeline
- **Depended on by**: DAAC

## 13. Semantic Dependency Hotspots

Modules with the most fine-grained semantic dependencies (model_ref + const_ref + task_dep + api_client):

| Module | Product | Total Semantic Edges | model_ref | const_ref | task_dep | api_client |
|--------|---------|---------------------|-----------|-----------|----------|------------|
| line | MAAC | 129 | 47 | 49 | 22 | 11 |
| tag | MAAC | 48 | 12 | 17 | 18 | 1 |
| openapi | MAAC | 44 | 12 | 20 | 7 | 5 |
| system | MAAC | 40 | 10 | 27 | 3 | 0 |
| accounts | MAAC | 35 | 26 | 6 | 2 | 1 |
| audience | MAAC | 27 | 12 | 12 | 3 | 0 |
| journey | MAAC | 27 | 7 | 13 | 7 | 0 |
| organization | MAAC | 27 | 11 | 13 | 2 | 1 |
| prize | MAAC | 26 | 10 | 8 | 6 | 2 |
| channel | MAAC | 25 | 4 | 20 | 1 | 0 |
| sms | MAAC | 24 | 7 | 13 | 1 | 3 |
| webhook | MAAC | 21 | 6 | 8 | 7 | 0 |
| google_analytics | MAAC | 17 | 11 | 6 | 0 | 0 |
| notification | MAAC | 17 | 3 | 9 | 5 | 0 |
| internal | MAAC | 16 | 5 | 6 | 3 | 2 |
| nine_one_app | MAAC | 14 | 5 | 3 | 5 | 1 |
| referral | MAAC | 14 | 6 | 3 | 3 | 2 |
| auto_reply | MAAC | 12 | 2 | 9 | 1 | 0 |
| cdp | MAAC | 11 | 1 | 8 | 2 | 0 |
| report | MAAC | 11 | 9 | 2 | 0 | 0 |

---
*End of Code Architecture Knowledge Graph v7*