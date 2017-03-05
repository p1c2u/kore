from kore import container_factory


class TestContainerFactory(object):

    def test_initial_components(self):
        components = {
            'foo': 'bar',
            'bar': 'baz',
        }

        container = container_factory.create(**components)

        assert container('foo') == 'bar'
        assert container('bar') == 'baz'
