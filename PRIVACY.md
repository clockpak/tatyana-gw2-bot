# Tatyana — Privacy Notice

**Last updated:** 30th August 2026

Tatyana is a Discord bot designed to help Guild Wars 2 guilds coordinate Guild Missions and track attendance.

## What information is stored?

When a member responds to a Guild Mission, Tatyana stores:

* Their Discord User ID
* Their selected attendance response:

  * 🟢 Interested
  * 🟡 Maybe
  * 🔴 Can't Attend

The bot uses the Discord User ID to identify the member when displaying the attendance list.

Tatyana does not intentionally collect Discord passwords, email addresses, private messages, or other unrelated personal information.

## How is the information used?

Attendance information is used solely to coordinate Guild Missions.

The regular Guild Mission message displays only the number of members in each response category.

The `/mission-attendees` command can display the Discord display names associated with those responses to authorised guild organisers.

## Where is the information stored?

For the official MIGC-hosted instance of Tatyana, mission and attendance data is stored in the bot's `missions.json` data file on its Railway-hosted application environment.

The bot's source code is hosted publicly on GitHub, but `missions.json` is **not** included in the public repository.

Discord bot credentials are stored separately as protected environment variables and are not included in the public repository.

Because Tatyana is open source, other guilds may host their own instances. In those cases, the administrator hosting the bot is responsible for determining where their instance stores its data.

## Who can access the information?

Attendance information is accessible through Tatyana's authorised attendance-management commands.

The information may also be accessible to the administrator responsible for the server or hosting environment in which Tatyana is running.

Individual attendance information is not intentionally published in Tatyana's public source repository.

## How long is information retained?

Mission and attendance information is retained by the bot while it is required for Guild Mission coordination.

The current implementation stores this information in `missions.json`. Data retention and deletion for independently hosted instances is the responsibility of the instance administrator.

## Open Source

Tatyana's source code is publicly available so that users and guild administrators can inspect how the bot handles attendance information.

The public repository does not contain guild members' attendance data or Discord bot credentials.

Tatyana is licensed under the MIT License.

## Discord and third-party hosting

Tatyana operates through the Discord API and is therefore subject to Discord's applicable terms and policies.

The MIGC-hosted instance is operated using Railway for application hosting and GitHub for public source-code hosting.

## Contact

For independently hosted instances, contact the administrator responsible for that instance.
