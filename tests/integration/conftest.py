import pytest

from kore.testing.factories import Factory


@pytest.fixture(scope='session')
def factory():
    return Factory()
