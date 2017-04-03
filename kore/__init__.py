# -*- coding: utf-8 -*-
from kore.configs.factories import ConfigFactory
from kore.components.factories import ComponentFactory
from kore.components.registrars import (
    FactoryRegistrar,
    ServiceRegistrar,
    ComponentRegistrar,
)
from kore.containers.factories import ContainerFactory
from kore.plugins.iterators import PluginIterator
from kore.plugins.providers import PluginsProvider

__author__ = 'Artur Maciąg'
__email__ = 'maciag.artur@gmail.com'
__version__ = '0.0.3'
__url__ = 'https://github.com/p1c2u/kore'


configs_iterator = PluginIterator('kore.configs')
components_iterator = PluginIterator('kore.components')

config_plugins_provider = PluginsProvider(configs_iterator)
component_plugins_provider = PluginsProvider(components_iterator)

factory_registrar = FactoryRegistrar()
service_registrar = ServiceRegistrar()
component_registrar = ComponentRegistrar(factory_registrar, service_registrar)

config_factory = ConfigFactory(config_plugins_provider)
component_factory = ComponentFactory()
container_factory = ContainerFactory(
    component_plugins_provider, component_factory, component_registrar)
