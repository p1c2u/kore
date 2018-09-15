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


class BaseTestComponents(object):

    @pytest.fixture(scope='session')
    def config_dict(self):
        return {'test': 'test'}

    @pytest.fixture(scope='session')
    def dict_config(self, config_dict, factory):
        return factory.create_dict_config(config_dict=config_dict)


class TestComponents(BaseTestComponents):

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


class TestComponentSignals(BaseTestComponents):

    @pytest.fixture
    def container_factory(self, plugin_1, plugin_2, factory):
        return factory.create_container_factory(
            plugins_iterator=[plugin_1, plugin_2])

    def test_pre_register(self, component_class, container_factory):
        receiver = Receiver()

        signals.pre_register.connect(receiver, sender=component_class)

        container = container_factory.create()
        assert receiver.instance is True
        assert receiver.sender == component_class
        assert receiver.container == container

    def test_post_register(self, component_class, container_factory):
        receiver = Receiver()

        signals.post_register.connect(receiver, sender=component_class)

        container = container_factory.create()
        assert receiver.instance is True
        assert receiver.sender == component_class
        assert receiver.container == container
