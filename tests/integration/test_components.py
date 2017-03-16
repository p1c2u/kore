class TestComponents(object):

    def test_services(self, container):
        assert container('test.service') == container('test.service')

    def test_factory(self, container):
        assert not container('test.factory') == container('test.factory')
