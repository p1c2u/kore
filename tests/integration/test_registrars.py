import pytest

from knot import Container


class TestComponentRegistrarBind(object):

    @pytest.fixture
    def component_1(self, component_factory, component_plugin_1):
        return component_factory.create(component_plugin_1.plugin)

    @pytest.fixture
    def ns_1(self, component_plugin_1):
        return component_plugin_1.name

    @pytest.fixture
    def component_2(self, component_factory, component_plugin_2):
        return component_factory.create(component_plugin_2.plugin)

    @pytest.fixture
    def ns_2(self, component_plugin_2):
        return component_plugin_2.name

    @pytest.fixture
    def container(self):
        return Container()

    def test_registered_single(
            self, component_registrar, container, component_1, ns_1):
        component_registrar.register(container, component_1, ns_1)

        component_registrar.bind(container)

    def test_registered_related(
            self, component_registrar, container, component_1, component_2,
            ns_1, ns_2):
        component_registrar.register(container, component_1, ns_1)
        component_registrar.register(container, component_2, ns_2)

        component_registrar.bind(container)

    def test_registered_reversed(
            self, component_registrar, container, component_1, component_2,
            ns_1, ns_2):
        component_registrar.register(container, component_2, ns_2)
        component_registrar.register(container, component_1, ns_1)

        component_registrar.bind(container)
