import logging

from knot import Container

log = logging.getLogger(__name__)


class ContainerFactory(object):

    def __init__(
            self, components_provider, component_factory, component_registrar):
        self.components_provider = components_provider
        self.component_factory = component_factory
        self.component_registrar = component_registrar

    def create(self, **components):
        log.debug("Creating container")
        container = Container(components)

        for namespace, component_class in self.components_provider.all():
            component = self.create_component(component_class)
            self.component_registrar.register(container, component, namespace)

        self.component_registrar.bind(container)

        return container

    def create_component(self, component_class):
        log.debug("Creating `%s` plugin", component_class.__name__)
        return self.component_factory.create(component_class)
