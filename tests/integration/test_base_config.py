import pytest

from kore.configs.base import BaseConfig


class TestBaseConfigGet(object):

    @pytest.fixture(scope='session')
    def base_config(self):
        return BaseConfig()

    def test_missing(self, base_config):
        key = 'missing'

        with pytest.raises(NotImplementedError):
            base_config.get(key)

    def test_missing_default_value(self, base_config):
        key = 'missing'
        default = 'test2'

        with pytest.raises(NotImplementedError):
            base_config.get(key, default)
