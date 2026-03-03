# Crescendo Lab — Code Architecture Knowledge Graph (LLM-Optimized)

> Auto-generated from source code analysis on 2026-03-03 15:03
> Repos: rubato (MAAC BE), Grazioso (MAAC FE), cantata (CAAC BE), Zeffiroso (CAAC FE), bebop (DAAC), polyrhythmic (CDH)
> Nodes: 137 | Edges: 495
> Purpose: Verified architecture map from actual import analysis — for LLM impact analysis & attribution.

---

## 1. Product Suite

### CAAC
- **CAAC**: Conversation Automation & Analytics Cloud
- Title: CAAC — Conversation Automation & Analytics Cloud
Tech: Go (Cantata) + React (Zeffiroso/TS)
Repos: {'backend': 'cantata (Go)', 'frontend': 'Zeffiroso (React/TS)'}

**Cross-product connections:**
- → MAAC: MAAC_URL (REST API)
- → CDH: CDH_INTERNAL_URL (Unification V2)

### CDH
- **CDH**: Customer Data Hub — Unified Contact Profile
- Title: CDH — Customer Data Hub — Unified Contact Profile
Tech: Python + Go (Polyrhythmic)
Repos: {'backend': 'polyrhythmic (Python+Go)', 'frontend': 'N/A (API-only)'}

**Cross-product connections:**
- → MAAC: RUBATO_HOST + RUBATO_DB_DSN
- → CAAC: CANTATA_HOST + CANTATA_DB_DSN

### DAAC
- **DAAC**: Data Automation & Analytics Cloud
- Title: DAAC — Data Automation & Analytics Cloud
Tech: Python (FastAPI) + React + AI Agent
Repos: {'backend': 'bebop (Python/FastAPI)', 'frontend': 'bebop/frontend (React/TS)'}

**Cross-product connections:**
- → MAAC: MAAC_GCP_PROJECT_ID (BigQuery)
- → CAAC: CAAC_GCP_PROJECT_ID (BigQuery)

### MAAC
- **MAAC**: Marketing Automation & Analytics Cloud
- Title: MAAC — Marketing Automation & Analytics Cloud
Tech: Django 3.2 + React 19 (TypeScript)
Repos: {'backend': 'rubato (Python/Django)', 'frontend': 'Grazioso (React/TS)'}

**Cross-product connections:**
- → CAAC: CAAC_CANTATA_URL (REST API)
- → DAAC: DAAC_API_URL (REST API)

## 2. Module Architecture

### CAAC Modules

| Module | Description | Dependencies (imports) |
|--------|-------------|----------------------|
| **aistrategy** | AI strategy configuration — model selection, prompts |  |
| **aitask** | AI task execution — auto-reply suggestions, summarization | aistrategy, aiusage, chat |
| **aiusage** | AI usage tracking — token consumption, quota |  |
| **auth** | Authentication & authorization — SSO, 2FA |  |
| **cat** | CAT (Contact Attribution Tracking) — member journey tracking |  |
| **cdp** | CDP integration — unified contact view within CAAC |  |
| **chat** | Core 1-on-1 chat — message routing, conversation lifecycle | aistrategy, aiusage, cdp, organization, tag |
| **dashboard** | CAAC analytics dashboard — conversation metrics, team performance |  |
| **longrunningtask** | Long-running operations — bulk exports, data migration | chat |
| **openapi** | CAAC public API for external integrations |  |
| **organization** | Organization management — channels, users, roles, AI features | aitask |
| **tag** | Contact tagging within CAAC conversations |  |
| **workertask** | Background worker tasks — message processing, sync jobs | aiusage |

### CDH Modules

| Module | Description | Dependencies (imports) |
|--------|-------------|----------------------|
| **broadcast** | CDH broadcast coordination — cross-product message dispatch |  |
| **channel_entity_comment** | Channel entity commenting — AI-powered contact annotations |  |
| **contact** | Unified contact profile — cross-product contact view | unification |
| **custom_field** | Custom contact fields — user-defined attributes |  |
| **engagement_history** | Engagement history — cross-channel interaction tracking |  |
| **member** | Member management — import/export, profile enrichment | tag, unification |
| **richmenu** | LINE Rich Menu management via CDH |  |
| **segment** | Cross-product audience segmentation via SQL/LLM |  |
| **tag** | Cross-product tag synchronization | member |
| **task** | Background task execution — unification, sync, export jobs |  |
| **unification** | Contact unification graph — merge/split profiles across channels | member, tag |

