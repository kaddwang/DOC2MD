# Document Specification
- **Original Source:** PRD - Auto-reply opt. (time & reply limit & duplicate).docx
- **Document Type:** Technical Specification
- **Language:** English (Translated from Chinese)
---

# Auto-reply Optimization: Time, Reply Limit, and Duplicate

## Project Overview

- **PM Owner:** Lydia Hou (previous: Jenny)
- **Engineering Owner:** Jhenyi Jhan
- **Product Design Owner:** Johny Hsieh
- **Communication Channels:** 
  - Slack: #proj-auto-reply-opt
  - Asana
  - Notion

## Version History

| Version | Date       | Description                                                                 | Editor |
|---------|------------|-----------------------------------------------------------------------------|--------|
| 0       | 2023.01.02 | Initial version                                                             | Jenny  |
| 0.1     | 2023.02.06 | Added design handoff, updated auto-reply by scheduled time, added auto-reply list | Jenny  |
| 1.1     | 2023.02.17 | Added auto-reply triggered by picked day setting                            | Jenny  |
| 1.2     | 2024.07.05 | PRD restructure                                                             | Lydia  |
| 1.3     | 2024.08.23 | Rescoping: Time, reply limit, and duplicate                                 | Lydia  |
| 1.4     | 2024.11.12 | Added next-day setting logic                                                | Lydia  |

## Release Notes

We are excited to introduce new enhancements to our auto-reply feature, designed to improve user experience and flexibility.

- **Trigger with Time Interval - Recurring:** We now offer daily and weekly recurring triggers for auto-replies, to unblock the reply scenario during weekends.
- **Reply Limit:** To prevent user annoyance, you can limit the number of times an auto-reply is sent within a specified period (minutes, hours, days).

These updates aim to provide more control and customization for your auto-reply settings.

## Out of 2024.Q3 Scope

- **Schedule Auto-reply:** Users can now schedule auto-replies to auto-activate with specific start and end times. If only the end time is set, the auto-reply activates immediately and ends at the specified time. If only the start time is set, it activates at the start time without an automatic end.
- **Trigger with Time Interval - Specific Time Period:** We now offer daily recurring, weekly recurring, and specific date triggers for auto-replies, with a detailed prioritization system.
- **Trigger Rules with Content Rule - Keywords:** Support for multiple sets of keywords (up to 30), with options for exact match and case-insensitive partial match.

## Background

### Existing Feature

Since it’s an optimization feature, let me introduce the overall existing feature and logic first:

- **Auto-reply List:**
  - Tabs: All, Keyword, Specific Time, Welcome Message, Archived
  - Columns: Auto-reply (with activate button), Trigger Rule, Total Triggers/Sent, CTR, Orders, Revenue
- **Auto-reply Setting:**
  - Name
  - Trigger Rule (Keyword, Time Interval, Welcome)
  - Tag
  - Message for Unbound/Bound Contacts

### Existing Pain Points & Business Impact

After we have an overview of existing features, let’s get aware of current users’ pain points:

#### Main Problems to be Solved:

- Weekly and specific date period setting for specific time auto-reply
- Flexible setting for sales/service to reply in non-business hours
- Easy setup for marketers to run auto-reply campaigns during holidays
- Limitation on auto-reply trigger times to prevent bothering consumers

#### Business Impact:

If we could solve 4 requirements which 27 clients mentioned before, this will bring us 716,066 MRR with 439,844 priority (considering brands’ care %).

| Requirement ID | Description                                                                 | # of Brands | MRR     | Priority  |
|----------------|-----------------------------------------------------------------------------|-------------|---------|-----------|
| RC00037        | Auto-reply can set up daily, weekly, and specific date period with timespan | 13          | 336,331 | 211,406.6 |
| RC00010        | Multiple keyword triggers one Auto-reply                                    | 11          | 325,351 | 195,033.6 |
| RC00407        | "Auto-reply within specified time interval" can limit trigger frequency     | 2           | 28,159  | 28,159.0  |
| RC00036        | Auto-reply can add scheduling functions                                     | 1           | 26,225  | 5,245.0   |
| **Total**      |                                                                             | **27**      | **716,066** | **439,844.2** |

## Auto-reply Component Level and Concept

- **Operating Schedule:**
  - Auto-reply auto-activate or deactivate time
- **Trigger with Time Interval:**
  - Recurring: daily/weekly/monthly
  - Specific time period
- **Trigger with Content Rule:**
  - Welcome message
  - Keyword message
  - Any content
