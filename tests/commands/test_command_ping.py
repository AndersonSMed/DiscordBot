import pytest

from app.commands.ping import Ping


@pytest.fixture()
def ping_command_object(client, message):
    return Ping(client=client, message=message)


@pytest.mark.asyncio
async def test_run_ping_command(ping_command_object):
    await ping_command_object.run()

    message = ping_command_object.message
    channel = message.channel

    channel.send.assert_called_once_with('Pong!')
