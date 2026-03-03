# Crescendo Lab — Knowledge Graph (LLM-Optimized)

> Auto-generated on 2026-03-03 12:10
> Nodes: 189 | Edges: 319
> Purpose: Provide LLMs a flattened, structured representation of the CL product suite's
>          architecture, dependencies, root causes, and issue attribution.

---

## 1. Product Suite Overview

### MAAC
- MAAC
- Marketing Automation
- & Analytics Cloud
- Core marketing automation platform — LINE/FB/IG/SMS messaging, automation, analytics

**Cross-product relationships:**
- MAAC ←shares contacts→ CAAC
- MAAC ←unifies contacts→ CDH
- MAAC ←provides data→ DAAC

### CAAC
- CAAC
- Conversation Automation
- & Analytics Cloud
- Real-time chat and conversation management — agent inbox, chatbot, AI assist

**Cross-product relationships:**
- CAAC ←unifies contacts→ CDH
- CAAC ←shares contacts→ MAAC

### DAAC
- DAAC
- Data Automation
- & Analytics Cloud
- Data analytics engine — Audience360, predictive models, data enrichment

**Cross-product relationships:**
- DAAC ←provides data→ MAAC
- DAAC ←enriches data→ CDH

### CDH
- CDH
- Customer Data Hub
- Cross-platform data unification — profile merging, segment engine, data exchange

**Cross-product relationships:**
- CDH ←unifies contacts→ MAAC
- CDH ←unifies contacts→ CAAC
- CDH ←enriches data→ DAAC

## 2. Module Architecture

### MAAC Modules

| Module | Sub-features | Issues | Infra Dependencies |
|--------|-------------|--------|-------------------|
| **Auto-reply** | Keyword Auto-reply, Web Chat Auto-reply, Auto-reply Scheduling, New Friend Welcome, Reply Limit & Dedup | 20 | LINE API, Meta API |
| **Broadcast** | LINE Broadcast, Broadcast Scheduling, Broadcast Report | 0 | LINE API |
| **Contacts** | Contact Profile, Profile Unification, Contact Import/Export, Email Channel, Contact Fields | 0 | LINE API, PostgreSQL |
| **Customer Journey** | Journey Editor, Journey Triggers, Journey Actions, Journey Conditions, Journey Report, EDM Integration | 0 | SendGrid, Airflow |
| **Deeplink** | Deeplink Generator, UTM Tracking, Deeplink Report, Deeplink QR Code | 15 | LIFF |
| **Insight** | Data Overview, Deeplink Report, Acquisition Analytics, Open Rate Hotspot, Message Analytics | 18 | Airflow, BigQuery, PostgreSQL |
| **Prize Management** | Prize Setup, Rapid Referral, Prize Messages | 7 | LINE API |
| **Rich Menu** | Rich Menu Editor, Rich Menu Scheduling | 1 | LINE API |
| **Segment** | AI Segment, Segment Filters, Segment Tag Ops | 26 | BigQuery |
| **Smart redirect tool** | Smart Redirect | 0 | — |
| **Tag Manager** | Tag CRUD, Auto Tagging, Tag Coverage | 10 | PostgreSQL |
| **Template Library** | Message Templates | 1 | — |
| **Tracelink** | Tracelink Short URL, LIFF Integration, CLID Tracking | 8 | LIFF, Redis |

## 3. Module Details

### Auto-reply
- MAAC Module: Auto-reply
- Known issues: 20

**Sub-features:**
- **Keyword Auto-reply**: Keyword Auto-reply — Trigger replies based on keyword matching
- **Web Chat Auto-reply**: Web Chat Auto-reply — Auto-reply for web chat channels
- **Auto-reply Scheduling**: Auto-reply Scheduling — Time-based auto-reply activation
- **New Friend Welcome**: New Friend Welcome — Greeting for new contacts
- **Reply Limit & Dedup**: Reply Limit & Dedup — Rate limiting and deduplication

**Data flows:**
- Auto-reply → Contacts (creates contacts)
- Template Library → Auto-reply (provides templates)

**Infrastructure dependencies:**
- LINE API
- Meta API

**Issues (20):** P2: 19, P3: 1

### Broadcast
- MAAC Module: Broadcast

**Sub-features:**
- **LINE Broadcast**: LINE Broadcast — Push messages to LINE contacts
- **Broadcast Scheduling**: Broadcast Scheduling — Schedule future broadcast sends
- **Broadcast Report**: Broadcast Report — Post-send analytics and delivery stats

**Data flows:**
- Broadcast → Insight (feeds metrics)
- Segment → Broadcast (filters audience)
- Template Library → Broadcast (provides templates)
- Customer Journey → Broadcast (sends messages)

**Infrastructure dependencies:**
- LINE API

### Contacts
- MAAC Module: Contacts

**Sub-features:**
- **Contact Profile**: Contact Profile — Unified contact profile with LINE UID, CID, phone, email
- **Profile Unification**: Profile Unification — Merge contacts across channels using matching logic
- **Contact Import/Export**: Contact Import/Export — Bulk import/export contacts via CSV or API
- **Email Channel**: Email Channel — Email contact management and sender domain setup
- **Contact Fields**: Contact Fields — Custom and system fields on contact profiles

**Data flows:**
- Contacts → Segment (provides data)
- Contacts → Customer Journey (enters journey)
- Tag Manager → Contacts (labels contacts)
- Deeplink → Contacts (acquires contacts)
- Auto-reply → Contacts (creates contacts)

**Infrastructure dependencies:**
- LINE API
- PostgreSQL

### Customer Journey
- MAAC Module: Customer Journey

**Sub-features:**
- **Journey Editor**: Journey Editor — Visual flow canvas for journey design
- **Journey Triggers**: Journey Triggers — Event-based triggers (tag, GA, time)
- **Journey Actions**: Journey Actions — Message send, tag ops, wait nodes
- **Journey Conditions**: Journey Conditions — Yes/No branch and filter conditions
- **Journey Report**: Journey Report — Per-node analytics and conversion
- **EDM Integration**: EDM Integration — Email channel in journey via SendGrid

