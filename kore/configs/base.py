class BaseConfigSection(object):

    @property
    def __dict__(self, key):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __getitem__(self, key):
        raise NotImplementedError

    def keys(self):
        raise NotImplementedError

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def get_section(self, name):
        raise NotImplementedError


class BaseConfig(BaseConfigSection):
    pass