### DAAC Modules

| Module | Description | Dependencies (imports) |
|--------|-------------|----------------------|
| **agent_v2** | AI Agent — natural language data querying (OpenAI/Gemini) | session |
| **auth** | Authentication via Arioso SSO + Interlude |  |
| **dashboard** | Custom analytics dashboards — user-created visualizations | organization |
| **dbt** | dbt pipeline management — data transformation & modeling | organization |
| **file** | File management — upload/download for analysis results |  |
| **infra** | Infrastructure provisioning — Terraform client setup | organization |
| **journey** | Journey analysis — customer path analysis via AI | session |
| **organization** | Org management — workspace, dbt config, Terraform infra | auth |
| **session** | AI analysis session — conversation state, context management | auth, organization |

### MAAC Modules

| Module | Description | Dependencies (imports) |
|--------|-------------|----------------------|
| **accounts** | User authentication, SSO, 2FA, session management | audience, caac, channel, journey, line, notification, organization, sms |
| **ai_generation** | AI content generation — copywriting, image generation | organization, system |
| **audience** | Contact management, segments, filters, ad platform audiences | accounts, cdp, google_analytics, line, organization, sms, system, tag |
| **auto_reply** | Keyword auto-reply across LINE/FB/WhatsApp channels | accounts, channel, fb, google_analytics, line, organization, tag, whatsapp |
| **broadcast** | Push messaging (LINE/SMS/WhatsApp), scheduling, A/B test | accounts, audience, channel, google_analytics, line, message, organization, report... |
| **caac** | CAAC integration bridge — connects Rubato to Cantata | accounts, line, organization |
| **campaign** | Campaign orchestration — multi-channel campaign management | accounts, channel, journey |
| **cdp** | Customer Data Platform — profile unification, data sync | accounts, audience, journey, line, organization, tag |
| **channel** | Multi-channel management (LINE/FB/IG/WhatsApp/Email/SMS) | accounts, line, message, notification, openapi, organization, sms, system |
| **cyberbiz** | Cyberbiz e-commerce integration | accounts, line |
| **email_channel** | Email campaign delivery via SendGrid, bounce handling | accounts, channel, journey, line, organization, sms, system |
| **extension** | MAAC extension plugins — custom action nodes | accounts, channel, google_analytics, journey, line, organization |
| **fb** | Facebook/Instagram messaging, comment auto-reply | accounts, auto_reply, channel, google_analytics, line, organization, tag |
| **form** | SurveyCake form integration, response tracking | line, tag, webhook |
| **google_analytics** | GA4/UTM tracking integration for campaigns | accounts, line, organization, report, system |
| **journey** | Customer journey automation (triggers, actions, conditions) | accounts, audience, cdp, channel, email_channel, google_analytics, line, organization... |
| **line** | Core LINE integration — messaging, rich menu, Flex, LIFF | accounts, audience, auto_reply, caac, cdp, channel, email_channel, fb... |
| **message** | Message rendering engine — builds LINE/FB/SMS/Email messages | channel, google_analytics, line, organization, system |
| **nine_one_app** | 91App e-commerce integration | accounts, line, openapi, organization, payment, system, tag, webhook |
| **notification** | In-app notification system for admin users | accounts |
| **openapi** | Public OpenAPI — external developer API endpoints | accounts, audience, auto_reply, channel, email_channel, google_analytics, line, notification... |
| **organization** | Org/tenant management, billing, feature control, RBAC | accounts, audience, caac, channel, google_analytics, journey, line, notification... |
| **payment** | Payment & billing — subscription, invoice management | line, notification, organization |
| **prize** | Prize/reward management, lottery, coupon distribution | accounts, google_analytics, line, notification, openapi, organization, report, sforzando... |
| **receipt** | Receipt registration campaign for loyalty programs | line, openapi, organization, prize, system, webhook |
| **referral** | Rapid Referral — MGM campaigns, invitation tracking | accounts, line, organization, prize, system, tag |
| **report** | Analytics & reporting — campaign performance, member stats | google_analytics, line, openapi, payment, sms_plus, system, tag |
| **sforzando** | Prize fulfillment partner integration | accounts, line, organization, prize, system, tag |
| **shopify** | Shopify e-commerce integration | accounts, line, system |
| **shopline** | Shopline e-commerce integration | accounts, line, openapi, organization, payment, system, tag, webhook |
| **sms** | SMS delivery — domestic/international SMS campaigns | audience, channel, google_analytics, journey, line, openapi, organization, payment... |
| **sms_plus** | SMS Plus — enhanced SMS features, message records | line, notification, openapi, organization, payment, sms, whatsapp |
| **system** | System-wide utilities — campaign tracking, feature flags | accounts, audience, google_analytics, line, message, notification, referral, tag |
| **tag** | Tag management — contact tagging, auto-tagging rules | accounts, audience, cdp, journey, line, organization, report, system |
| **webhook** | Webhook delivery — event push to external systems | line, openapi, prize, receipt, system, tag |
| **whatsapp** | WhatsApp Business messaging, template management | auto_reply, channel, line, message, openapi, organization, tag |

