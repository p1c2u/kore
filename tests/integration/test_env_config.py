from kore import config_factory

from kore.configs.env import EnvSection


class TestEnvConfig(object):

    def test_get_section(self):
        config_type = 'env'
        config_opt = {
            'bar': 'baz',
        }

        config = config_factory.create(config_type, **config_opt)

        result = config.get_section('UNDEFINED')

        assert result.__class__ is EnvSection

    def test_get_section_default_value(self):
        config_type = 'env'
        config_opt = {
            'bar': 'baz',
        }

        config = config_factory.create(config_type, **config_opt)

        section = config.get_section('UNDEFINED')

        result = section.get('UNDEFINED', 'undefined')

        assert result == 'undefined'

    def test_section_option(self, monkeypatch):
        monkeypatch.setenv('TESTING_KEY', 'value')
        config_type = 'env'
        config_opt = {
            'bar': 'baz',
        }
        config = config_factory.create(config_type, **config_opt)
        section = config.get_section('TESTING')

        result = section['key']

        assert result == 'value'

    def test_section_option_upper(self, monkeypatch):
        monkeypatch.setenv('TESTING_KEY', 'value')
        config_type = 'env'
        config_opt = {
            'bar': 'baz',
        }
        config = config_factory.create(config_type, **config_opt)
        section = config.get_section('TESTING')

        result = dict(section)

        assert result == {
            'key': 'value',
        }

    def test_get_value(self, monkeypatch):
        monkeypatch.setenv('TESTING_KEY', 'value')
        config_type = 'env'
        config_opt = {
            'bar': 'baz',
        }
        config = config_factory.create(config_type, **config_opt)

        result = config.get('key2', 'undefined')

        assert result == 'undefined'
