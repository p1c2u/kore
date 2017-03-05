import pytest

from kore import config_factory
from kore.configs.exceptions import ConfigPluginNotFoundError


class TestConfigFactory(object):

    def test_undefined_config_type(self):
        config_type = 'undefined'

        with pytest.raises(ConfigPluginNotFoundError):
            config_factory.create(config_type)

    def test_dict_config_type(self):
        config_type = 'dict'
        config_dict = {
            'foo': 'bar',
            'bar': 'baz',
        }

        config = config_factory.create(config_type, **config_dict)

        assert config == config_dict
