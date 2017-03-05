import logging

log = logging.getLogger(__name__)


class BasePluginComponent(object):

    factories = {}
    services = {}

    def get_factories(self):
        return self.factories.items()

    def get_services(self):
        return self.services.items()

    def pre_hook(self, container):
        return

    def post_hook(self, container):
        return
