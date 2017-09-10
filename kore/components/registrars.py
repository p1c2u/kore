import logging

log = logging.getLogger(__name__)


class ComponentRegistrar(object):

    def __init__(self):
        self.components = []

    def register(self, container, component):
        log.debug("Registering `%s`", component.namespace)
        component.pre_hook(container)
        factories = component.get_factories()
        for name, factory in factories:
            container.add_factory(factory, name, component.namespace)
        services = component.get_services()
        for name, service in services:
            container.add_service(service, name, component.namespace)
        self.components.append(component)

    def bind(self, container):
        for component in self.components:
            component.post_hook(container)