- **Reply Limit:**
  - 1 time in [N] [hours/days]

## Scope

### Within Scope

To solve current pain points, we need to:

- Support “time interval with recurring” as an advanced optimization
- Support “reply limit” as a general setting for all kinds of auto-reply triggers

#### Prioritized Features:

- A - Reply Type and Scheduling
- C - Reply Limit
- D - Duplicate
- F - Reply Hours

#### Related Adjustments:

- G - List Adjustment
- H - Before and After for Existing Clients Default

### Out of Scope

Since auto-reply revamp is not in the 2024 and 2025 revamp plan, we won’t directly plan details of the revamp plan in this PRD, e.g.:

- Auto-reply to support multichannel
- Journey include auto-reply
- Provide category for auto-reply

2024.08.23 after understanding the effort estimation, we decided to refine the scope, and below is not in scope:

- A - Trigger with Time Interval - Specific Time Period
- B - Trigger with Content Rule - Keywords
- E - Operating Schedule Feature (auto-activate)

## User Story

- As a store owner, I want to set auto-reply by weekday, so I don’t have to manually change the settings weekly when the routing close day is coming.
- As a marketer, I want to set auto-reply for holidays or marketing campaigns at one time, so I don’t need to manually change settings after the holiday or marketing campaign ends.
- As a marketer, I want to flexibly set multiple keywords for triggering auto-reply, so that I won’t have to set a lot of auto-reply but answer for the same campaign content. (Conditions: Contains any keyword / Contains all keywords / Exact match.)
- As a marketer, I want to pre-build and schedule the auto-reply campaign before the weekend, so that I won’t have to activate the auto-reply during my weekend time.

## Metrics & Key Results

### Goal: Improve NDR by Solving High-request Requirements

#### Success Criteria:

- **Adoption:** 20% of clients adopt the business hour setting and apply to auto-reply
  - 76 out of 307 (24.76%) time scheduled auto-reply is about offline hours notification. Assume 50% need different settings for weekdays from weekends, about 12%.
  - Use business hour setting to solve the user scenario who need different auto-reply for weekdays and weekends. 25% time scheduled auto-reply is about offline hours notification. Assume 80% need different settings for weekdays from weekends, about 20%.
  - Change success metric from 12% WAU of newly added trigger types (recurring) to 20% auto-reply client adopt business hour setting

- **Satisfaction:** 80% of clients satisfied with the auto-reply opt.
  - 2024/09/19 meeting: Set Userflow with simple satisfaction form to investigate whether solve user’s pain point, and gain feedback as an ingredient for 2025 auto-reply opt.
  - 2024/11/18: Ask CS to directly collect feedback from clients, to verify our assumption when building the auto-reply optimization.

#### Other Metrics - Usage:

- # of auto-reply using welcome/keyword/general trigger type
- # of keyword auto-reply with specific time period
- # of general auto-reply with daily/reply hours/monthly
- # of auto-reply with reply limit setting
- # of auto-reply with duplicate function

## Raw Data Table

### Auto-reply Setting

- Org_id
- Auto reply id
- Auto reply name
- Trigger type: welcome/keyword/general
- Keyword: with specific time period
- General: with daily/reply hours/monthly
- Reply limit setting

### Auto-reply Performance

- Org_id
- Auto reply id
- Auto reply name
- TTL triggers: existing contact - unbound/bound
- TTL msg sent: existing contact - unbound/bound
- Performance: Clicks, Items add to cart, Orders, Revenue

### Reply Hour

- Org_id
- Reply hour setting

### Trigger Record

- Org_id, bot_id
- LINE_uid
- Auto reply id
- Auto reply name
- Time stamp

## Feature Specification

### A - Reply Type and Scheduling

|                  | Welcome | Keyword                                      | General Reply                             |
|------------------|---------|----------------------------------------------|-------------------------------------------|
| Scheduling       | X       | No specified date range <br> Specified date range | Monthly <br> Based on reply hours/non-reply hours <br> Daily with time-setting |
| Setting Rule     | X       | Cannot set same name keyword, even if deactivated | Monthly: <br> Choose at most 5 dates with same time period <br> Cannot set the same date of other monthly auto-reply <br> Reply hours: will be in Business hours setting in Organization setting (Details see F. reply hour) |

#### Trigger Prioritization

- **Trigger Rule:**
  - Welcome: happens when a new friend joins LINE OA
  - Keywords > General Reply

