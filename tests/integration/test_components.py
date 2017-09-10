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

    def test_services(self, container):
        assert container('test.service_1') == container('test.service_1')

    def test_services_related(self, container):
        assert container('test.service_1') == container('test.service_2')

    def test_factories(self, container):
        assert not container('test.factory_1') == container('test.factory_1')

    def test_factories_related(self, container):
        assert not container('test.factory_1') == container('test.factory_2')


class TestComponentSignals(object):

    def test_pre_register(self, component_plugin_class, container_factory):
        receiver = Receiver()

        signals.pre_register.connect(receiver, sender=component_plugin_class)

        container = container_factory.create()
        assert receiver.instance is True
        assert receiver.sender == component_plugin_class
        assert receiver.container == container

    def test_post_register(self, component_plugin_class, container_factory):
        receiver = Receiver()

        signals.post_register.connect(receiver, sender=component_plugin_class)

        container = container_factory.create()
        assert receiver.instance is True
        assert receiver.sender == component_plugin_class
        assert receiver.container == container
