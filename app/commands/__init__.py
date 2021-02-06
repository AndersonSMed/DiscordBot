import constants
from commands import ping

command_classes = [ping.Ping]


def get_command_from_message(message):
    splitted_content = message.content.split(' ')

    has_at_least_one_word = len(splitted_content) > 0

    first_word = splitted_content[0] if has_at_least_one_word else None

    command_prefix = constants.COMMAND_PREFIX

    if first_word and first_word.startswith(command_prefix):
        return first_word.replace(command_prefix, '', 1)

    return None


def get_payload_from_message(message):
    splitted_content = message.content.split(' ')

    has_at_least_two_words = len(splitted_content) > 1

    if has_at_least_two_words:
        return ' '.join(splitted_content[1:])

    return None


def get_command_instance_from_message(client, message):
    mapped_commands = {cmd.command_name: cmd for cmd in command_classes}

    command_name = get_command_from_message(message=message)

    payload = get_payload_from_message(message=message)

    if command_name in mapped_commands:
        selected_command = mapped_commands[command_name]

        return selected_command(
            client=client,
            message=message,
            payload=payload
        )

    return None