- **Scheduling:**
  - Recurring-Monthly > Reply Hours > Recurring-Daily

- **Scheduling Edit Rule:**
  - Once complete, cannot be edited.
  - Logic: For clear reporting, to decrease confusion if edit the timing. Users could use “Duplicate” for any adjustment.

#### The Time Picker Details

- All day as default -> When users choose “all day”, time picker will be set 00:00-23:59 automatically
- 24-hour time format
- Separate “hour” and “minute” in the menu
- Time period granularity: minute

### (X) B - Trigger with Content Rule - Keywords

2024.09.19 moved to

### C - Reply Limit

To support the “reply limit” feature which allows the user to receive the same auto-reply not exceeding a certain number of times to prevent bothering users.

#### Logic:

- This rule is optional; users could decide whether to turn on this setting.

#### Solution:

- 1 time in [N] [hours/days], the upper limit is 999
- UI reference: Beacon Do-not-disturb interval

### D - Duplicate

**Context:**

Currently, clients cannot edit the auto-reply trigger rule, such as editing the keyword, after publishing an auto-reply because it affects report performance. With the support for multiple keywords, this inconvenience will increase significantly. Here is the proposed solution.

**Solution:**

- Support a "Make a copy" feature in the auto-reply list.
- When the user clicks "Make a copy," the system will automatically duplicate the auto-reply with:
  - Auto-reply name appended with "_copy"
  - Keyword appended with "_copy"
  - All other settings remain unchanged.

### F - Reply Hours

**Context:**

To address user scenarios requiring different auto-replies for weekdays and weekends, we will utilize business hour settings. Over 80% of use cases involve business/non-business hours auto-replies. To simplify settings and address clients' main concerns, we will provide reply/non-reply hours instead of weekly settings for each auto-reply.

**Solution:**

- Users can access the organization-level settings to view the Business hours section and set the Reply hours.
- Users can configure reply/non-reply hours based on their business hours.

### G - List Adjustment

Adjustments to the auto-reply list include:

- Change the "Trigger" column to "Reply type and Scheduling."
- **Reply type:**
  - Welcome
  - Keyword
  - General
- **Scheduling:**
  - Daily recurring: Display the time period, e.g., Daily: hh:mm - hh:mm
  - Reply hours / Non-reply hours
  - Monthly recurring: Display the selected month date, e.g., Monthly: 1st, 11th, 21st, 31st
- Change the "Specific time" tab to "General reply."

### H - Before and After for Existing Clients Default

When existing clients switch to the new feature, the default values are as follows:

| New Setting                  | Existing Setting - Welcome | Existing Setting - Keyword | Existing Setting - Time Interval |
|------------------------------|----------------------------|----------------------------|----------------------------------|
| Trigger with time interval   | off                        | off                        | Time (as setting)                |
| Trigger with content rule    | Welcome                    | Keyword                    | General reply                    |
| Reply limit                  | null                       | null                       | null                             |

### Dependency

**Release Plan**

**Timeline**

- **Milestone**
  - M1 - Reply limit & business hour: 10/1~10/14, complete testing and bug fixing by 10/17
  - M2 - Auto-reply with time: 10/17~11/12, complete testing and bug fixing by 11/15
  - M3 - Duplicate & list: 11/18~11/22, complete testing and bug fixing by 11/27

**Releasing Timeline**

- Tier 1: 11/27 15:00
- Tier 2: 12/4 15:00
- Tier 3: 12/11 15:00 → Check whether to delete this tooltip

**Tracking Data**

- Metabase

**Note**

- Logic: Since 27 clients fall into all service levels, this project will directly use service levels for tiering without selecting a specific client list.

**Pricing Plan**

- As-is, no change.

**Release Region**

- Please check the grayed-out feature list:

| TW | TH | JP |
|----|----|----|

**GTM Plan**

- **How do users adopt:** Self-serve
- **How do users troubleshoot:** Self-serve

**Development Documents**

- **Design Docs**
  - Design critique for Switch → E1 (need audit log)
- **QA Docs**

**Post Release**

- **Monitoring:** Daily check for issues within the first week (required)
- **Feedback Collection:** Collect feedback from CSM/GTM within the first 4 weeks (required)
- **Outcome & Learnings Sharing:**
  - Collect metrics results within the first 8 weeks (required)
  - Complete learnings within the first 8 weeks (required)
  - Share outcomes at monthly R&D all-hands (required)
  - Share outcomes at company all-hands (optional)
  - Share outcomes at QBR (optional)

**Next Steps**

