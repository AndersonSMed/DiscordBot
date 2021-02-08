from app import commands


async def on_received_message(client, message):
    if message.author == client.user:
        return

    command = commands.get_command_instance_from_message(
        client,
        message
    )

    if command:
        await command.run()
