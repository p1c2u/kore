import logging
import warnings

from kore.components import signals

log = logging.getLogger(__name__)


class ComponentRegistrar(object):

    def __init__(self):
        self.components = []

    def register(self, container, component):
        log.debug("Registering `%s`", component.namespace)

        if hasattr(component, 'pre_hook'):
            warnings.warn(
                "pre_hook method is deprecated. "
                "Use pre_register signal instead.",
                DeprecationWarning,
            )
            component.pre_hook(container)
        signals.pre_register.send(
            component.__class__, instance=component, container=container)

        factories = component.get_factories()
        for name, factory in factories:
            container.add_factory(factory, name, component.namespace)
        services = component.get_services()
        for name, service in services:
            container.add_service(service, name, component.namespace)
        self.components.append(component)

        signals.post_register.send(
            component.__class__, instance=component, container=container)

    def bind(self, container):
        for component in self.components:
            if hasattr(component, 'post_hook'):
                warnings.warn(
                    "post_hook method is deprecated. "
                    "Use post_register signal instead.",
                    DeprecationWarning,
                )
                component.post_hook(container)
