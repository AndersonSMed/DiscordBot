import abc


class Base(abc.ABC):
    command_name = None

    def __init__(self, client, message, payload):
        self.client = client
        self.message = message
        self.payload = payload

        if not self.command_name:
            raise NotImplementedError('Should have a command name!')