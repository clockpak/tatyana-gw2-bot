import discord
from discord import app_commands
from datetime import datetime
import json
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# BOT SETTINGS
# ============================================================

TOKEN = os.getenv("DISCORD_TOKEN")

GUILD_ID = 1505910756875571212
GUILD = discord.Object(id=GUILD_ID)

intents = discord.Intents.default()

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)


# ============================================================
# ROLE PERMISSIONS
# ============================================================

# Add the Discord role names that should be allowed
# to use restricted bot commands.
#
# Anyone with ANY of these roles can use them.

ALLOWED_ROLES = [
    "Mentally ill CEO (Guild leader)"
    "Mentally ill officer (Guild officer)"
    "Mentally ill captain (captain)",
    "Mentally ill veteran (Veteran)",
]


def has_allowed_role(interaction: discord.Interaction) -> bool:
    """Check whether the user has one of the allowed roles."""

    # Server owner always has permission
    if interaction.guild and interaction.user.id == interaction.guild.owner_id:
        return True

    # Make sure this is a guild member
    if not isinstance(interaction.user, discord.Member):
        return False

    # Check the member's roles
    user_roles = {role.name for role in interaction.user.roles}

    return bool(user_roles.intersection(ALLOWED_ROLES))


async def check_permissions(interaction: discord.Interaction) -> bool:
    """
    Check whether the user is allowed to use a restricted command.

    Returns True if allowed.
    Returns False and sends an error message if not.
    """

    if has_allowed_role(interaction):
        return True

    await interaction.response.send_message(
        "❌ You don't have permission to use this command.",
        ephemeral=True
    )

    return False


# ============================================================
# DATA STORAGE
# ============================================================

DATA_FILE = Path(__file__).parent / "missions.json"

responses = {}
current_mission = None