## 3. Module Details

### CAAC/aistrategy
- **Product**: CAAC
- **Description**: AI strategy configuration — model selection, prompts
- **Imported by**: aitask, chat
- **Frontend pages**: AI Settings

### CAAC/aitask
- **Product**: CAAC
- **Description**: AI task execution — auto-reply suggestions, summarization
- **Imports from**: aistrategy, aiusage, chat
- **Imported by**: organization
- **Frontend pages**: AI Settings, Chat

### CAAC/aiusage
- **Product**: CAAC
- **Description**: AI usage tracking — token consumption, quota
- **Imported by**: aitask, chat, workertask
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
- **Imported by**: chat

### CAAC/chat
- **Product**: CAAC
- **Description**: Core 1-on-1 chat — message routing, conversation lifecycle
- **Imports from**: aistrategy, aiusage, cdp, organization, tag
- **Imported by**: aitask, longrunningtask
- **Frontend pages**: Broadcast, Chat, Quick Template

### CAAC/dashboard
- **Product**: CAAC
- **Description**: CAAC analytics dashboard — conversation metrics, team performance
- **Frontend pages**: Insights

### CAAC/longrunningtask
- **Product**: CAAC
- **Description**: Long-running operations — bulk exports, data migration
- **Imports from**: chat

### CAAC/openapi
- **Product**: CAAC
- **Description**: CAAC public API for external integrations

### CAAC/organization
- **Product**: CAAC
- **Description**: Organization management — channels, users, roles, AI features
- **Imports from**: aitask
- **Imported by**: chat
- **Frontend pages**: Settings

### CAAC/tag
- **Product**: CAAC
- **Description**: Contact tagging within CAAC conversations
- **Imported by**: chat

### CAAC/workertask
- **Product**: CAAC
- **Description**: Background worker tasks — message processing, sync jobs
- **Imports from**: aiusage

### CDH/broadcast
- **Product**: CDH
- **Description**: CDH broadcast coordination — cross-product message dispatch

### CDH/channel_entity_comment
- **Product**: CDH
- **Description**: Channel entity commenting — AI-powered contact annotations

### CDH/contact
- **Product**: CDH
- **Description**: Unified contact profile — cross-product contact view
- **Imports from**: unification

### CDH/custom_field
- **Product**: CDH
- **Description**: Custom contact fields — user-defined attributes

### CDH/engagement_history
- **Product**: CDH
- **Description**: Engagement history — cross-channel interaction tracking

### CDH/member
- **Product**: CDH
- **Description**: Member management — import/export, profile enrichment
- **Imports from**: tag, unification
- **Imported by**: tag, unification

### CDH/richmenu
- **Product**: CDH
- **Description**: LINE Rich Menu management via CDH

### CDH/segment
- **Product**: CDH
- **Description**: Cross-product audience segmentation via SQL/LLM

### CDH/tag
- **Product**: CDH
- **Description**: Cross-product tag synchronization
- **Imports from**: member
- **Imported by**: member, unification

### CDH/task
- **Product**: CDH
- **Description**: Background task execution — unification, sync, export jobs

### CDH/unification
- **Product**: CDH
- **Description**: Contact unification graph — merge/split profiles across channels
- **Imports from**: member, tag
- **Imported by**: contact, member

### DAAC/agent_v2
- **Product**: DAAC
- **Description**: AI Agent — natural language data querying (OpenAI/Gemini)
- **Imports from**: session

### DAAC/auth
- **Product**: DAAC
- **Description**: Authentication via Arioso SSO + Interlude
- **Imported by**: organization, session

### DAAC/dashboard
- **Product**: DAAC
- **Description**: Custom analytics dashboards — user-created visualizations
- **Imports from**: organization

### DAAC/dbt
- **Product**: DAAC
- **Description**: dbt pipeline management — data transformation & modeling
- **Imports from**: organization

