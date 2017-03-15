import mock
import pytest

from kore.configs.models import BaseConfig


class TestBaseConfigGet(object):

    @pytest.fixture
    def config(self):
        return BaseConfig()

    @mock.patch.object(BaseConfig, '__getitem__', side_effect=KeyError)
    def test_missing(self, mock_getitem, config):
        key = mock.sentinel.key

        result = config.get(key)

        assert result is None

    @mock.patch.object(BaseConfig, '__getitem__', side_effect=KeyError)
    def test_missing_default_value(self, mock_getitem, config):
        key = mock.sentinel.key
        default = mock.sentinel.default

        result = config.get(key, default)

        assert result == default

    @mock.patch.object(BaseConfig, '__getitem__', return_value=mock.sentinel.v)
    def test_exists(self, mock_getitem, config):
        key = mock.sentinel.key

        result = config.get(key)

        assert result == mock_getitem.return_value
