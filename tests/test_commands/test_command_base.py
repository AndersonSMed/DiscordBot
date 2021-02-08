import pytest

from app.commands.base import Base


class DummyCommand(Base):
    async def run(self):
        pass


def test_create_instance_without_command_name(client, message):
    with pytest.raises(ValueError):
        DummyCommand(client=client, message=message)
