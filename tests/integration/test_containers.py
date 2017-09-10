import mock


class TestContainersProvide(object):

    def test_namespace(self, container):
        assert container('test.service_1') ==\
            container('service_1', namespace='test')
        assert container('test.service_2') ==\
            container('service_2', namespace='test')

        assert container('test_2.service_1') ==\
            container('service_1', namespace='test_2')
        assert container('test_2.service_2') ==\
            container('service_2', namespace='test_2')


class TestContainersAddFactory(object):

    def test_namespace(self, container):
        container.add_factory(
            lambda x: mock.sentinel.factory, 'service_3', namespace='test_3')

        assert container('test_3.service_3') == mock.sentinel.factory


class TestContainersAddService(object):

    def test_namespace(self, container):
        container.add_service(
            lambda x: mock.sentinel.service, 'service_3', namespace='test_3')

        assert container('test_3.service_3') == mock.sentinel.service
