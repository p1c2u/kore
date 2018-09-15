import pytest


class BaseTestDictConfig(object):

    @pytest.fixture(scope='session')
    def config_dict(self):
        return {'test': 'test'}

    @pytest.fixture(scope='session')
    def dict_config(self, config_dict, factory):
        return factory.create_dict_config(config_dict=config_dict)


class TestDictConfigGet(BaseTestDictConfig):

    def test_missing(self, dict_config):
        key = 'missing'

        result = dict_config.get(key)

        assert result is None

    def test_missing_default_value(self, dict_config):
        key = 'missing'
        default = 'test2'

        result = dict_config.get(key, default)

        assert result == default

    def test_exists(self, dict_config, config_dict):
        key = 'test'

        result = dict_config.get(key)

        assert result == config_dict[key]


class TestDictConfigGetItem(BaseTestDictConfig):

    def test_missing(self, dict_config):
        key = 'missing'

        result = dict_config[key]

        assert result == {}

    def test_exists(self, dict_config, config_dict):
        key = 'test'

        result = dict_config[key]

        assert result == config_dict[key]
