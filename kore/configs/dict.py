from collections import defaultdict

from kore.configs.base import BaseConfig


class DictConfig(defaultdict, BaseConfig):

    def __missing__(self, key):
        return defaultdict()
