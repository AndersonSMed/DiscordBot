from app.commands import base


class Ping(base.Base):
    command_name = 'ping'

    async def run(self):
        await self.message.channel.send('Pong!')
