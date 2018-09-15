import pytest


class TestComponentRegistrarBind(object):

    @pytest.fixture
    def component_registrar(self, factory):
        return factory.create_component_registrar()

    @pytest.fixture
    def component_1(self, plugin_1, factory):
        return factory.create_component(component_plugin=plugin_1)

    @pytest.fixture
    def component_2(self, plugin_2, factory):
        return factory.create_component(component_plugin=plugin_2)

    @pytest.fixture
    def container(self, factory):
        return factory.create_container()

    def test_registered_single(
            self, component_registrar, container, component_1):
        component_registrar.register(container, component_1)

        component_registrar.bind(container)

    def test_registered_related(
            self, component_registrar, container, component_1, component_2):
        component_registrar.register(container, component_1)
        component_registrar.register(container, component_2)

        component_registrar.bind(container)

    def test_registered_reversed(
            self, component_registrar, container, component_1, component_2):
        component_registrar.register(container, component_2)
        component_registrar.register(container, component_1)

        component_registrar.bind(container)
