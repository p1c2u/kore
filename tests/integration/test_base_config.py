import pytest


class TestBaseConfigGet(object):

    def test_missing(self, base_config):
        key = 'missing'

        with pytest.raises(NotImplementedError):
            base_config.get(key)

    def test_missing_default_value(self, base_config):
        key = 'missing'
        default = 'test2'

        with pytest.raises(NotImplementedError):
            base_config.get(key, default)