- Complete the next steps within the first 8 weeks
- Case close

**Iteration**

**Future Plan**

- 2025.Q1: Auto-reply will be moved to the platform layer to support CAAC
- 2025.H2: Auto-reply will be integrated into the journey

### Discussion and Open Questions

**20241115 General Reply Naming Finalization**

- Fixed reply → General reply
- General reply will handle any chat content, with scheduling settings applied at the next level.
- General is more accurately translated into Japanese and Thai compared to "fixed," which may require contextual translation. "Default" implies only one set, which is not suitable.

**Proposal for Tooltip Content:**

- When auto-reply is active, it will respond under the following conditions:
  1. Welcome message for new contacts: Automatically sent when a new contact joins LINE OA.
  2. Keyword reply: Responds to specified keywords.
  3. General reply: Responds to any sent chat content.

**Scheduling Description on Setting Page:**

- If multiple auto-reply schedules overlap, the response order is monthly > reply/non-reply hours > daily.

**20241112 Reply Limit:**

- **Problem:** When the reply limit for an auto-reply is reached, should the system continue to evaluate the next auto-reply?
- **Proposal:** Do not continue evaluating the next auto-reply.
- **Logic:** The purpose of the reply limit is to prevent the auto-reply from being overly intrusive.

**20241112 Auto-reply Next-day Setting Only on Daily General Auto-reply for Now**

**Context:**

- LINE OA manager's native backend supports cross-day settings.
- Existing CL auto-reply also supports cross-day settings.

**Proposal:**

- Support cross-day settings → Daily start and end times can be any time within 24 hours (remove the requirement for the end time to be later than the start time).
- Time display format:
  - <cht> 20:00 ~ Next day 02:00
  - <ja> 20:00 ~ 翌日 02:00
  - <en> 20:00 to 2:00 am (next day)
  - <th> TBD

**Decision:**

