import logging

log = logging.getLogger(__name__)


class ProviderRegistrar(object):

    namespace_separator = '.'

    def register(self, container, providers, namespace):
        for name, provider in providers:
            component_name = self.get_component_name(name, namespace)
            self.add_provider(container, provider, component_name)

    def get_component_name(self, name, namespace):
        return self.namespace_separator.join([namespace, name])

    def add_provider(self, container, provider, component_name):
        raise NotImplementedError


class FactoryRegistrar(ProviderRegistrar):

    def add_provider(self, container, provider, name):
        log.debug("Registering `%s` factory", name)
        container.add_factory(provider, name)


class ServiceRegistrar(ProviderRegistrar):

    def add_provider(self, container, provider, name):
        log.debug("Registering `%s` service", name)
        container.add_service(provider, name)


class ComponentRegistrar(object):

    def __init__(self, factory_registrar, service_registrar):
        self.factory_registrar = factory_registrar
        self.service_registrar = service_registrar
        self.components = []

    def register(self, container, component, namespace):
        log.debug("Registering `%s`", namespace)
        component.pre_hook(container)
        factories = component.get_factories()
        self.factory_registrar.register(container, factories, namespace)
        services = component.get_services()
        self.service_registrar.register(container, services, namespace)
        self.components.append(component)

    def bind(self, container):
        for component in self.components:
            component.post_hook(container)
