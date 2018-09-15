import os

from six import iteritems
from kore.configs.base import BaseConfigSection, BaseConfig


class BaseEnv(object):

    prefix = NotImplemented

    def __iter__(self):
        for key in self._iter_envvars():
            yield key.replace(self.prefix, "").lower()

    def __getitem__(self, key):
        envvar = self._get_envvar(key)
        return os.environ[envvar]

    @property
    def __dict__(self):
        data = {}
        for key in self._iter_envvars():
            subkey = key.replace(self.prefix, "").lower()
            data[subkey] = os.environ[key]
        return data

    def get(self, key, default=None):
        envvar = self._get_envvar(key)
        try:
            return os.environ[envvar]
        except KeyError:
            return default

    def keys(self):
        return list(self)

    def _get_envvar(self, key):
        return ''.join([self.prefix, key]).upper()

    def _iter_envvars(self):
        for key, value in iteritems(os.environ):
            if key.startswith(self.prefix):
                yield key


class EnvSection(BaseEnv, BaseConfigSection):

    separator = '_'

    def __init__(self, name):
        self.name = name

    @property
    def prefix(self):
        return ''.join([self.name, self.separator])

    def get_section(self, name):
        envvar = self._get_envvar(name)
        return EnvSection(envvar)


class EnvConfig(BaseEnv, BaseConfig):

    def __init__(self, *args, **kwargs):
        prefix = kwargs.get('env_prefix', '')

        self.prefix = prefix

    def get_section(self, name):
        envvar = self._get_envvar(name)
        return EnvSection(envvar)
