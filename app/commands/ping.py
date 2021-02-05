from commands import base


class Ping(base.Base):
    command_name = 'ping'

    async def process(self):
        await self.message.channel.send('Pong!')
