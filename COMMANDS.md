# Tatyana — Commands

Tatyana is a Discord bot designed to help Guild Wars 2 guilds coordinate Guild Missions.

> **Status:** Work in Progress
> Commands and functionality may change as Tatyana develops.

## Guild Mission Commands

### `/mission`

Creates a Guild Mission interest check.

**Options:**

* `date` — The date of the Guild Mission in `DD/MM/YYYY` format.
* `time` — The starting time of the Guild Mission in `HH:MM` format. Times are displayed as AWST.
* `title` — An optional title for the mission.

**Example:**

```text
/mission date:30/08/2026 time:19:00 title:Guild Mission Night
```

Tatyana creates an interactive message containing:

* 📅 Mission date
* 🕐 Mission time
* 🟢 Interested button
* 🟡 Maybe button
* 🔴 Can't Attend button
* Current response totals

Members can change their response at any time by selecting another option.

---

### `/mission-attendees`

Displays the members who have responded to the current Guild Mission.

Responses are separated into:

* 🟢 Interested
* 🟡 Maybe
* 🔴 Can't Attend

This command is intended for guild organisers and may be restricted to designated guild roles.

---

## Attendance Responses

Members do not need to use a command to respond to a mission.

Instead, they can select one of the buttons on the Guild Mission message:

| Response        | Meaning                        |
| --------------- | ------------------------------ |
| 🟢 Interested   | Planning to attend             |
| 🟡 Maybe        | Unsure whether they can attend |
| 🔴 Can't Attend | Unable to attend               |

A member's most recent response replaces their previous response.

---

## Permissions

Tatyana is intended to be used by small, casual Guild Wars 2 communities.

Certain administrative commands may be restricted to designated guild roles, while regular members can still respond to Guild Mission polls.

---

## Timezone

Guild Mission times are currently displayed in **Australian Western Standard Time (AWST)**.

Support for additional timezones may be added in the future.

---

Features may be added, changed, or removed as development continues.
