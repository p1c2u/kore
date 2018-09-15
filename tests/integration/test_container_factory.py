import pytest


class TestContainerFactory(object):

    @pytest.fixture
    def container_factory(self, plugin_1, plugin_2, factory):
        return factory.create_container_factory(
            plugins_iterator=[plugin_1, plugin_2])

    def test_initial_components(self, container_factory):
        components = {
            'foo': 'bar',
            'bar': 'baz',
        }

        container = container_factory.create(**components)

        assert container('foo') == 'bar'
        assert container('bar') == 'baz'
