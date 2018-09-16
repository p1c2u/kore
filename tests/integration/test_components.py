from datetime import datetime

import pytest

from kore.components import signals


class Receiver(object):

    def __init__(self):
        self.sender = None
        self.instance = False
        self.container = None

    def __call__(self, sender, instance, container):
        self.sender = sender
        self.instance = True
        self.container = container


class TestComponents(object):

    @pytest.fixture
    def factory_1(self):
        return lambda container: container('test.factory_2')

    @pytest.fixture
    def factory_2(self):
        return lambda container: datetime.utcnow()

    @pytest.fixture
    def service_1(self):
        return lambda container: container('test.service_2')

    @pytest.fixture
    def service_2(self):
        return lambda container: datetime.utcnow()

    @pytest.fixture
    def component_class(
            self, factory_1, factory_2, service_1, service_2, factory):
        return factory.create_component_class(
            name="TestComponent",
            factories={'factory_1': factory_1, 'factory_2': factory_2},
            services={'service_1': service_1, 'service_2': service_2},
        )

    @pytest.fixture
    def plugin_1(self, component_class, factory):
        return factory.create_plugin(
            name='test', component_class=component_class)

    @pytest.fixture
    def plugin_2(self, component_class, factory):
        return factory.create_plugin(
            name='test_2', component_class=component_class)

    @pytest.fixture(scope='session')
    def config_dict(self):
        return {'test': 'test'}

    @pytest.fixture
    def container(self, plugin_1, plugin_2, config_dict, factory):
        return factory.create_container(
            plugins_iterator=[plugin_1, plugin_2], config_dict=config_dict)

    def test_services(self, container):
        assert container('test.service_1') == container('test.service_1')

    def test_services_related(self, container):
        assert container('test.service_1') == container('test.service_2')

    def test_factories(self, container):
        assert not container('test.factory_1') == container('test.factory_1')

    def test_factories_related(self, container):
        assert not container('test.factory_1') == container('test.factory_2')


class TestComponentPreRegister(object):

    @pytest.fixture
    def pre_hook(self):
        return lambda self, container: container

    @pytest.fixture
    def component_class(self, pre_hook, factory):
        return factory.create_component_class(
            name="TestComponent", pre_hook=pre_hook)

    @pytest.fixture
    def plugin(self, component_class, factory):
        return factory.create_plugin(
            name='test', component_class=component_class)

    @pytest.fixture
    def container_factory(self, plugin, factory):
        return factory.create_container_factory(plugins_iterator=[plugin, ])

    def test_received(self, component_class, container_factory):
        receiver = Receiver()

        signals.pre_register.connect(receiver, sender=component_class)

        container = container_factory.create()
        assert receiver.instance is True
        assert receiver.sender == component_class
        assert receiver.container == container


class TestComponentPostRegister(object):

    @pytest.fixture
    def post_hook(self):
        return lambda self, container: container

    @pytest.fixture
    def component_class(self, post_hook, factory):
        return factory.create_component_class(
            name="TestComponent", post_hook=post_hook)

    @pytest.fixture
    def plugin(self, component_class, factory):
        return factory.create_plugin(
            name='test', component_class=component_class)

    @pytest.fixture
    def container_factory(self, plugin, factory):
        return factory.create_container_factory(plugins_iterator=[plugin, ])

    def test_received(self, component_class, container_factory):
        receiver = Receiver()

        signals.post_register.connect(receiver, sender=component_class)

        container = container_factory.create()
        assert receiver.instance is True
        assert receiver.sender == component_class
        assert receiver.container == container
