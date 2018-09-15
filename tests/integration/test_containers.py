import mock
import pytest

from kore.containers import signals


class Receiver(object):

    def __init__(self):
        self.container = None

    def __call__(self, sender, container):
        self.container = container


class TestContainersProvide(object):

    @pytest.fixture
    def container(self, plugin_1, plugin_2, factory):
        return factory.create_container(
            plugins_iterator=[plugin_1, plugin_2])

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

    @pytest.fixture
    def container(self, factory):
        return factory.create_container()

    def test_namespace(self, container):
        container.add_factory(
            lambda x: mock.sentinel.factory, 'service_3', namespace='test_3')

        assert container('test_3.service_3') == mock.sentinel.factory


class TestContainersAddService(object):

    @pytest.fixture
    def container(self, factory):
        return factory.create_container()

    def test_namespace(self, container):
        container.add_service(
            lambda x: mock.sentinel.service, 'service_3', namespace='test_3')

        assert container('test_3.service_3') == mock.sentinel.service


class TestCContainerSignals(object):

    @pytest.fixture
    def container_factory(self, factory):
        return factory.create_container_factory()

    def test_container_prepared(self, component_class, container_factory):
        receiver = Receiver()

        signals.container_prepared.connect(receiver)

        container = container_factory.create()
        assert receiver.container == container
