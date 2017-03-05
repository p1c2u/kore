class ConfigFactoryError(Exception):
    pass


class ConfigPluginNotFoundError(ConfigFactoryError):
    pass
