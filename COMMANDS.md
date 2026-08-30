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

### `/say`

Tatyana will repeat what you say through the command while deleting the original command message sent.

<img width="729" height="247" alt="image" src="https://github.com/user-attachments/assets/c5a575dd-6897-4bee-a71f-3a311a214128" />

---

### `/update`

Displays a message with what has been typed into the source, changes made and (optional) link if needed,
<img width="549" height="228" alt="image" src="https://github.com/user-attachments/assets/586d26b2-958d-412c-bd2d-c015f0c894ed" />

---

## Permissions

Tatyana is intended to be used by small, casual Guild Wars 2 communities.

Certain administrative commands may be restricted to designated guild roles, while regular members can still respond to Guild Mission polls.

<img width="673" height="188" alt="image" src="https://github.com/user-attachments/assets/6a426cfa-44e8-43a7-ac76-ac1fabcdad6c" />

---

## Timezone

Guild Mission times are currently displayed in **Australian Western Standard Time (AWST)**.

Support for additional timezones may be added in the future.

---

Features may be added, changed, or removed as development continues.
