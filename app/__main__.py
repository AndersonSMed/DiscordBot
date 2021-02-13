"""Setup discord client"""
import discord

from app import constants
from app import exceptions
from app import handlers


if not constants.DISCORD_BOT_TOKEN:
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


if __name__ == "__main__":
    client.run(constants.DISCORD_BOT_TOKEN)
