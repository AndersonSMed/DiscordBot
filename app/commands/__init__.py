import constants
from commands import ping

command_classes = [ping.Ping]


def get_command_instance_from_message(client, message):
    mapped_commands = {cmd.command_name: cmd for cmd in command_classes}

    splitted_words = message.content.split(' ')

    if len(splitted_words) > 0:

        command_name = splitted_words.pop()
        command_name = command_name.replace(constants.MESSAGE_ACTIVATOR, '')

        payload = None

        if len(splitted_words) > 0:
            payload = ' '.join(splitted_words)

        if command_name in mapped_commands:
            selected_command = mapped_commands[command_name]

            return selected_command(
                client=client,
                message=message,
                payload=payload
            )

    return None
