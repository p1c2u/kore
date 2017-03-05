import logging

from kore.configs.models import BaseConfig

log = logging.getLogger(__name__)


class BasePluginConfig(BaseConfig):

    def __getitem__(self, key):
        raise NotImplementedError

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
