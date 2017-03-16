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
def factory_component():
    return lambda self: datetime.utcnow()


@pytest.fixture
def service_component():
    return lambda self: datetime.utcnow()


@pytest.fixture
def component_plugin_class(factory_component, service_component):
    return type(
        "TestPluginComponent",
        (BasePluginComponent, ),
        {
            "get_factories": lambda self: (("factory", factory_component),),
            "get_services": lambda self: (("service", service_component),),
        }
    )


@pytest.fixture
def component_plugin(component_plugin_class):
    return Plugin('test', component_plugin_class)


@pytest.fixture
def component_plugins_iterator(component_plugin):
    return (component_plugin, )


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
