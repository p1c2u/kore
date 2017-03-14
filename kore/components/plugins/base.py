import logging

log = logging.getLogger(__name__)


class BasePluginComponent(object):

    factories = ()
    services = ()

    def get_factories(self):
        return self.factories

    def get_services(self):
        return self.services

    def pre_hook(self, container):
        return

    def post_hook(self, container):
        return
