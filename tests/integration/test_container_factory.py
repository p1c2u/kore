class TestContainerFactory(object):

    def test_initial_components(self, container_factory):
        components = {
            'foo': 'bar',
            'bar': 'baz',
        }

        container = container_factory.create(**components)

        assert container('foo') == 'bar'
        assert container('bar') == 'baz'
