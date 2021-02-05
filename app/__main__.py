import os

import discord

from exceptions import NoEnvironmentVariableError


DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

if not DISCORD_TOKEN:
    raise NoEnvironmentVariableError(
        "Please, set your DISCORD_TOKEN environment variable"
    )
    exit()

client = discord.Client(DISCORD_TOKEN)