### DAAC/file
- **Product**: DAAC
- **Description**: File management — upload/download for analysis results

### DAAC/infra
- **Product**: DAAC
- **Description**: Infrastructure provisioning — Terraform client setup
- **Imports from**: organization

### DAAC/journey
- **Product**: DAAC
- **Description**: Journey analysis — customer path analysis via AI
- **Imports from**: session

### DAAC/organization
- **Product**: DAAC
- **Description**: Org management — workspace, dbt config, Terraform infra
- **Imports from**: auth
- **Imported by**: dashboard, dbt, infra, session

### DAAC/session
- **Product**: DAAC
- **Description**: AI analysis session — conversation state, context management
- **Imports from**: auth, organization
- **Imported by**: agent_v2, journey

### MAAC/accounts
- **Product**: MAAC
- **Description**: User authentication, SSO, 2FA, session management
- **Imports from**: audience, caac, channel, journey, line, notification, organization, sms
- **Imported by**: audience, auto_reply, broadcast, caac, campaign, cdp, channel, cyberbiz, email_channel, extension, fb, google_analytics, journey, line, nine_one_app, notification, openapi, organization, prize, referral, sforzando, shopify, shopline, system, tag
- **Frontend pages**: Organization Settings

### MAAC/ai_generation
- **Product**: MAAC
- **Description**: AI content generation — copywriting, image generation
- **Imports from**: organization, system

### MAAC/audience
- **Product**: MAAC
- **Description**: Contact management, segments, filters, ad platform audiences
- **Imports from**: accounts, cdp, google_analytics, line, organization, sms, system, tag
- **Imported by**: accounts, broadcast, cdp, journey, line, openapi, organization, sms, system, tag
- **Frontend pages**: Members, Retarget, Segment

### MAAC/auto_reply
- **Product**: MAAC
- **Description**: Keyword auto-reply across LINE/FB/WhatsApp channels
- **Imports from**: accounts, channel, fb, google_analytics, line, organization, tag, whatsapp
- **Imported by**: fb, line, openapi, whatsapp
- **Frontend pages**: Auto Reply

### MAAC/broadcast
- **Product**: MAAC
- **Description**: Push messaging (LINE/SMS/WhatsApp), scheduling, A/B test
- **Imports from**: accounts, audience, channel, google_analytics, line, message, organization, report, system, tag
- **Frontend pages**: Broadcast

### MAAC/caac
- **Product**: MAAC
- **Description**: CAAC integration bridge — connects Rubato to Cantata
- **Imports from**: accounts, line, organization
- **Imported by**: accounts, line, organization

### MAAC/campaign
- **Product**: MAAC
- **Description**: Campaign orchestration — multi-channel campaign management
- **Imports from**: accounts, channel, journey

### MAAC/cdp
- **Product**: MAAC
- **Description**: Customer Data Platform — profile unification, data sync
- **Imports from**: accounts, audience, journey, line, organization, tag
- **Imported by**: audience, journey, line, tag
- **Frontend pages**: Members

### MAAC/channel
- **Product**: MAAC
- **Description**: Multi-channel management (LINE/FB/IG/WhatsApp/Email/SMS)
- **Imports from**: accounts, line, message, notification, openapi, organization, sms, system
- **Imported by**: accounts, auto_reply, broadcast, campaign, email_channel, extension, fb, journey, line, message, openapi, organization, sms, whatsapp
- **Frontend pages**: Channel Settings

### MAAC/cyberbiz
- **Product**: MAAC
- **Description**: Cyberbiz e-commerce integration
- **Imports from**: accounts, line

### MAAC/email_channel
- **Product**: MAAC
- **Description**: Email campaign delivery via SendGrid, bounce handling
- **Imports from**: accounts, channel, journey, line, organization, sms, system
- **Imported by**: journey, line, openapi
- **Frontend pages**: Journey

### MAAC/extension
- **Product**: MAAC
- **Description**: MAAC extension plugins — custom action nodes
- **Imports from**: accounts, channel, google_analytics, journey, line, organization

### MAAC/fb
- **Product**: MAAC
- **Description**: Facebook/Instagram messaging, comment auto-reply
- **Imports from**: accounts, auto_reply, channel, google_analytics, line, organization, tag
- **Imported by**: auto_reply, line
- **Frontend pages**: Auto Reply, Retarget

### MAAC/form
- **Product**: MAAC
- **Description**: SurveyCake form integration, response tracking
- **Imports from**: line, tag, webhook
- **Imported by**: line
- **Frontend pages**: SurveyCake (Form)

