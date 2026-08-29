# Tatyana

A Discord bot for Guild Wars 2 guild mission coordination.

## Documentation

- [Commands](COMMANDS.md) — Available commands and their usage
- [Privacy](PRIVACY.md) — Information about data collection and storage

## Features

* Guild Mission interest polls
* Interested / Maybe / Can't Attend responses
* Attendance tracking
* Mission dates and times in customizable time zones
* Guild mission type and difficulty
* Guild Favor and Commendation tracking
* Persistent mission data

## Requirements

* Python 3.14+
* discord.py
* python-dotenv

## Setup

1. Clone the repository
2. Install the required dependencies
3. Paste your Discord server ID into GUILD_ID =
4. Create a `.env` file
5. Add your Discord bot token to the `.env` file as `DISCORD_TOKEN=`
6. Run `tatyana.py`

## License

This project is licensed under the MIT License. See the (LICENSE) file for details.

## Disclaimer

Tatyana is an independent community project and is not affiliated with or endorsed by ArenaNet or Guild Wars 2.

## Privacy

Tatyana stores Discord User IDs and attendance responses so authorised guild organisers can see who has indicated that they are interested in a Guild Mission.

For more information, see [PRIVACY.md](PRIVACY.md).
