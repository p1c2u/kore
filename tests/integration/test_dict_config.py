class TestDictConfigGet(object):

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


class TestDictConfigGetItem(object):

    def test_missing(self, dict_config):
        key = 'missing'

        result = dict_config[key]

        assert result == {}

    def test_exists(self, dict_config, config_dict):
        key = 'test'

        result = dict_config[key]

        assert result == config_dict[key]
