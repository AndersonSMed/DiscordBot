from unittest.mock import patch

import pytest

from app.commands import get_command_instance_from_message
from app.commands.base import Base


class DummyImplementation(Base):
    async def run(self):
        pass


class DummyCommand(DummyImplementation):
    command_name = 'dummy'


class DummyCommand2(DummyImplementation):
    command_name = 'dummy_2'


class DummyCommand3(DummyImplementation):
    command_name = 'dummy_3'


COMMAND_CLASSES = [DummyCommand, DummyCommand2, DummyCommand3]


@pytest.mark.parametrize(
    "message_content, type_of_object", [
        ("$dummy", DummyCommand),
        ("$dummy_2", DummyCommand2),
        ("$dummy_3", DummyCommand3)
    ]
)
@patch('app.commands.COMMAND_CLASSES', COMMAND_CLASSES)
def test_get_command_instance_without_payload(
    client,
    message,
    message_content,
    type_of_object
):
    message.content = message_content

    instance = get_command_instance_from_message(client, message)

    assert type(instance) == type_of_object
    assert instance.payload is None


@pytest.mark.parametrize(
    "message_content, type_of_object", [
        ("$dummy lorem ipsum", DummyCommand),
        ("$dummy_2 lorem ipsum", DummyCommand2),
        ("$dummy_3 lorem ipsum", DummyCommand3)
    ]
)
@patch('app.commands.COMMAND_CLASSES', COMMAND_CLASSES)
def test_get_command_instance_with_payload(
    client,
    message,
    message_content,
    type_of_object
):
    message.content = message_content

    instance = get_command_instance_from_message(client, message)

    assert type(instance) == type_of_object
    assert instance.payload == "lorem ipsum"

