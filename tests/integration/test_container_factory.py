import pytest


class TestContainerFactory(object):

    @pytest.fixture
    def container_factory(self, factory):
        return factory.create_container_factory()

    def test_initial_components(self, container_factory):
        components = {
            'foo': 'bar',
            'bar': 'baz',
        }

        container = container_factory.create(**components)

        assert container('foo') == 'bar'
        assert container('bar') == 'baz'
