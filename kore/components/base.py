import logging

log = logging.getLogger(__name__)


class BaseComponent(object):

    factories = ()
    services = ()

    def __init__(self, namespace=None):
        self.namespace = namespace

    def get_factories(self):
        return self.factories

    def get_services(self):
        return self.services