- **Current:** Only add cross-day settings to daily general auto-reply (next-day).
- **Assumption:** The current scenario focuses on non-business hour replies, so monthly cross-day settings are not considered at this stage.
- **Future:** Continue to monitor for additional feedback. If needed, add support for multiple time intervals on a single date for monthly auto-reply (currently unable to set the same day's monthly auto-reply).

**To-do:**

- Assist in retrieving data to confirm past cross-day setting auto-replies.
- Assist in confirming cross-day time multi-language display formats.

**20241108 Auto-reply List Tooltip Metric Tracking → Check Whether to Delete This Tooltip**

**Background:** FE - Noel adjusted the list and asked PD - Johny about the layout of this tooltip.

**Process:** Broad inquiries were made to CS (Lanchi, Dash), FE (Jack, Simon), BE (JY), David, Catherine, PM (Lydia) to understand the technical architecture implications, but no consensus on user practicality was reached.

**Current Status:**

- Maintain the status quo: Tooltips accompany the title on the right.
- Add data tracking: Due to uncertainty about user usage, removing it directly may cause issues. FE added GA Tracking for observation.

**Tracking Period:** From now until the Tier release stage.

**Final Action:** By 12/11 Tier 3 release, PM will observe data and decide whether to retain or remove.

### Discussion and Alignment

- **Time Settings**: 
  - Daily, weekly settings should align with business/non-business hours.
  - Monthly settings should be considered separately.

- **Proposal**:
  - Time-based settings should be divided into two layers: Monthly > Daily, with business/non-business hours.
  - Ensure no duplication in comparisons: Monthly time, Daily time, and business/non-business hours should be compared separately.
  - List sorting should be categorized accordingly.

### Timeline

- **9/10**: Final specification adjustment and kickoff.
- **9/11**: Design proposal for recurring settings.
- **9/12**: Design discussion for recurring settings.
- **9/13 or 9/16**: Final design handoff.
- **9/9**: Lydia archived previous metric settings.

### Goals and Success Criteria

- **Goal**: Enhance the flexibility and automation of auto-reply.
- **Success Criteria**: Achieve a 12% Weekly Active Users (WAU) increase for newly added trigger types (weekly recurring + specific date).
  - Based on data: 76 out of 307 (24.76%) time-scheduled auto-replies are for offline hours notifications. Assuming 50% require different settings for weekdays vs. weekends, this equates to approximately 12%.

### Adoption and Retention Metrics

- Weekly active usage of daily recurring auto-reply.
- Weekly active usage of weekly recurring auto-reply.
- Weekly active usage of specific date auto-reply.

### Raw Data Table

- Engineering to add this section.

### Discussion Notes

- **7/29**: Lydia to document today's discussion and inform Johny, and sync with Peter.
  - Considerations for auto-reply volume per client and categorization.
  - **Questions**:
    - Is a manual switch still necessary?
    - Should time and keyword be used in combination?
  - **Edge Cases**: Consider any factors that might affect past auto-replies.
  - **Migration**: Evaluate if the old time mechanism, which applied keywords, will be cumbersome for clients. The new system should be user-friendly.
  - **Multiple Groups, Time, and Keywords**: Expand dimensions and reorganize.
  - **Order and Sorting**: Ensure logical sequence and categorization.

### Sync and Planning

- **7/30**: Sync with the project team.
  - Auto-reply coordination with Jenny.
  - Comparison with CAAC AI conversation, transitioning to MAAC then AI conversation.
  - Include problem/value analysis.
  - JP requirements learned from Soji and Yun on 7/16.

### Previous Planning

#### Daily Recurring

| Type | Daily Recurring |  |
| --- | --- | --- |
| Week | (skip) |  |
| Time Interval | (skip) |  |
| Time Period | [start] to [end] <br> All day |  |

#### Weekly Recurring

| Type | Weekly Recurring | Weekly Recurring |  |
| --- | --- | --- | --- |
| Week | M,T,W,T,F,S,S (Multiple choice) | M,T,W,T,F,S,S (Multiple choice) |  |
| Time Interval | General | Custom |  |
| Time Period | [start] to [end] <br> All day | [start] to [end] / Each <br> All day / Each |  |

#### Specific Date

| Type | Specific Date |  |
| --- | --- | --- |
| Date & Time | Select date and time interval |  |
| Add Another Date | (Optional) Add another date setting if needed <br> Maximum: 30 triggers |  |

### Archive

#### Trigger with Content Rule - Keywords

- **Previously**: Only one set of keywords with the Exact Match rule was provided.
- **Proposed**:
  - Support multiple sets of keywords, with an upper limit of 30 sets. The keyword string limitation remains at 32 characters.
  - Support both Exact Match and Partial Match.
  - **Partial Match Definition**: Includes keywords, does not include partial characters, case insensitive.
- **Keep As-Is**:
  - Cannot set the same keywords in different auto-replies.
  - Both Exact and Partial Match need to be checked, including all auto-reply statuses.
  - A pop-up reminder should indicate which auto-reply already has the same keyword.
  - If user content includes more than one keyword in different auto-replies, only the latest created auto-reply will be triggered.

#### Operating Schedule Feature (Auto-Activate)

- **Support**: 
  - Auto-activate the auto-reply with a start [date+time].
  - Auto-deactivate it with an end [date+time].
- **User Options**:
  - If the operating schedule is off, the auto-reply will not auto-activate or auto-deactivate.
  - If on, users can set either auto-activation with a start [date+time] or auto-deactivation with an end [date+time].
- **Logic**:
  - Start and end times can be empty.
  - If only the end time is filled, activate directly and end at that time.
  - If only the start time is filled, start at that time and do not auto-end.
  - Scheduled time can only be extended after publishing.
- **Time Selector**: Same as the Journey Operating Schedule.
- **Adjustment on Auto-Reply List**:
  - Manual activation/deactivation takes precedence over auto-activation/deactivation.
  - If manually activated outside operating time, a pop-up reminder will check if the user wants to reactivate the auto-reply.
  - If reactivated, turn off the operating schedule setting and activate the auto-reply.
  - Add a column to show the operating schedule set.
  - **Column Name**: Operating Schedule
  - **Column Content**:
    - yyyy-MM-dd ~ yyyy-MM-dd
    - If only start time: yyyy-MM-dd ~
    - If only end time: ~ yyyy-MM-dd

---

## Technical Diagram Descriptions

### Diagram 1

The image consists of two main components:

1. **Bar Chart:**
   - Title: Not visible, but related to "Service L..."
   - X-axis: Service Levels (L1, L2, L3, L4, L5)
   - Y-axis: Frequency (0 to 15)
   - Data:
     - L1: Approximately 5
     - L2: Approximately 5
     - L3: Approximately 15
     - L4: Approximately 5
     - L5: Approximately 1

2. **Table:**
   - Columns: Value (值), Frequency (频率)
   - Data:
     - L3: 18
     - L2: 5
     - L1: 5
     - L5: 3
     - L4: 3

The chart and table indicate that L3 has the highest frequency.

