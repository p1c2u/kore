import pytest


class TestComponentRegistrarBind(object):

    @pytest.fixture
    def factory_1(self):
        return lambda container: container('test.factory_2')

    @pytest.fixture
    def factory_2(self):
        return lambda container: container

    @pytest.fixture
    def service_1(self):
        return lambda container: container('test.service_2')

    @pytest.fixture
    def service_2(self):
        return lambda container: container

    @pytest.fixture
    def post_hook(self):
        return lambda self, container: container('test.service_1')

    @pytest.fixture
    def component_class(
            self,
            factory_1, factory_2, service_1, service_2, post_hook,
            factory,
    ):
        return factory.create_component_class(
            name="TestComponent",
            factories={'factory_1': factory_1, 'factory_2': factory_2},
            services={'service_1': service_1, 'service_2': service_2},
            post_hook=post_hook,
        )

    @pytest.fixture
    def plugin_1(self, component_class, factory):
        return factory.create_plugin(
            name='test', component_class=component_class)

    @pytest.fixture
    def plugin_2(self, component_class, factory):
        return factory.create_plugin(
            name='test_2', component_class=component_class)

    @pytest.fixture
    def component_registrar(self, factory):
        return factory.create_component_registrar()

    @pytest.fixture
    def component_1(self, plugin_1, factory):
        return factory.create_component(plugin=plugin_1)

    @pytest.fixture
    def component_2(self, plugin_2, factory):
        return factory.create_component(plugin=plugin_2)

    @pytest.fixture
    def container(self, factory):
        return factory.create_container()

    def test_registered_single(
            self, component_registrar, container, component_1):
        component_registrar.register(container, component_1)

        result = component_registrar.bind(container)

        assert result is None

    def test_registered_related(
            self, component_registrar, container, component_1, component_2):
        component_registrar.register(container, component_1)
        component_registrar.register(container, component_2)

        result = component_registrar.bind(container)

        assert result is None

    def test_registered_reversed(
            self, component_registrar, container, component_1, component_2):
        component_registrar.register(container, component_2)
        component_registrar.register(container, component_1)

        result = component_registrar.bind(container)

        assert result is None
