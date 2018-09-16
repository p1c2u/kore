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
    def service(self):
        return lambda container: container

    def test_namespace(self, service, factory):
        service_name = 'service'
        component_class = factory.create_component_class(
            name="TestComponent",
            services={service_name: service},
        )
        plugin_namespace = 'test'
        plugin = factory.create_plugin(
            name=plugin_namespace, component_class=component_class)
        container = factory.create_container(
            plugins_iterator=[plugin, ])

        assert container('test.service') ==\
            container(service_name, namespace=plugin_namespace)


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

    def test_container_prepared(self, container_factory):
        receiver = Receiver()

        signals.container_prepared.connect(receiver)

        container = container_factory.create()
        assert receiver.container == container
