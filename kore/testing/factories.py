from six import iteritems

from kore.configs.dict import DictConfig
from kore.components.base import BaseComponent
from kore.components.factories import ComponentFactory
from kore.components.registrars import ComponentRegistrar
from kore.containers.factories import ContainerFactory
from kore.plugins.models import Plugin
from kore.plugins.providers import PluginsProvider


class Factory(dict):

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    def __init__(self, *args, **kwargs):
        super(Factory, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def create_config_dict(self):
        return {}

    def create_dict_config(self, config_dict=None):
        if config_dict is None:
            config_dict = self.create_config_dict()

        return DictConfig(**config_dict)

    def create_factories(self):
        return {}

    def create_services(self):
        return {}

    def create_component_class(
            self, name="TestComponent", factories=None, services=None,
            pre_hook=None, post_hook=None,
    ):
        if factories is None:
            factories = self.create_factories()

        if services is None:
            services = self.create_services()

        attributes = {
            "get_factories": lambda self: tuple(iteritems(factories)),
            "get_services": lambda self: tuple(iteritems(services)),
        }

        if pre_hook is not None:
            attributes['pre_hook'] = pre_hook

        if post_hook is not None:
            attributes['post_hook'] = post_hook

        return type(name, (BaseComponent, ), attributes)

    def create_component_factory(self):
        return ComponentFactory()

    def create_component_registrar(self):
        return ComponentRegistrar()

    def create_component(
            self, component_factory=None, plugin=None,
            plugin_namespace=None, plugin_class=None,
    ):
        if component_factory is None:
            component_factory = self.create_component_factory()

        if plugin is None:
            plugin = self.create_plugin(plugin_namespace, plugin_class)

        return component_factory.create(
            plugin.component_class, plugin.namespace)

    def create_container_factory(
            self, plugins_provider=None, component_factory=None,
            component_registrar=None, plugins_iterator=None,
    ):
        if plugins_provider is None:
            plugins_provider = self.create_plugins_provider(
                plugins_iterator=plugins_iterator)

        if component_factory is None:
            component_factory = self.create_component_factory()

        if component_registrar is None:
            component_registrar = self.create_component_registrar()

        return ContainerFactory(
            plugins_provider, component_factory, component_registrar)

    def create_container(
            self, container_factory=None, config=None,
            plugins_provider=None, component_factory=None,
            component_registrar=None, plugins_iterator=None,
            config_dict=None,
    ):
        if container_factory is None:
            container_factory = self.create_container_factory(
                plugins_provider=plugins_provider,
                component_factory=component_factory,
                component_registrar=component_registrar,
                plugins_iterator=plugins_iterator,
            )

        if config is None:
            config = self.create_dict_config(config_dict=config_dict)

        return container_factory.create(config=config)

    def create_plugin(self, name="TestPlugin", component_class=None):
        if component_class is None:
            component_class = self.create_component_class()

        return Plugin(name, component_class)

    def create_plugins_provider(self, plugins_iterator=None):
        if plugins_iterator is None:
            plugins_iterator = []

        return PluginsProvider(plugins_iterator)