**Data flows:**
- Customer Journey → Broadcast (sends messages)
- Customer Journey → Tag Manager (applies tags)
- Customer Journey → Segment (uses segments)
- Contacts → Customer Journey (enters journey)

**Infrastructure dependencies:**
- SendGrid
- Airflow

### Deeplink
- MAAC Module: Deeplink
- Known issues: 15

**Sub-features:**
- **Deeplink Generator**: Deeplink Generator — Create trackable deeplinks for LINE
- **UTM Tracking**: UTM Tracking — UTM parameter support for deeplinks
- **Deeplink Report**: Deeplink Report — Click and conversion analytics
- **Deeplink QR Code**: Deeplink QR Code — QR code generation for deeplinks

**Data flows:**
- Deeplink → Contacts (acquires contacts)
- Deeplink → Insight (feeds analytics)
- Tracelink → Deeplink (wraps URLs)
- Rich Menu → Deeplink (links to deeplinks)

**Infrastructure dependencies:**
- LIFF

**Issues (15):** P2: 13, P4: 2

### Insight
- MAAC Module: Insight
- Known issues: 18

**Sub-features:**
- **Data Overview**: Data Overview — Dashboard with LINE overview, tag coverage, CID binding
- **Deeplink Report**: Deeplink Report — Tracks new contacts acquired via deeplinks
- **Acquisition Analytics**: Acquisition Analytics — New contact acquisition metrics and sources
- **Open Rate Hotspot**: Open Rate Hotspot — Heatmap of message open rates by day/time
- **Message Analytics**: Message Analytics — Track messages sent across channels

**Data flows:**
- Deeplink → Insight (feeds analytics)
- Broadcast → Insight (feeds metrics)

**Infrastructure dependencies:**
- Airflow
- BigQuery
- PostgreSQL

**Issues (18):** P1: 2, P2: 13, P3: 2, P4: 1

### Prize Management
- MAAC Module: Prize Management
- Known issues: 7

**Sub-features:**
- **Prize Setup**: Prize Setup — Configure prizes for campaigns
- **Rapid Referral**: Rapid Referral — Referral campaign prize distribution
- **Prize Messages**: Prize Messages — LINE Flex Message prize notifications

**Infrastructure dependencies:**
- LINE API

**Issues (7):** P1: 2, P2: 4, P4: 1

### Rich Menu
- MAAC Module: Rich Menu
- Known issues: 1

**Sub-features:**
- **Rich Menu Editor**: Rich Menu Editor — Visual editor for LINE rich menus
- **Rich Menu Scheduling**: Rich Menu Scheduling — Schedule rich menu activation

**Data flows:**
- Rich Menu → Deeplink (links to deeplinks)

**Infrastructure dependencies:**
- LINE API

**Issues (1):** P2: 1

### Segment
- MAAC Module: Segment
- Known issues: 26

**Sub-features:**
- **AI Segment**: AI Segment — NL prompt-based audience segmentation
- **Segment Filters**: Segment Filters — Rule-based segmentation with include/exclude
- **Segment Tag Ops**: Segment Tag Ops — Batch tag operations on segments

**Data flows:**
- Segment → Broadcast (filters audience)
- Contacts → Segment (provides data)
- Tag Manager → Segment (tags for filtering)
- Customer Journey → Segment (uses segments)

**Infrastructure dependencies:**
- BigQuery

**Issues (26):** P0: 2, P1: 4, P2: 17, P3: 2, P4: 1

### Smart redirect tool
- MAAC Module: Smart redirect tool

**Sub-features:**
- **Smart Redirect**: Smart Redirect — Intelligent URL redirection logic

### Tag Manager
- MAAC Module: Tag Manager
- Known issues: 10

**Sub-features:**
- **Tag CRUD**: Tag CRUD — Create, read, update, delete tags
- **Auto Tagging**: Auto Tagging — Rule-based automatic tag assignment
- **Tag Coverage**: Tag Coverage — Analytics on tag usage across contacts

**Data flows:**
- Tag Manager → Segment (tags for filtering)
- Tag Manager → Contacts (labels contacts)
- Customer Journey → Tag Manager (applies tags)

**Infrastructure dependencies:**
- PostgreSQL

**Issues (10):** P2: 9, P3: 1

### Template Library
- MAAC Module: Template Library
- Known issues: 1

**Sub-features:**
- **Message Templates**: Message Templates — Reusable LINE Flex Message templates

**Data flows:**
- Template Library → Broadcast (provides templates)
- Template Library → Auto-reply (provides templates)

**Issues (1):** P2: 1

### Tracelink
- MAAC Module: Tracelink
- Known issues: 8

**Sub-features:**
- **Tracelink Short URL**: Tracelink Short URL — Short URL generation with tracking
- **LIFF Integration**: LIFF Integration — LINE Front-end Framework integration
- **CLID Tracking**: CLID Tracking — Cross-domain customer ID tracking

**Data flows:**
- Tracelink → Deeplink (wraps URLs)

**Infrastructure dependencies:**
- LIFF
- Redis

**Issues (8):** P2: 4, P3: 2, P4: 2

## 4. Cross-Module Dependency Map

This section maps how modules depend on and feed data to each other.
Use this to understand impact when changing a module.

```
FROM                  → TO                    RELATIONSHIP
─────────────────────────────────────────────────────────────
CDH                    → MAAC                   unifies contacts
CDH                    → CAAC                   unifies contacts
DAAC                   → MAAC                   provides data
DAAC                   → CDH                    enriches data
MAAC                   → CAAC                   shares contacts
Contacts               → Segment                provides data
Segment                → Broadcast              filters audience
Template Library       → Broadcast              provides templates
Template Library       → Auto-reply             provides templates
Tag Manager            → Segment                tags for filtering
Tag Manager            → Contacts               labels contacts
Deeplink               → Contacts               acquires contacts
Deeplink               → Insight                feeds analytics
Tracelink              → Deeplink               wraps URLs
Broadcast              → Insight                feeds metrics
Customer Journey       → Broadcast              sends messages
Customer Journey       → Tag Manager            applies tags
Customer Journey       → Segment                uses segments
Auto-reply             → Contacts               creates contacts
Rich Menu              → Deeplink               links to deeplinks
Contacts               → Customer Journey       enters journey
CDH                    → Contacts               unifies profiles
DAAC                   → Segment                feeds AI Segment
```