### MAAC/google_analytics
- **Product**: MAAC
- **Description**: GA4/UTM tracking integration for campaigns
- **Imports from**: accounts, line, organization, report, system
- **Imported by**: audience, auto_reply, broadcast, extension, fb, journey, line, message, openapi, organization, prize, report, sms, system
- **Frontend pages**: Insight (Dashboard), Tracelink

### MAAC/journey
- **Product**: MAAC
- **Description**: Customer journey automation (triggers, actions, conditions)
- **Imports from**: accounts, audience, cdp, channel, email_channel, google_analytics, line, organization, report, sms, system, tag
- **Imported by**: accounts, campaign, cdp, email_channel, extension, line, organization, sms, tag
- **Frontend pages**: Journey

### MAAC/line
- **Product**: MAAC
- **Description**: Core LINE integration — messaging, rich menu, Flex, LIFF
- **Imports from**: accounts, audience, auto_reply, caac, cdp, channel, email_channel, fb, form, google_analytics, journey, message, notification, openapi, organization, prize, receipt, referral, report, sms, system, tag, webhook, whatsapp
- **Imported by**: accounts, audience, auto_reply, broadcast, caac, cdp, channel, cyberbiz, email_channel, extension, fb, form, google_analytics, journey, message, nine_one_app, openapi, organization, payment, prize, receipt, referral, report, sforzando, shopify, shopline, sms, sms_plus, system, tag, webhook, whatsapp
- **Frontend pages**: Beacon, Bindlink, DPM, Deeplink, Interaction Games, Rich Menu, Template Library, Widget

### MAAC/message
- **Product**: MAAC
- **Description**: Message rendering engine — builds LINE/FB/SMS/Email messages
- **Imports from**: channel, google_analytics, line, organization, system
- **Imported by**: broadcast, channel, line, system, whatsapp
- **Frontend pages**: Broadcast, Template Library

### MAAC/nine_one_app
- **Product**: MAAC
- **Description**: 91App e-commerce integration
- **Imports from**: accounts, line, openapi, organization, payment, system, tag, webhook

### MAAC/notification
- **Product**: MAAC
- **Description**: In-app notification system for admin users
- **Imports from**: accounts
- **Imported by**: accounts, channel, line, openapi, organization, payment, prize, sms_plus, system

### MAAC/openapi
- **Product**: MAAC
- **Description**: Public OpenAPI — external developer API endpoints
- **Imports from**: accounts, audience, auto_reply, channel, email_channel, google_analytics, line, notification, organization, payment, prize, report, sms, system, tag, webhook, whatsapp
- **Imported by**: channel, line, nine_one_app, organization, prize, receipt, report, shopline, sms, sms_plus, webhook, whatsapp
- **Frontend pages**: API Token

### MAAC/organization
- **Product**: MAAC
- **Description**: Org/tenant management, billing, feature control, RBAC
- **Imports from**: accounts, audience, caac, channel, google_analytics, journey, line, notification, openapi, payment
- **Imported by**: accounts, ai_generation, audience, auto_reply, broadcast, caac, cdp, channel, email_channel, extension, fb, google_analytics, journey, line, message, nine_one_app, openapi, payment, prize, receipt, referral, sforzando, shopline, sms, sms_plus, tag, whatsapp
- **Frontend pages**: Organization Settings

### MAAC/payment
- **Product**: MAAC
- **Description**: Payment & billing — subscription, invoice management
- **Imports from**: line, notification, organization
- **Imported by**: nine_one_app, openapi, organization, report, shopline, sms, sms_plus

### MAAC/prize
- **Product**: MAAC
- **Description**: Prize/reward management, lottery, coupon distribution
- **Imports from**: accounts, google_analytics, line, notification, openapi, organization, report, sforzando, system, tag, webhook
- **Imported by**: line, openapi, receipt, referral, sforzando, webhook
- **Frontend pages**: Interaction Games, Prize

### MAAC/receipt
- **Product**: MAAC
- **Description**: Receipt registration campaign for loyalty programs
- **Imports from**: line, openapi, organization, prize, system, webhook
- **Imported by**: line, webhook
- **Frontend pages**: Receipt Register

### MAAC/referral
- **Product**: MAAC
- **Description**: Rapid Referral — MGM campaigns, invitation tracking
- **Imports from**: accounts, line, organization, prize, system, tag
- **Imported by**: line, system
- **Frontend pages**: Referral V2