def save_data():
    """Save the current mission and responses."""

    data = {
        "mission": current_mission,
        "responses": {
            str(user_id): response
            for user_id, response in responses.items()
        }
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data():
    """Load the current mission and responses."""

    global current_mission

    if not DATA_FILE.exists():
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        current_mission = data.get("mission")

        responses.clear()

        for user_id, response in data.get("responses", {}).items():
            responses[int(user_id)] = response

        print("Mission data loaded successfully.")

    except Exception as e:
        print(f"Could not load mission data: {e}")


# ============================================================
# MISSION OPTIONS
# ============================================================

MISSION_TYPES = [
    app_commands.Choice(
        name="Guild Bounty",
        value="Guild Bounty"
    ),
    app_commands.Choice(
        name="Guild Trek",
        value="Guild Trek"
    ),
    app_commands.Choice(
        name="Guild Race",
        value="Guild Race"
    ),
    app_commands.Choice(
        name="Guild Challenge",
        value="Guild Challenge"
    ),
    app_commands.Choice(
        name="Guild Puzzle",
        value="Guild Puzzle"
    ),
]


DIFFICULTIES = [
    app_commands.Choice(
        name="Easy",
        value="Easy"
    ),
    app_commands.Choice(
        name="Medium",
        value="Medium"
    ),
    app_commands.Choice(
        name="Hard",
        value="Hard"
    ),
]


# ============================================================
# MISSION VIEW / BUTTONS
# ============================================================

class MissionView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    def create_embed(self):

        interested = list(responses.values()).count("interested")
        maybe = list(responses.values()).count("maybe")
        cant_attend = list(responses.values()).count("cant_attend")

        if current_mission is None:

            return discord.Embed(
                title="🏰 Guild Mission",
                description="No mission is currently active."
            )

        embed = discord.Embed(
            title=f"🏰 {current_mission['title']}",
            description=(
                f"⚔️ **Mission:** "
                f"{current_mission['mission_type']}\n"

                f"📊 **Difficulty:** "
                f"{current_mission['difficulty']}\n"

                f"📅 **Date:** "
                f"{current_mission['date']}\n"

                f"🕐 **Time:** "
                f"{current_mission['time']} AWST\n\n"

                "Let us know whether you're interested "
                "in attending:\n\n"

                "🟢 **Interested** — I'm planning to attend\n"
                "🟡 **Maybe** — I'm not sure yet\n"
                "🔴 **Can't Attend** — I won't be joining"
            )
        )

        embed.add_field(
            name="🎁 Rewards",
            value=(
                f"💰 **Guild Favor:** "
                f"{current_mission['favor']}\n"

                f"🏅 **Guild Commendations:** "
                f"{current_mission['commendations']}"
            ),
            inline=False
        )

        if current_mission["notes"]:

            embed.add_field(
                name="📝 Notes",
                value=current_mission["notes"],
                inline=False
            )

        embed.add_field(
            name="📊 Current Responses",
            value=(
                f"🟢 Interested: **{interested}**\n"
                f"🟡 Maybe: **{maybe}**\n"
                f"🔴 Can't Attend: **{cant_attend}**"
            ),
            inline=False
        )

        return embed

    async def record_response(
        self,
        interaction: discord.Interaction,
        response: str
    ):

        user_id = interaction.user.id

        # Record or replace the member's response
        responses[user_id] = response

        # Save immediately
        save_data()

        response_names = {
            "interested": "Interested",
            "maybe": "Maybe",
            "cant_attend": "Can't Attend"
        }

        # Update the mission message
        await interaction.message.edit(
            embed=self.create_embed(),
            view=self
        )

        # Private confirmation
        await interaction.response.send_message(
            f"Your response has been recorded as "
            f"**{response_names[response]}**. 💕",
            ephemeral=True
        )

    @discord.ui.button(
        label="Interested",
        style=discord.ButtonStyle.success,
        emoji="🟢"
    )
    async def interested(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await self.record_response(
            interaction,
            "interested"
        )

    @discord.ui.button(
        label="Maybe",
        style=discord.ButtonStyle.primary,
        emoji="🟡"
    )
    async def maybe(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await self.record_response(
            interaction,
            "maybe"
        )

    @discord.ui.button(
        label="Can't Attend",
        style=discord.ButtonStyle.danger,
        emoji="🔴"
    )
    async def cant_attend(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await self.record_response(
            interaction,
            "cant_attend"
        )


# ============================================================
# BOT READY
# ============================================================

@bot.event
async def on_ready():

    load_data()

    print(
        f"Tatyana is online as {bot.user}"
    )

    try:

        synced = await tree.sync(
            guild=GUILD
        )

        print(
            f"Synced {len(synced)} command(s)!"
        )

    except Exception as e:

        print(
            f"Command sync error: {e}"
        )


# ============================================================
# /SAY
# ============================================================

@tree.command(
    name="say",
    description="Make Tatyana say something",
    guild=GUILD
)
@app_commands.describe(
    message="What you want Tatyana to say"
)
async def say(
    interaction: discord.Interaction,
    message: str
):

    # Check permissions
    if not await check_permissions(interaction):
        return

    # Acknowledge the command privately first
    await interaction.response.send_message(
        "✅ Sent!",
        ephemeral=True
    )

    # Send the actual message as the bot
    await interaction.channel.send(
        message
    )


# ============================================================
# /MISSION
# ============================================================

@tree.command(
    name="mission",
    description="Create a Guild Mission interest check",
    guild=GUILD
)
@app_commands.describe(
    mission_type="Type of Guild Mission",
    difficulty="Mission difficulty",
    date="Mission date (DD/MM/YYYY)",
    time="Mission time (HH:MM, AWST)",
    favor="Guild Favor awarded",
    commendations="Guild Commendations awarded",
    title="Optional title for the mission",
    notes="Optional information for guild members"
)
@app_commands.choices(
    mission_type=MISSION_TYPES,
    difficulty=DIFFICULTIES
)
async def mission(
    interaction: discord.Interaction,
    mission_type: app_commands.Choice[str],
    difficulty: app_commands.Choice[str],
    date: str,
    time: str,
    favor: int,
    commendations: str,
    title: str = "Guild Mission Interest Check",
    notes: str = ""
):

    # Check permissions
    if not await check_permissions(interaction):
        return

    global current_mission

    # Validate date and time
    try:

        mission_datetime = datetime.strptime(
            f"{date} {time}",
            "%d/%m/%Y %H:%M"
        )

    except ValueError:

        await interaction.response.send_message(
            "❌ I couldn't understand that date/time.\n\n"

            "Please use:\n"
            "`DD/MM/YYYY` for the date\n"
            "`HH:MM` for the time\n\n"

            "Example:\n"
            "`30/08/2026`\n"
            "`19:00`",

            ephemeral=True
        )

        return

    # Start a new mission
    responses.clear()

    current_mission = {

        "date": mission_datetime.strftime(
            "%d %B %Y"
        ),

        "time": mission_datetime.strftime(
            "%H:%M"
        ),

        "title": title,

        "mission_type": mission_type.value,

        "difficulty": difficulty.value,

        "favor": favor,

        "commendations": commendations,

        "notes": notes
    }

    # Save the mission
    save_data()

    # Create the mission view
    view = MissionView()

    # Send the mission
    await interaction.response.send_message(
        embed=view.create_embed(),
        view=view
    )


# ============================================================
# /MISSION-ATTENDEES
# ============================================================

@tree.command(
    name="mission-attendees",
    description="Show the current Guild Mission responses",
    guild=GUILD
)
async def mission_attendees(
    interaction: discord.Interaction
):

    if current_mission is None:

        await interaction.response.send_message(
            "❌ There isn't currently an active Guild Mission.",
            ephemeral=True
        )

        return

    interested_members = []
    maybe_members = []
    cant_attend_members = []

    # Fetch members directly from Discord
    for user_id, response in responses.items():

        try:

            member = await interaction.guild.fetch_member(
                user_id
            )

        except discord.NotFound:

            # User is no longer in the guild
            continue

        except discord.HTTPException:

            # Discord temporarily failed to provide the member
            continue

        if response == "interested":

            interested_members.append(
                member.display_name
            )

        elif response == "maybe":

            maybe_members.append(
                member.display_name
            )

        elif response == "cant_attend":

            cant_attend_members.append(
                member.display_name
            )

    # Sort alphabetically
    interested_members.sort()
    maybe_members.sort()
    cant_attend_members.sort()

    # Build member lists
    interested_text = (
        "\n".join(
            f"• {name}"
            for name in interested_members
        )
        if interested_members
        else "Nobody yet."
    )

    maybe_text = (
        "\n".join(
            f"• {name}"
            for name in maybe_members
        )
        if maybe_members
        else "Nobody yet."
    )

    cant_attend_text = (
        "\n".join(
            f"• {name}"
            for name in cant_attend_members
        )
        if cant_attend_members
        else "Nobody yet."
    )

    # Create attendance embed
    embed = discord.Embed(
        title="📋 Guild Mission Attendees",
        description=(
            f"🏰 **{current_mission['title']}**\n"
            f"⚔️ {current_mission['mission_type']} — "
            f"{current_mission['difficulty']}\n"
            f"📅 {current_mission['date']} "
            f"at {current_mission['time']} AWST"
        )
    )

    embed.add_field(
        name=f"🟢 Interested ({len(interested_members)})",
        value=interested_text,
        inline=False
    )

    embed.add_field(
        name=f"🟡 Maybe ({len(maybe_members)})",
        value=maybe_text,
        inline=False
    )

    embed.add_field(
        name=f"🔴 Can't Attend ({len(cant_attend_members)})",
        value=cant_attend_text,
        inline=False
    )

    # Send privately to the person using the command
    await interaction.response.send_message(
        embed=embed,
        ephemeral=True
    )


# ============================================================
# START BOT
# ============================================================

bot.run(TOKEN)
