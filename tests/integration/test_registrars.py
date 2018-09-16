import pytest


class TestComponentRegistrarBind(object):

    @pytest.fixture
    def service(self):
        return lambda container: container

    @pytest.fixture
    def component_registrar(self, factory):
        return factory.create_component_registrar()

    @pytest.fixture
    def container(self, factory):
        return factory.create_container()

    def test_single(self, component_registrar, container, service, factory):
        component_class = factory.create_component_class(
            name="TestComponent",
            services={'service': service},
            post_hook=lambda self, container: container('test.service'),
        )
        plugin = factory.create_plugin(
            namespace='test', component_class=component_class)
        component = factory.create_component(plugin=plugin)
        component_registrar.register(container, component)

        result = component_registrar.bind(container)

        assert result is None

    def test_related(
            self, component_registrar, container, service, factory):
        component_class = factory.create_component_class(
            name="TestComponent",
            services={'service': service},
            post_hook=lambda self, container: container('test_2.service'),
        )
        plugin_1 = factory.create_plugin(
            namespace='test_1', component_class=component_class)
        plugin_2 = factory.create_plugin(
            namespace='test_2', component_class=component_class)
        component_1 = factory.create_component(plugin=plugin_1)
        component_2 = factory.create_component(plugin=plugin_2)
        component_registrar.register(container, component_1)
        component_registrar.register(container, component_2)

        result = component_registrar.bind(container)

        assert result is None

    def test_reversed(
            self, component_registrar, container, service, factory):
        component_class = factory.create_component_class(
            name="TestComponent",
            services={'service': service},
            post_hook=lambda self, container: container('test_2.service'),
        )
        plugin_1 = factory.create_plugin(
            namespace='test_1', component_class=component_class)
        plugin_2 = factory.create_plugin(
            namespace='test_2', component_class=component_class)
        component_1 = factory.create_component(plugin=plugin_1)
        component_2 = factory.create_component(plugin=plugin_2)
        component_registrar.register(container, component_2)
        component_registrar.register(container, component_1)

        result = component_registrar.bind(container)

        assert result is None

    def test_bind_related(
            self, component_registrar, container, service, factory):
        def post_hook_1(self, container):
            self.value = True

        def post_hook_2(self, container):
            container('service', namespace='test_1')
        component_class_1 = factory.create_component_class(
            name="TestComponent",
            post_hook=post_hook_1,
        )
        component_class_2 = factory.create_component_class(
            name="TestComponent",
            post_hook=post_hook_2,
        )
        plugin_1 = factory.create_plugin(
            namespace='test_1', component_class=component_class_1)
        plugin_2 = factory.create_plugin(
            namespace='test_2', component_class=component_class_2)
        component_1 = factory.create_component(plugin=plugin_1)
        component_2 = factory.create_component(plugin=plugin_2)
        component_registrar.register(container, component_1)
        component_registrar.register(container, component_2)
        container.add_service(
            lambda container: component_1.value, 'service', plugin_1.namespace)

        result = component_registrar.bind(container)

        assert result is None

    @pytest.mark.xfail(reason="No dependencies resolving")
    def test_bind_reversed(
            self, component_registrar, container, service, factory):
        def post_hook_1(self, container):
            self.value = True

        def post_hook_2(self, container):
            container('service', namespace='test_1')
        component_class_1 = factory.create_component_class(
            name="TestComponent",
            post_hook=post_hook_1,
        )
        component_class_2 = factory.create_component_class(
            name="TestComponent",
            post_hook=post_hook_2,
        )
        plugin_1 = factory.create_plugin(
            namespace='test_1', component_class=component_class_1)
        plugin_2 = factory.create_plugin(
            namespace='test_2', component_class=component_class_2)
        component_1 = factory.create_component(plugin=plugin_1)
        component_2 = factory.create_component(plugin=plugin_2)
        component_registrar.register(container, component_2)
        component_registrar.register(container, component_1)
        container.add_service(
            lambda container: component_1.value, 'service', plugin_1.namespace)

        result = component_registrar.bind(container)

        assert result is None
