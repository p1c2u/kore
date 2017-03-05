import logging

from kore.configs.exceptions import ConfigPluginNotFoundError
from kore.plugins.exceptions import PluginNotFoundError

log = logging.getLogger(__name__)


class ConfigFactory(object):

    def __init__(self, config_provider):
        self.config_provider = config_provider

    def create(self, config_type, *args, **kwargs):
        log.debug("Creating `%s` config", config_type)

        try:
            config_class = self.config_provider.get(config_type)
        except PluginNotFoundError:
            raise ConfigPluginNotFoundError(
                "Config type `%s` not found" % config_type)
        else:
            return config_class(*args, **kwargs)
