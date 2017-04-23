import logging

from knot import Container

log = logging.getLogger(__name__)


class ContainerFactory(object):

    def __init__(
            self, components_provider, component_factory, component_registrar):
        self.components_provider = components_provider
        self.component_factory = component_factory
        self.component_registrar = component_registrar

    def create(self, config, **initial):
        log.debug("Creating container")
        kore_config = config.get('kore', {})

        container = Container(initial)
        container.update({
            'config': config,
            'kore.config': kore_config,
        })

        components_dict = self.provide_components(kore_config)
        for namespace, component_class in components_dict:
            component = self.create_component(component_class)
            self.component_registrar.register(container, component, namespace)

        self.component_registrar.bind(container)

        return container

    def provide_components(self, kore_config):
        components_whitelist = kore_config.get('plugins', [])

        if not components_whitelist:
            return self.components_provider.all()

        return self.components_provider.filter(*components_whitelist)

    def create_component(self, component_class):
        log.debug("Creating `%s` plugin", component_class.__name__)
        return self.component_factory.create(component_class)