## 5. Infrastructure Dependencies

### Airflow
- Infrastructure: Airflow
- Apache Airflow for ETL pipelines
- **Used by:** Insight, Customer Journey

### BigQuery
- Infrastructure: BigQuery
- Google BigQuery data warehouse
- **Used by:** Insight, Segment

### Django Admin
- Infrastructure: Django Admin
- Admin panel for config management

### LIFF
- Infrastructure: LIFF
- LINE Front-end Framework
- **Used by:** Deeplink, Tracelink

### LINE API
- Infrastructure: LINE API
- LINE Messaging API, LIFF, Rich Menu API
- **Used by:** Contacts, Broadcast, Auto-reply, Prize Management, Rich Menu

### Meta API
- Infrastructure: Meta API
- Facebook & Instagram messaging APIs
- **Used by:** Auto-reply

### PostgreSQL
- Infrastructure: PostgreSQL
- Primary relational database
- **Used by:** Insight, Contacts, Tag Manager

### Redis
- Infrastructure: Redis
- Cache layer for session/state
- **Used by:** Tracelink

### SendGrid
- Infrastructure: SendGrid
- Email delivery service
- **Used by:** Customer Journey

## 6. Root Cause Taxonomy

Root causes are clustered from 106 investigation tickets.
Each cluster represents a systemic pattern that recurs across modules.

### Other Root Cause (33 tickets)
- Root Cause: Other Root Cause
- Other root causes not fitting major categories
- Affected: 33 tickets

**Affected modules:**
- Segment: 11 tickets
- Auto-reply: 8 tickets
- Prize Management: 5 tickets
- Insight: 2 tickets
- Deeplink: 2 tickets
- Tracelink: 2 tickets
- Tag Manager: 1 tickets

### Config / Permission (13 tickets)
- Root Cause: Config / Permission
- Missing permissions or disabled settings
- Affected: 13 tickets

**Affected modules:**
- Auto-reply: 4 tickets
- Segment: 3 tickets
- Insight: 2 tickets
- Tag Manager: 1 tickets
- Deeplink: 1 tickets
- Tracelink: 1 tickets

**Related infrastructure:** Django Admin

### Data Inconsistency (12 tickets)
- Root Cause: Data Inconsistency
- Mismatched metrics between reports/dashboards
- Affected: 12 tickets

**Affected modules:**
- Insight: 4 tickets
- Segment: 4 tickets
- Tag Manager: 3 tickets
- Tracelink: 1 tickets

### External API Dep (11 tickets)
- Root Cause: External API Dep
- LINE/Meta/SendGrid API changes, rate limits, or policy restrictions
- Affected: 11 tickets

**Affected modules:**
- Deeplink: 6 tickets
- Auto-reply: 3 tickets
- Segment: 1 tickets
- Rich Menu: 1 tickets

**Related infrastructure:** LINE API, Meta API

### Data Pipeline Failure (10 tickets)
- Root Cause: Data Pipeline Failure
- Airflow DAG failures, BigQuery sync issues, ETL errors causing missing report data
- Affected: 10 tickets

**Affected modules:**
- Insight: 7 tickets
- Segment: 3 tickets

**Related infrastructure:** Airflow, BigQuery

### Webhook / Sync Delay (10 tickets)
- Root Cause: Webhook / Sync Delay
- Event processing timing, race conditions
- Affected: 10 tickets

**Affected modules:**
- Tag Manager: 3 tickets
- Insight: 2 tickets
- Segment: 2 tickets
- Auto-reply: 2 tickets
- Prize Management: 1 tickets

### User Misunderstanding (5 tickets)
- Root Cause: User Misunderstanding
- Customer misunderstanding resolved by documentation
- Affected: 5 tickets

**Affected modules:**
- Segment: 1 tickets
- Tag Manager: 1 tickets
- Template Library: 1 tickets
- Auto-reply: 1 tickets

### By Design (3 tickets)
- Root Cause: By Design
- Behavior working as designed but misaligned with user expectations
- Affected: 3 tickets

**Affected modules:**
- Insight: 1 tickets
- Tag Manager: 1 tickets
- Tracelink: 1 tickets

### Quota / Limit (3 tickets)
- Root Cause: Quota / Limit
- System or API quota/rate limit exceeded
- Affected: 3 tickets

**Affected modules:**
- Deeplink: 5 tickets
- Segment: 1 tickets
- Auto-reply: 1 tickets

### Encoding / Format (3 tickets)
- Root Cause: Encoding / Format
- Character encoding, emoji, or template format issues
- Affected: 3 tickets

**Affected modules:**
- Auto-reply: 1 tickets
- Tracelink: 1 tickets
- Prize Management: 1 tickets

### Cache / State Issue (2 tickets)
- Root Cause: Cache / State Issue
- Stale cache, cookies, or session data
- Affected: 2 tickets

**Affected modules:**
- Tracelink: 2 tickets

**Related infrastructure:** Redis

### Resource Constraint (1 tickets)
- Root Cause: Resource Constraint
- Issues too costly to fix; accepted technical debt
- Affected: 1 tickets

**Affected modules:**
- Deeplink: 1 tickets

## 7. Issue Catalog — Attribution Table

Each issue is linked to its module, root cause cluster, and Asana ticket.

### P0 Issues (2)

