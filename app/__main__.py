import os

import discord

from app import exceptions
from app import handlers


DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

if not DISCORD_BOT_TOKEN:
    raise exceptions.NoEnvironmentVariableError(
        "Please, set your DISCORD_BOT_TOKEN environment variable"
    )

client = discord.Client()


@client.event
async def on_message(message):
    await handlers.messages.on_received_message(client, message)


@client.event
async def on_guild_channel_create(channel):
    await handlers.channels.on_guild_channel_created(client, channel)


client.run(DISCORD_BOT_TOKEN)
