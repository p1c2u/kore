class PluginProviderError(Exception):
    pass


class PluginNotFoundError(PluginProviderError):
    pass