### MAAC/report
- **Product**: MAAC
- **Description**: Analytics & reporting — campaign performance, member stats
- **Imports from**: google_analytics, line, openapi, payment, sms_plus, system, tag
- **Imported by**: broadcast, google_analytics, journey, line, openapi, prize, sms, tag
- **Frontend pages**: Insight (Dashboard)

### MAAC/sforzando
- **Product**: MAAC
- **Description**: Prize fulfillment partner integration
- **Imports from**: accounts, line, organization, prize, system, tag
- **Imported by**: prize
- **Frontend pages**: Prize

### MAAC/shopify
- **Product**: MAAC
- **Description**: Shopify e-commerce integration
- **Imports from**: accounts, line, system

### MAAC/shopline
- **Product**: MAAC
- **Description**: Shopline e-commerce integration
- **Imports from**: accounts, line, openapi, organization, payment, system, tag, webhook

### MAAC/sms
- **Product**: MAAC
- **Description**: SMS delivery — domestic/international SMS campaigns
- **Imports from**: audience, channel, google_analytics, journey, line, openapi, organization, payment, report, system
- **Imported by**: accounts, audience, channel, email_channel, journey, line, openapi, sms_plus
- **Frontend pages**: Broadcast, SMS Plus

### MAAC/sms_plus
- **Product**: MAAC
- **Description**: SMS Plus — enhanced SMS features, message records
- **Imports from**: line, notification, openapi, organization, payment, sms, whatsapp
- **Imported by**: report
- **Frontend pages**: SMS Plus

### MAAC/system
- **Product**: MAAC
- **Description**: System-wide utilities — campaign tracking, feature flags
- **Imports from**: accounts, audience, google_analytics, line, message, notification, referral, tag
- **Imported by**: ai_generation, audience, broadcast, channel, email_channel, google_analytics, journey, line, message, nine_one_app, openapi, prize, receipt, referral, report, sforzando, shopify, shopline, sms, tag, webhook

### MAAC/tag
- **Product**: MAAC
- **Description**: Tag management — contact tagging, auto-tagging rules
- **Imports from**: accounts, audience, cdp, journey, line, organization, report, system
- **Imported by**: audience, auto_reply, broadcast, cdp, fb, form, journey, line, nine_one_app, openapi, prize, referral, report, sforzando, shopline, system, webhook, whatsapp
- **Frontend pages**: Members, Tag Manager

### MAAC/webhook
- **Product**: MAAC
- **Description**: Webhook delivery — event push to external systems
- **Imports from**: line, openapi, prize, receipt, system, tag
- **Imported by**: form, line, nine_one_app, openapi, prize, receipt, shopline
- **Frontend pages**: Webhook

### MAAC/whatsapp
- **Product**: MAAC
- **Description**: WhatsApp Business messaging, template management
- **Imports from**: auto_reply, channel, line, message, openapi, organization, tag
- **Imported by**: auto_reply, line, openapi, sms_plus
- **Frontend pages**: Auto Reply

## 4. Frontend → Backend Mapping

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
| Insight (Dashboard) | report, google_analytics |
| Interaction Games | prize, line |
| Journey | journey, email_channel |
| Members | audience, cdp, tag |
| Organization Settings | organization, accounts |
| Prize | prize, sforzando |
| Receipt Register | receipt |
| Referral V2 | referral |
| Retarget | audience, fb |
| Rich Menu | line |
| SMS Plus | sms_plus, sms |
| Segment | audience |
| SurveyCake (Form) | form |
| Tag Manager | tag |
| Template Library | message, line |
| Tracelink | google_analytics |
| Webhook | webhook |
| Widget | line |

### CAAC Frontend Pages

| Page | Calls Backend Modules |
|------|----------------------|
| AI Settings | aistrategy, aitask, aiusage |
| Broadcast | chat |
| Chat | chat, aitask |
| Insights | dashboard |
| Quick Template | chat |
| Settings | organization, auth |

## 5. Infrastructure Dependencies

