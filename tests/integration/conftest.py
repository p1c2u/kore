from datetime import datetime

import pytest

from kore.configs.base import BaseConfig
from kore.testing.factories import Factory


@pytest.fixture(scope='session')
def factory():
    return Factory()


@pytest.fixture
def factory_1():
    return lambda container: container('test.factory_2')


@pytest.fixture
def factory_2():
    return lambda container: datetime.utcnow()


@pytest.fixture
def service_1():
    return lambda container: container('test.service_2')


@pytest.fixture
def service_2():
    return lambda container: datetime.utcnow()


@pytest.fixture
def pre_hook():
    return lambda self, container: container


@pytest.fixture
def post_hook():
    return lambda self, container: container('test.service_1')


@pytest.fixture
def component_class(
        factory_1, factory_2, service_1, service_2, pre_hook, post_hook,
        factory,
):
    return factory.create_component_class(
        name="TestComponent",
        factories={'factory_1': factory_1, 'factory_2': factory_2},
        services={'service_1': service_1, 'service_2': service_2},
        pre_hook=pre_hook, post_hook=post_hook,
    )


@pytest.fixture
def plugin_1(component_class, factory):
    return factory.create_plugin(
        name='test', component_class=component_class)


@pytest.fixture
def plugin_2(component_class, factory):
    return factory.create_plugin(
        name='test_2', component_class=component_class)