| Issue | Module | Root Cause | Asana |
|-------|--------|-----------|-------|
| Data Insights Display Anomalies in Multi | Segment | Data Pipeline Failure | [1213131750073052](https://app.asana.com/1/1184020052539844/task/1213131750073052) |
| Contact Discrepancy in LINE Segment | Segment | Data Inconsistency | [1213084606836149](https://app.asana.com/1/1184020052539844/task/1213084606836149) |

### P1 Issues (8)

| Issue | Module | Root Cause | Asana |
|-------|--------|-----------|-------|
| Zero Tag Coverage in MAAC Data Insights | Insight | Data Pipeline Failure | [1213185386062836](https://app.asana.com/1/1184020052539844/task/1213185386062836) |
| Missing Data in Data Insights Report for | Insight | Data Pipeline Failure | [1212601716064139](https://app.asana.com/1/1184020052539844/task/1212601716064139) |
| Prize Management Editing Issue | Prize Management | Other Root Cause | [1212834391682490](https://app.asana.com/1/1184020052539844/task/1212834391682490) |
| Prize Delivery Failure in Rapid Referral | Prize Management | Encoding / Format | [1211256941142756](https://app.asana.com/1/1184020052539844/task/1211256941142756) |
| Reduced Recipient Count in Scheduled Sma | Segment | Data Inconsistency | [1213115186501137](https://app.asana.com/1/1184020052539844/task/1213115186501137) |
| Segment Update Failure in MAAC | Segment | Other Root Cause | [1212760165483455](https://app.asana.com/1/1184020052539844/task/1212760165483455) |
| Unexpected Segment Calculation Results | Segment | Other Root Cause | [1212084549273717](https://app.asana.com/1/1184020052539844/task/1212084549273717) |
| Unexpected MAAC Segment Count Discrepanc | Segment | Other Root Cause | [1212084549273694](https://app.asana.com/1/1184020052539844/task/1212084549273694) |

### P2 Issues (81)

| Issue | Module | Root Cause | Asana |
|-------|--------|-----------|-------|
| Auto-Reply Trigger Failure on Facebook M | Auto-reply | Config / Permission | [1213145171671763](https://app.asana.com/1/1184020052539844/task/1213145171671763) |
| Keyword Case Sensitivity Issue in MAAC A | Auto-reply | Other Root Cause | [1213109852110296](https://app.asana.com/1/1184020052539844/task/1213109852110296) |
| Auto-Reply Delays and Failures in Specif | Auto-reply | Other Root Cause | [1212806889218671](https://app.asana.com/1/1184020052539844/task/1212806889218671) |
| Keyword Auto-Reply Trigger Issue on Inst | Auto-reply | Config / Permission | [1212740607334933](https://app.asana.com/1/1184020052539844/task/1212740607334933) |
| Image Carousel Addition Failure in Auto- | Auto-reply | Config / Permission | [1212516260073008](https://app.asana.com/1/1184020052539844/task/1212516260073008) |
| Auto-Reply Failure on Instagram | Auto-reply | User Misunderstanding | [1212278988595118](https://app.asana.com/1/1184020052539844/task/1212278988595118) |
| Anomalous Data in Auto Reply Feature | Auto-reply | Other Root Cause | [1212207746495315](https://app.asana.com/1/1184020052539844/task/1212207746495315) |
| Auto-Reply Editing Failure in MAAC Syste | Auto-reply | Other Root Cause | [1212084549446863](https://app.asana.com/1/1184020052539844/task/1212084549446863) |
| Error Code and Content Loss During Editi | Auto-reply | Other Root Cause | [1211990876371633](https://app.asana.com/1/1184020052539844/task/1211990876371633) |
| Display Name Issue for New OA Contacts | Auto-reply | External API Dep | [1211975651294654](https://app.asana.com/1/1184020052539844/task/1211975651294654) |
| Unexpected Automated Reply in MAAC Syste | Auto-reply | External API Dep | [1211730242249302](https://app.asana.com/1/1184020052539844/task/1211730242249302) |
| Image Display Issue in MAAC Auto-Reply o | Auto-reply | Other Root Cause | [1211658874580570](https://app.asana.com/1/1184020052539844/task/1211658874580570) |
| Google Maps Link Display Issue in MAAC A | Auto-reply | Encoding / Format | [1211529952491962](https://app.asana.com/1/1184020052539844/task/1211529952491962) |
| Keyword Auto-Reply Failure in MAAC Syste | Auto-reply | Webhook / Sync Delay | [1211518547270482](https://app.asana.com/1/1184020052539844/task/1211518547270482) |
| Auto-Reply Discrepancy in MAAC Settings | Auto-reply | Webhook / Sync Delay | [1211405329420293](https://app.asana.com/1/1184020052539844/task/1211405329420293) |
| Missing Tag Application for New Contacts | Auto-reply | Other Root Cause | [1211383189088844](https://app.asana.com/1/1184020052539844/task/1211383189088844) |
| Image Display Issues in Facebook Messeng | Auto-reply | Other Root Cause | [1211289255692411](https://app.asana.com/1/1184020052539844/task/1211289255692411) |
| Deeplink Redirection Failure in Meta Aut | Auto-reply | Quota / Limit | [1210875549357676](https://app.asana.com/1/1184020052539844/task/1210875549357676) |
| Auto Reply Functionality Failure | Auto-reply | External API Dep | [1210776362195812](https://app.asana.com/1/1184020052539844/task/1210776362195812) |
| Deeplink Redirection Issue on Facebook A | Deeplink | External API Dep | [1213079624870420](https://app.asana.com/1/1184020052539844/task/1213079624870420) |
| CLID Missing During Deep Link Transition | Deeplink | External API Dep | [1213035004023053](https://app.asana.com/1/1184020052539844/task/1213035004023053) |
| Message Delivery Failure in Customer Jou | Deeplink | Quota / Limit | [1212011516046540](https://app.asana.com/1/1184020052539844/task/1212011516046540) |
| Missing Coupon Delivery via Deeplink | Deeplink | Other Root Cause | [1211818239155742](https://app.asana.com/1/1184020052539844/task/1211818239155742) |
| Message Delivery Failure in Customer Jou | Deeplink | Quota / Limit | [1211728764247261](https://app.asana.com/1/1184020052539844/task/1211728764247261) |
| Deep Link Failure in Facebook Environmen | Deeplink | External API Dep | [1211658876963521](https://app.asana.com/1/1184020052539844/task/1211658876963521) |
| Deeplink Redirect Failure in Facebook Me | Deeplink | External API Dep | [1211476033978693](https://app.asana.com/1/1184020052539844/task/1211476033978693) |
| Message Delivery Failure in Customer Jou | Deeplink | Quota / Limit | [1211405329420306](https://app.asana.com/1/1184020052539844/task/1211405329420306) |
| Archived Deep Link Content Display for N | Deeplink | External API Dep | [1211368444546388](https://app.asana.com/1/1184020052539844/task/1211368444546388) |
| Message Delivery Failure in Customer Jou | Deeplink | Quota / Limit | [1211368348898205](https://app.asana.com/1/1184020052539844/task/1211368348898205) |
| Android Incompatibility with MAAC Referr | Deeplink | External API Dep | [1211356153706723](https://app.asana.com/1/1184020052539844/task/1211356153706723) |
| Deeplink Functionality in TikTok Ads | Deeplink | Resource Constraint | [1211292942830085](https://app.asana.com/1/1184020052539844/task/1211292942830085) |
| Message Delivery Failure in Customer Jou | Deeplink | Quota / Limit | [1211168364860701](https://app.asana.com/1/1184020052539844/task/1211168364860701) |
| Data Discrepancy in Deeplink Reports | Insight | Data Inconsistency | [1212213023126579](https://app.asana.com/1/1184020052539844/task/1212213023126579) |
| Discrepancy in Customer ID Binding Rates | Insight | Data Inconsistency | [1212207562464141](https://app.asana.com/1/1184020052539844/task/1212207562464141) |
| Data Discrepancy in MAAC Acquisition Das | Insight | Data Pipeline Failure | [1211976775930269](https://app.asana.com/1/1184020052539844/task/1211976775930269) |
| Unresponsive "View Send Record" Button i | Insight | Config / Permission | [1211780759562084](https://app.asana.com/1/1184020052539844/task/1211780759562084) |
| Incorrect Auto-Reply Name in Weekly Repo | Insight | Webhook / Sync Delay | [1211693894670618](https://app.asana.com/1/1184020052539844/task/1211693894670618) |
| Non-Unique Click Counts in Broadcast Mes | Insight | By Design | [1211518421816701](https://app.asana.com/1/1184020052539844/task/1211518421816701) |
| Zero Tag Coverage on Insight Page for Al | Insight | Data Pipeline Failure | [1211426159186280](https://app.asana.com/1/1184020052539844/task/1211426159186280) |
| Discrepancy in Customer ID Binding Rate  | Insight | Other Root Cause | [1211358426495869](https://app.asana.com/1/1184020052539844/task/1211358426495869) |
| Membership Binding Anomalies in Data Ins | Insight | Data Pipeline Failure | [1211356786872970](https://app.asana.com/1/1184020052539844/task/1211356786872970) |
| Open Rate Hotspot Discrepancies in MAAC  | Insight | Webhook / Sync Delay | [1211353841908307](https://app.asana.com/1/1184020052539844/task/1211353841908307) |
| Mapping Count Recognition Failure for Cu | Insight | Data Pipeline Failure | [1211314354463888](https://app.asana.com/1/1184020052539844/task/1211314354463888) |
| Auto-Reply Ranking Display in Insight Re | Insight | Config / Permission | [1211298009313561](https://app.asana.com/1/1184020052539844/task/1211298009313561) |
| Message Discrepancy Between MAAC and LIN | Insight | Data Inconsistency | [1211285609853706](https://app.asana.com/1/1184020052539844/task/1211285609853706) |
| "Limit Reached" Message and Prize Non-re | Prize Management | Other Root Cause | [1212713603195744](https://app.asana.com/1/1184020052539844/task/1212713603195744) |
| Repeated Prize Redemption in JCB Event | Prize Management | Other Root Cause | [1212148507497017](https://app.asana.com/1/1184020052539844/task/1212148507497017) |
| Unresponsive Redemption Voucher Click in | Prize Management | Other Root Cause | [1211530080882418](https://app.asana.com/1/1184020052539844/task/1211530080882418) |
| Prize Stock Alert Notifications Despite  | Prize Management | Webhook / Sync Delay | [1211310614292818](https://app.asana.com/1/1184020052539844/task/1211310614292818) |
| Incorrect Rich Menu Tagging After Contac | Rich Menu | External API Dep | [1211803131074457](https://app.asana.com/1/1184020052539844/task/1211803131074457) |
| CID Field Data Discrepancy in Segment Ex | Segment | Data Inconsistency | [1213076444939189](https://app.asana.com/1/1184020052539844/task/1213076444939189) |
| Segment Update Failure in MAAC System | Segment | Other Root Cause | [1212739151110360](https://app.asana.com/1/1184020052539844/task/1212739151110360) |
| Identical Contact Numbers Across Differe | Segment | Config / Permission | [1212714239759016](https://app.asana.com/1/1184020052539844/task/1212714239759016) |
| Smart Sending Suspension Request | Segment | Data Pipeline Failure | [1212617985199028](https://app.asana.com/1/1184020052539844/task/1212617985199028) |
| Zero Data in High Purchase Probability L | Segment | Config / Permission | [1212543508010702](https://app.asana.com/1/1184020052539844/task/1212543508010702) |
| Segment Data Export Format Changes | Segment | Other Root Cause | [1212465993341273](https://app.asana.com/1/1184020052539844/task/1212465993341273) |
| AI Segment Displaying Zero Results | Segment | Other Root Cause | [1212277836186691](https://app.asana.com/1/1184020052539844/task/1212277836186691) |
| GA Tracking Failure in MAAC EC-Features | Segment | Config / Permission | [1212252476377404](https://app.asana.com/1/1184020052539844/task/1212252476377404) |
| Audience Exclusion Limit Reached in MAAC | Segment | User Misunderstanding | [1212212478568915](https://app.asana.com/1/1184020052539844/task/1212212478568915) |
| Unexpected Segment Filtering Results | Segment | Webhook / Sync Delay | [1212086489143431](https://app.asana.com/1/1184020052539844/task/1212086489143431) |
| Inaccurate AI Segment Creation | Segment | Other Root Cause | [1212000598445419](https://app.asana.com/1/1184020052539844/task/1212000598445419) |
| AI Segmentation Failure in Broadcast | Segment | Other Root Cause | [1211919837362932](https://app.asana.com/1/1184020052539844/task/1211919837362932) |
| Limited Broadcast Reach in MAAC System | Segment | External API Dep | [1211818294292311](https://app.asana.com/1/1184020052539844/task/1211818294292311) |
| Discrepancy in MAAC Segment Import Count | Segment | Other Root Cause | [1209226325083447](https://app.asana.com/1/1184020052539844/task/1209226325083447) |
| AI Segment Results Discrepancy in Insurv | Segment | Webhook / Sync Delay | [1211648131247953](https://app.asana.com/1/1184020052539844/task/1211648131247953) |
| Anomalous Segment Count in MAAC-Segment | Segment | Data Pipeline Failure | [1211285615645748](https://app.asana.com/1/1184020052539844/task/1211285615645748) |
| Upload Failure in MAAC-Segment | Segment | Quota / Limit | [1210376434573383](https://app.asana.com/1/1184020052539844/task/1210376434573383) |
| Tagging Failure After Clicking Broadcast | Tag Manager | Webhook / Sync Delay | [1212314620645881](https://app.asana.com/1/1184020052539844/task/1212314620645881) |
| Tag Discrepancy Between MAAC and Emarsys | Tag Manager | Data Inconsistency | [1211876667612502](https://app.asana.com/1/1184020052539844/task/1211876667612502) |
| Irregular Tag Synchronization from CAAC  | Tag Manager | Webhook / Sync Delay | [1211802724129394](https://app.asana.com/1/1184020052539844/task/1211802724129394) |
| Tag Reappearance in MAAC System | Tag Manager | Config / Permission | [1211669157227422](https://app.asana.com/1/1184020052539844/task/1211669157227422) |
| Discrepancy in Tag List and Deep Link Da | Tag Manager | Data Inconsistency | [1211622605919662](https://app.asana.com/1/1184020052539844/task/1211622605919662) |
| Tag Addition Delay in MAAC Contact List | Tag Manager | Webhook / Sync Delay | [1211575001403892](https://app.asana.com/1/1184020052539844/task/1211575001403892) |
| Unexpected Tag Appearance in MAAC | Tag Manager | User Misunderstanding | [1211528743341634](https://app.asana.com/1/1184020052539844/task/1211528743341634) |
| Extended Tag Deletion Time in MAAC-Tag | Tag Manager | By Design | [1211222283206634](https://app.asana.com/1/1184020052539844/task/1211222283206634) |
| Tag Disappearance After Name Change in M | Tag Manager | Other Root Cause | [1210638961172045](https://app.asana.com/1/1184020052539844/task/1210638961172045) |
| Broadcast Delivery Failure to Active Con | Template Library | User Misunderstanding | [1211557302787615](https://app.asana.com/1/1184020052539844/task/1211557302787615) |
| Why Can't Users Open MAAC Deeplinks from | Tracelink | By Design | [1211978338514071](https://app.asana.com/1/1184020052539844/task/1211978338514071) |
| Reauthorization Process for Existing LIN | Tracelink | Cache / State Issue | [1211847487255320](https://app.asana.com/1/1184020052539844/task/1211847487255320) |
| Inconsistent Page Redirection in MAAC Ri | Tracelink | Data Inconsistency | [1211713182842659](https://app.asana.com/1/1184020052539844/task/1211713182842659) |
| Safari Incompatibility with MAAC Trackin | Tracelink | Other Root Cause | [1211379820597016](https://app.asana.com/1/1184020052539844/task/1211379820597016) |

### P3 Issues (8)

| Issue | Module | Root Cause | Asana |
|-------|--------|-----------|-------|
| Message Delivery Failure in Instagram Au | Auto-reply | Config / Permission | [1213115186501125](https://app.asana.com/1/1184020052539844/task/1213115186501125) |
| Discrepancy in Message Count Between MAA | Insight | Other Root Cause | [1212736080583740](https://app.asana.com/1/1184020052539844/task/1212736080583740) |
| Sudden Tag Coverage Drop to Zero | Insight | Data Pipeline Failure | [1212602245683188](https://app.asana.com/1/1184020052539844/task/1212602245683188) |
| Button Selection Failure in Segment Filt | Segment | Other Root Cause | [1212803690945957](https://app.asana.com/1/1184020052539844/task/1212803690945957) |
| Unexpected Segment Count Discrepancy | Segment | Data Inconsistency | [1212821275473949](https://app.asana.com/1/1184020052539844/task/1212821275473949) |
| Contact Tag Order in MAAC Interface | Tag Manager | Data Inconsistency | [1212526242255975](https://app.asana.com/1/1184020052539844/task/1212526242255975) |
| ID Binding Failure via CLID in MAAC Trac | Tracelink | Config / Permission | [1213035004023033](https://app.asana.com/1/1184020052539844/task/1213035004023033) |
| LIFF Opening Failure Due to External Red | Tracelink | Cache / State Issue | [1212486166756322](https://app.asana.com/1/1184020052539844/task/1212486166756322) |

### P4 Issues (7)

| Issue | Module | Root Cause | Asana |
|-------|--------|-----------|-------|
| Deeplink Display Failure in Customer Onb | Deeplink | Config / Permission | [1212585827993386](https://app.asana.com/1/1184020052539844/task/1212585827993386) |
| Button Visibility Issue on Small-Screen  | Deeplink | Other Root Cause | [1212400140357443](https://app.asana.com/1/1184020052539844/task/1212400140357443) |
| Discrepancy in Acquired New Contacts Bet | Insight | Data Inconsistency | [1212791162159401](https://app.asana.com/1/1184020052539844/task/1212791162159401) |
| Incorrect Localization in Prize Status L | Prize Management | Other Root Cause | [1212577017707300](https://app.asana.com/1/1184020052539844/task/1212577017707300) |
| "NaN" Display in Contact List Export | Segment | Other Root Cause | [1212543257591550](https://app.asana.com/1/1184020052539844/task/1212543257591550) |
| Tracelink Redirection to Welcome Message | Tracelink | Encoding / Format | [1212716056060047](https://app.asana.com/1/1184020052539844/task/1212716056060047) |
| Incorrect URL Generation in MAAC-Traceli | Tracelink | Other Root Cause | [1212440779412548](https://app.asana.com/1/1184020052539844/task/1212440779412548) |

## 8. Attribution Chains

These chains show how root causes propagate through the system.
Format: `Root Cause → Issue → Module → Product`

### Other Root Cause
- `Other Root Cause` → `Discrepancy in Message Count Between MAA` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212736080583740)
- `Other Root Cause` → `Discrepancy in Customer ID Binding Rate ` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211358426495869)
- `Other Root Cause` → `Button Selection Failure in Segment Filt` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212803690945957)
- `Other Root Cause` → `Segment Update Failure in MAAC` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212760165483455)
- `Other Root Cause` → `Segment Update Failure in MAAC System` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212739151110360)
- `Other Root Cause` → `"NaN" Display in Contact List Export` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212543257591550)
- `Other Root Cause` → `Segment Data Export Format Changes` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212465993341273)
- `Other Root Cause` → `AI Segment Displaying Zero Results` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212277836186691)
- `Other Root Cause` → `Unexpected Segment Calculation Results` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212084549273717)
- `Other Root Cause` → `Unexpected MAAC Segment Count Discrepanc` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212084549273694)
- `Other Root Cause` → `Inaccurate AI Segment Creation` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212000598445419)
- `Other Root Cause` → `AI Segmentation Failure in Broadcast` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211919837362932)
- `Other Root Cause` → `Discrepancy in MAAC Segment Import Count` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1209226325083447)
- `Other Root Cause` → `Tag Disappearance After Name Change in M` → `Tag Manager` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1210638961172045)
- `Other Root Cause` → `Keyword Case Sensitivity Issue in MAAC A` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1213109852110296)
- ... +16 more

### Config / Permission
- `Config / Permission` → `Unresponsive "View Send Record" Button i` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211780759562084)
- `Config / Permission` → `Auto-Reply Ranking Display in Insight Re` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211298009313561)
- `Config / Permission` → `Identical Contact Numbers Across Differe` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212714239759016)
- `Config / Permission` → `Zero Data in High Purchase Probability L` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212543508010702)
- `Config / Permission` → `GA Tracking Failure in MAAC EC-Features` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212252476377404)
- `Config / Permission` → `Tag Reappearance in MAAC System` → `Tag Manager` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211669157227422)
- `Config / Permission` → `Auto-Reply Trigger Failure on Facebook M` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1213145171671763)
- `Config / Permission` → `Message Delivery Failure in Instagram Au` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1213115186501125)
- `Config / Permission` → `Keyword Auto-Reply Trigger Issue on Inst` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212740607334933)
- `Config / Permission` → `Image Carousel Addition Failure in Auto-` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212516260073008)
- `Config / Permission` → `Deeplink Display Failure in Customer Onb` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212585827993386)
- `Config / Permission` → `ID Binding Failure via CLID in MAAC Trac` → `Tracelink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1213035004023033)

### Data Inconsistency
- `Data Inconsistency` → `Discrepancy in Acquired New Contacts Bet` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212791162159401)
- `Data Inconsistency` → `Data Discrepancy in Deeplink Reports` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212213023126579)
- `Data Inconsistency` → `Discrepancy in Customer ID Binding Rates` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212207562464141)
- `Data Inconsistency` → `Message Discrepancy Between MAAC and LIN` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211285609853706)
- `Data Inconsistency` → `Reduced Recipient Count in Scheduled Sma` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1213115186501137)
- `Data Inconsistency` → `Contact Discrepancy in LINE Segment` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1213084606836149)
- `Data Inconsistency` → `CID Field Data Discrepancy in Segment Ex` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1213076444939189)
- `Data Inconsistency` → `Unexpected Segment Count Discrepancy` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212821275473949)
- `Data Inconsistency` → `Contact Tag Order in MAAC Interface` → `Tag Manager` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212526242255975)
- `Data Inconsistency` → `Tag Discrepancy Between MAAC and Emarsys` → `Tag Manager` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211876667612502)
- `Data Inconsistency` → `Discrepancy in Tag List and Deep Link Da` → `Tag Manager` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211622605919662)
- `Data Inconsistency` → `Inconsistent Page Redirection in MAAC Ri` → `Tracelink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211713182842659)

### External API Dep
- `External API Dep` → `Limited Broadcast Reach in MAAC System` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211818294292311)
- `External API Dep` → `Incorrect Rich Menu Tagging After Contac` → `Rich Menu` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211803131074457)
- `External API Dep` → `Display Name Issue for New OA Contacts` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211975651294654)
- `External API Dep` → `Unexpected Automated Reply in MAAC Syste` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211730242249302)
- `External API Dep` → `Auto Reply Functionality Failure` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1210776362195812)
- `External API Dep` → `Deeplink Redirection Issue on Facebook A` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1213079624870420)
- `External API Dep` → `CLID Missing During Deep Link Transition` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1213035004023053)
- `External API Dep` → `Deep Link Failure in Facebook Environmen` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211658876963521)
- `External API Dep` → `Deeplink Redirect Failure in Facebook Me` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211476033978693)
- `External API Dep` → `Archived Deep Link Content Display for N` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211368444546388)
- `External API Dep` → `Android Incompatibility with MAAC Referr` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211356153706723)

### Data Pipeline Failure
- `Data Pipeline Failure` → `Zero Tag Coverage in MAAC Data Insights` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1213185386062836)
- `Data Pipeline Failure` → `Sudden Tag Coverage Drop to Zero` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212602245683188)
- `Data Pipeline Failure` → `Missing Data in Data Insights Report for` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212601716064139)
- `Data Pipeline Failure` → `Data Discrepancy in MAAC Acquisition Das` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211976775930269)
- `Data Pipeline Failure` → `Zero Tag Coverage on Insight Page for Al` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211426159186280)
- `Data Pipeline Failure` → `Membership Binding Anomalies in Data Ins` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211356786872970)
- `Data Pipeline Failure` → `Mapping Count Recognition Failure for Cu` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211314354463888)
- `Data Pipeline Failure` → `Data Insights Display Anomalies in Multi` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1213131750073052)
- `Data Pipeline Failure` → `Smart Sending Suspension Request` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212617985199028)
- `Data Pipeline Failure` → `Anomalous Segment Count in MAAC-Segment` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211285615645748)

### Webhook / Sync Delay
- `Webhook / Sync Delay` → `Incorrect Auto-Reply Name in Weekly Repo` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211693894670618)
- `Webhook / Sync Delay` → `Open Rate Hotspot Discrepancies in MAAC ` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211353841908307)
- `Webhook / Sync Delay` → `Unexpected Segment Filtering Results` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212086489143431)
- `Webhook / Sync Delay` → `AI Segment Results Discrepancy in Insurv` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211648131247953)
- `Webhook / Sync Delay` → `Tagging Failure After Clicking Broadcast` → `Tag Manager` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212314620645881)
- `Webhook / Sync Delay` → `Irregular Tag Synchronization from CAAC ` → `Tag Manager` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211802724129394)
- `Webhook / Sync Delay` → `Tag Addition Delay in MAAC Contact List` → `Tag Manager` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211575001403892)
- `Webhook / Sync Delay` → `Keyword Auto-Reply Failure in MAAC Syste` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211518547270482)
- `Webhook / Sync Delay` → `Auto-Reply Discrepancy in MAAC Settings` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211405329420293)
- `Webhook / Sync Delay` → `Prize Stock Alert Notifications Despite ` → `Prize Management` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211310614292818)

### User Misunderstanding
- `User Misunderstanding` → `Audience Exclusion Limit Reached in MAAC` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212212478568915)
- `User Misunderstanding` → `Unexpected Tag Appearance in MAAC` → `Tag Manager` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211528743341634)
- `User Misunderstanding` → `Broadcast Delivery Failure to Active Con` → `Template Library` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211557302787615)
- `User Misunderstanding` → `Auto-Reply Failure on Instagram` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212278988595118)

### By Design
- `By Design` → `Non-Unique Click Counts in Broadcast Mes` → `Insight` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211518421816701)
- `By Design` → `Extended Tag Deletion Time in MAAC-Tag` → `Tag Manager` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211222283206634)
- `By Design` → `Why Can't Users Open MAAC Deeplinks from` → `Tracelink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211978338514071)

### Quota / Limit
- `Quota / Limit` → `Upload Failure in MAAC-Segment` → `Segment` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1210376434573383)
- `Quota / Limit` → `Deeplink Redirection Failure in Meta Aut` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1210875549357676)
- `Quota / Limit` → `Message Delivery Failure in Customer Jou` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212011516046540)
- `Quota / Limit` → `Message Delivery Failure in Customer Jou` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211728764247261)
- `Quota / Limit` → `Message Delivery Failure in Customer Jou` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211405329420306)
- `Quota / Limit` → `Message Delivery Failure in Customer Jou` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211368348898205)
- `Quota / Limit` → `Message Delivery Failure in Customer Jou` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211168364860701)

### Encoding / Format
- `Encoding / Format` → `Google Maps Link Display Issue in MAAC A` → `Auto-reply` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211529952491962)
- `Encoding / Format` → `Tracelink Redirection to Welcome Message` → `Tracelink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212716056060047)
- `Encoding / Format` → `Prize Delivery Failure in Rapid Referral` → `Prize Management` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211256941142756)

### Cache / State Issue
- `Cache / State Issue` → `LIFF Opening Failure Due to External Red` → `Tracelink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1212486166756322)
- `Cache / State Issue` → `Reauthorization Process for Existing LIN` → `Tracelink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211847487255320)

### Resource Constraint
- `Resource Constraint` → `Deeplink Functionality in TikTok Ads` → `Deeplink` → MAAC | [Asana](https://app.asana.com/1/1184020052539844/task/1211292942830085)

## 9. Quick Reference — Impact Analysis Guide

When evaluating a change to any component, use this guide:

| If you change... | Check impact on... |
|------------------|-------------------|
| **Auto-reply** | Contacts, Template Library, LINE API, Meta API |
| **Broadcast** | Insight, Segment, Template Library, Customer Journey, LINE API |
| **Contacts** | Segment, Customer Journey, Tag Manager, Deeplink, Auto-reply, LINE API, PostgreSQL |
| **Customer Journey** | Broadcast, Tag Manager, Segment, Contacts, SendGrid, Airflow |
| **Deeplink** | Contacts, Insight, Tracelink, Rich Menu, LIFF |
| **Insight** | Deeplink, Broadcast, Airflow, BigQuery, PostgreSQL |
| **Prize Management** | LINE API |
| **Rich Menu** | Deeplink, LINE API |
| **Segment** | Broadcast, Contacts, Tag Manager, Customer Journey, BigQuery |
| **Tag Manager** | Segment, Contacts, Customer Journey, PostgreSQL |
| **Template Library** | Broadcast, Auto-reply |
| **Tracelink** | Deeplink, LIFF, Redis |

---

*End of Knowledge Graph Document*