| Infrastructure | Description | Used by Products |
|---------------|-------------|-----------------|
| **BigQuery** | Data warehouse for engagement history & analytics | CAAC, CDH, DAAC, MAAC |
| **Cloud Run Jobs** | Task execution for heavy processing | CDH |
| **Cloud Storage (GCS)** | File/image storage | MAAC |
| **Cloud Tasks** | Deferred task execution | MAAC |
| **Datadog** | APM & distributed tracing | MAAC |
| **Elasticsearch** | Message search & conversation indexing | CAAC |
| **FCM** | Push notifications to mobile/browser | CAAC |
| **Firebase / Firestore** | Real-time database for live features | MAAC |
| **GCS** | File storage for import/export | CAAC, CDH, DAAC |
| **Google Analytics** | Campaign tracking & UTM parameters | MAAC |
| **Infobip** | WhatsApp/Voice gateway | CAAC |
| **LINE Messaging API** | LINE platform messaging, rich menu, LIFF | MAAC |
| **Meta API (FB/IG)** | Facebook & Instagram messaging API | MAAC |
| **OpenAI** | AI for segment tagging & entity commenting | CDH |
| **OpenAI / Gemini** | AI model APIs for agent | DAAC |
| **PostgreSQL** | Primary database (SQLAlchemy + raw SQL) | CAAC, CDH, DAAC, MAAC |
| **PubSub** | Event streaming — profile changes, tag updates | CAAC, CDH, MAAC |
| **RabbitMQ / Celery** | Async task queue for background jobs | MAAC |
| **Redis** | Session cache, rate limiting, pub/sub | CAAC, MAAC |
| **SendGrid** | Email delivery service | MAAC |
| **Sentry** | Error tracking & monitoring | MAAC |
| **Statsig** | Feature flag management | CDH, MAAC |
| **Terraform** | Infrastructure as code for client provisioning | DAAC |
| **WhatsApp Cloud API** | WhatsApp Business messaging via Infobip | MAAC |
| **dbt** | Data transformation pipeline | DAAC |

## 6. Shared Services

### Arioso
- SSO authentication service — Google/MS OAuth
- Used by: CAAC, DAAC, MAAC

### Harmony
- Partner API & Google Ads integration
- Used by: MAAC

### Interlude
- Admin center — billing, subscription, org provisioning
- Used by: CAAC, DAAC, MAAC

### MDS
- Message Delivery Service
- Used by: MAAC

### Monophony
- URL shortener service (maac.io)
- Used by: CAAC, MAAC

### Sforzando
- Prize fulfillment & reward distribution
- Used by: MAAC

## 7. Cross-Product Data Flow

```
MAAC (rubato) ──CAAC_CANTATA_URL──→ CAAC (cantata)
MAAC (rubato) ──DAAC_API_URL──────→ DAAC (bebop)
CAAC (cantata) ──MAAC_URL──────────→ MAAC (rubato)
CAAC (cantata) ──CDH_INTERNAL_URL──→ CDH  (polyrhythmic)
CDH  ──RUBATO_HOST+DB_DSN──────────→ MAAC (reads DB)
CDH  ──CANTATA_HOST+DB_DSN─────────→ CAAC (reads DB)
DAAC ──MAAC_GCP_PROJECT_ID─────────→ MAAC (BigQuery)
DAAC ──CAAC_GCP_PROJECT_ID─────────→ CAAC (BigQuery)
```

## 8. Impact Analysis Guide

### High-Impact Modules (most imported by others)

| Module | Imported by N modules | Risk |
|--------|----------------------|------|
| maac/line | 32 | 🔴 Critical |
| maac/organization | 27 | 🔴 Critical |
| maac/accounts | 25 | 🔴 Critical |
| maac/system | 21 | 🔴 Critical |
| maac/tag | 18 | 🔴 Critical |
| maac/channel | 14 | 🔴 Critical |
| maac/google_analytics | 14 | 🔴 Critical |
| maac/openapi | 12 | 🔴 Critical |
| maac/audience | 10 | 🟡 High |
| maac/journey | 9 | 🟡 High |
| maac/notification | 9 | 🟡 High |
| maac/sms | 8 | 🟡 High |
| maac/report | 8 | 🟡 High |
| maac/webhook | 7 | 🟡 High |
| maac/payment | 7 | 🟡 High |

### Hub Modules (most outgoing deps)

| Module | Depends on N modules | Coupling |
|--------|---------------------|----------|
| maac/line | 24 | 🔴 High |
| maac/openapi | 17 | 🔴 High |
| maac/journey | 12 | 🔴 High |
| maac/prize | 11 | 🔴 High |
| maac/broadcast | 10 | 🟡 Medium |
| maac/organization | 10 | 🟡 Medium |
| maac/sms | 10 | 🟡 Medium |
| maac/accounts | 8 | 🟡 Medium |
| maac/audience | 8 | 🟡 Medium |
| maac/auto_reply | 8 | 🟡 Medium |
| maac/channel | 8 | 🟡 Medium |
| maac/tag | 8 | 🟡 Medium |
| maac/system | 8 | 🟡 Medium |
| maac/nine_one_app | 8 | 🟡 Medium |
| maac/shopline | 8 | 🟡 Medium |

