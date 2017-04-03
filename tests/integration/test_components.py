class TestComponents(object):

    def test_services(self, container):
        assert container('test.service_1') == container('test.service_1')

    def test_services_related(self, container):
        assert container('test.service_1') == container('test.service_2')

    def test_factories(self, container):
        assert not container('test.factory_1') == container('test.factory_1')

    def test_factories_related(self, container):
        assert not container('test.factory_1') == container('test.factory_2')
