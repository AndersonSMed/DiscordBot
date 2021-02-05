import os

import discord

from exceptions import NoEnvironmentVariableError


DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

if not DISCORD_BOT_TOKEN:
    raise NoEnvironmentVariableError(
        "Please, set your DISCORD_BOT_TOKEN environment variable"
    )
    exit()

client = discord.Client(DISCORD_BOT_TOKEN)
