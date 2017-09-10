from datetime import datetime

import pytest

from kore.components.factories import ComponentFactory
from kore.components.plugins.base import BasePluginComponent
from kore.configs.models import BaseConfig
from kore.configs.plugins.dict import DictConfig
from kore.containers.factories import ContainerFactory
from kore.plugins.models import Plugin
from kore.plugins.providers import PluginsProvider


@pytest.fixture(scope='session')
def base_config():
    return BaseConfig()


@pytest.fixture(scope='session')
def config_dict():
    return {'test': 'test'}


@pytest.fixture(scope='session')
def dict_config(config_dict):
    return DictConfig(**config_dict)


@pytest.fixture
def factory_component_1():
    return lambda container: container('test.factory_2')


@pytest.fixture
def factory_component_2():
    return lambda container: datetime.utcnow()


@pytest.fixture
def service_component_1():
    return lambda container: container('test.service_2')


@pytest.fixture
def service_component_2():
    return lambda container: datetime.utcnow()


@pytest.fixture
def component_plugin_class(
        factory_component_1, factory_component_2, service_component_1,
        service_component_2):
    return type(
        "TestPluginComponent",
        (BasePluginComponent, ),
        {
            "get_factories":
                lambda self: (
                    ("factory_1", factory_component_1),
                    ("factory_2", factory_component_2),
                ),
            "get_services":
                lambda self: (
                    ("service_1", service_component_1),
                    ("service_2", service_component_2),
                ),
            "pre_hook":
                lambda self, container: container,
            "post_hook":
                lambda self, container: container('test.service_1'),
        }
    )


@pytest.fixture
def component_plugin_1(component_plugin_class):
    return Plugin('test', component_plugin_class)


@pytest.fixture
def component_plugin_2(component_plugin_class):
    return Plugin('test_2', component_plugin_class)


@pytest.fixture
def component_plugins_iterator(component_plugin_1, component_plugin_2):
    return (component_plugin_1, component_plugin_2)


@pytest.fixture
def component_plugins_provider(component_plugins_iterator):
    return PluginsProvider(component_plugins_iterator)


@pytest.fixture
def component_factory():
    return ComponentFactory()


@pytest.fixture
def component_registrar():
    from kore import component_registrar
    return component_registrar


@pytest.fixture
def container_factory(
        component_plugins_provider, component_factory, component_registrar):
    return ContainerFactory(
        component_plugins_provider, component_factory, component_registrar)


@pytest.fixture
def container(container_factory, dict_config):
    return container_factory.create(config=dict_config)
