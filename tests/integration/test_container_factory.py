class TestContainerFactory(object):

    def test_initial_components(self, container_factory):
        config = {}

        components = {
            'config': config,
            'foo': 'bar',
            'bar': 'baz',
        }

        container = container_factory.create(**components)

        assert container('config') == config
        assert container('foo') == 'bar'
        assert container('bar') == 'baz'
