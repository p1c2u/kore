from collections import defaultdict

from kore.configs.plugins.base import BasePluginConfig


class DictConfig(defaultdict, BasePluginConfig):

    def __missing__(self, key):
        return defaultdict()
