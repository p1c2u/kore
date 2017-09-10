class TestContainers(object):

    def test_namespace(self, container):
        assert container('test.service_1') ==\
            container('service_1', namespace='test')
        assert container('test.service_2') ==\
            container('service_2', namespace='test')

        assert container('test_2.service_1') ==\
            container('service_1', namespace='test_2')
        assert container('test_2.service_2') ==\
            container('service_2', namespace='test_2')
