MESSAGE_ACTIVATOR = '$'


class BaseProcessor:
    def __init__(self, client, message):
        self.client = client
        self.message = message


class PingProcessor(BaseProcessor):
    async def process(self, payload):
        await self.message.channel.send('Pong!')


class DefaultProcessor(BaseProcessor):
    async def process(self, payload):
        await self.message.channel.send(
            'Sorry, but this command is not supported :('
        )


mapped_processors = {
    "default": DefaultProcessor,
    "ping": PingProcessor
}


def get_message_processor_from_command(command, client, message):
    processor_class = mapped_processors["default"]

    if command in mapped_processors:
        processor_class = mapped_processors[command]

    return processor_class(client, message)


async def on_received_message(client, message):
    if message.author == client.user:
        return

    has_activator = message.content.startswith(MESSAGE_ACTIVATOR)
    splitted_message = message.content.split(' ')

    if has_activator and splitted_message:
        command = splitted_message.pop(0)
        payload = ' '.join(splitted_message)

        command = command.replace(MESSAGE_ACTIVATOR, '')

        message_processor = get_message_processor_from_command(
            command,
            client,
            message
        )
        await message_processor.process(payload)
