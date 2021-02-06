import pytest
import mock


class DummyClient():
    pass


class DummyChannel():
    send = mock.AsyncMock()


class DummyMessage():
    channel = DummyChannel()


@pytest.fixture(scope="function")
def client():
    return DummyClient()


@pytest.fixture(scope="function")
def message():
    return DummyMessage()
