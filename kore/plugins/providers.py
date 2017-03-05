from kore.plugins.exceptions import PluginNotFoundError


class PluginsProvider(object):

    def __init__(self, iterator):
        self.iterator = iterator
        self._plugins_cache = None

    def get(self, name):
        try:
            return self.plugins[name]
        except KeyError:
            raise PluginNotFoundError("Plugin `%s` not found" % name)

    def all(self):
        return self.plugins.items()

    @property
    def plugins(self):
        if self._plugins_cache is None:
            self._plugins_cache = self._get_plugins()

        return self._plugins_cache

    def _get_plugins(self):
        plugins = {}
        for plugin in self.iterator:
            plugins[plugin.name] = plugin.plugin
        return plugins