## 9. Change Impact Chains

Format: `If you change X → these modules are directly affected`

### Changing `maac/line`
Directly affects 32 modules:
- maac/accounts
- maac/audience
- maac/auto_reply
- maac/broadcast
- maac/caac
- maac/cdp
- maac/channel
- maac/cyberbiz
- maac/email_channel
- maac/extension
- maac/fb
- maac/form
- maac/google_analytics
- maac/journey
- maac/message
- maac/nine_one_app
- maac/openapi
- maac/organization
- maac/payment
- maac/prize
- maac/receipt
- maac/referral
- maac/report
- maac/sforzando
- maac/shopify
- maac/shopline
- maac/sms
- maac/sms_plus
- maac/system
- maac/tag
- maac/webhook
- maac/whatsapp

### Changing `maac/organization`
Directly affects 27 modules:
- maac/accounts
- maac/ai_generation
- maac/audience
- maac/auto_reply
- maac/broadcast
- maac/caac
- maac/cdp
- maac/channel
- maac/email_channel
- maac/extension
- maac/fb
- maac/google_analytics
- maac/journey
- maac/line
- maac/message
- maac/nine_one_app
- maac/openapi
- maac/payment
- maac/prize
- maac/receipt
- maac/referral
- maac/sforzando
- maac/shopline
- maac/sms
- maac/sms_plus
- maac/tag
- maac/whatsapp

### Changing `maac/accounts`
Directly affects 25 modules:
- maac/audience
- maac/auto_reply
- maac/broadcast
- maac/caac
- maac/campaign
- maac/cdp
- maac/channel
- maac/cyberbiz
- maac/email_channel
- maac/extension
- maac/fb
- maac/google_analytics
- maac/journey
- maac/line
- maac/nine_one_app
- maac/notification
- maac/openapi
- maac/organization
- maac/prize
- maac/referral
- maac/sforzando
- maac/shopify
- maac/shopline
- maac/system
- maac/tag

### Changing `maac/system`
Directly affects 21 modules:
- maac/ai_generation
- maac/audience
- maac/broadcast
- maac/channel
- maac/email_channel
- maac/google_analytics
- maac/journey
- maac/line
- maac/message
- maac/nine_one_app
- maac/openapi
- maac/prize
- maac/receipt
- maac/referral
- maac/report
- maac/sforzando
- maac/shopify
- maac/shopline
- maac/sms
- maac/tag
- maac/webhook

### Changing `maac/tag`
Directly affects 18 modules:
- maac/audience
- maac/auto_reply
- maac/broadcast
- maac/cdp
- maac/fb
- maac/form
- maac/journey
- maac/line
- maac/nine_one_app
- maac/openapi
- maac/prize
- maac/referral
- maac/report
- maac/sforzando
- maac/shopline
- maac/system
- maac/webhook
- maac/whatsapp

### Changing `maac/channel`
Directly affects 14 modules:
- maac/accounts
- maac/auto_reply
- maac/broadcast
- maac/campaign
- maac/email_channel
- maac/extension
- maac/fb
- maac/journey
- maac/line
- maac/message
- maac/openapi
- maac/organization
- maac/sms
- maac/whatsapp

### Changing `maac/google_analytics`
Directly affects 14 modules:
- maac/audience
- maac/auto_reply
- maac/broadcast
- maac/extension
- maac/fb
- maac/journey
- maac/line
- maac/message
- maac/openapi
- maac/organization
- maac/prize
- maac/report
- maac/sms
- maac/system

### Changing `maac/openapi`
Directly affects 12 modules:
- maac/channel
- maac/line
- maac/nine_one_app
- maac/organization
- maac/prize
- maac/receipt
- maac/report
- maac/shopline
- maac/sms
- maac/sms_plus
- maac/webhook
- maac/whatsapp

### Changing `maac/audience`
Directly affects 10 modules:
- maac/accounts
- maac/broadcast
- maac/cdp
- maac/journey
- maac/line
- maac/openapi
- maac/organization
- maac/sms
- maac/system
- maac/tag

### Changing `maac/journey`
Directly affects 9 modules:
- maac/accounts
- maac/campaign
- maac/cdp
- maac/email_channel
- maac/extension
- maac/line
- maac/organization
- maac/sms
- maac/tag

---
*End of Code Architecture Knowledge Graph*