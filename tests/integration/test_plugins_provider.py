class TestPuglinsProviderAll(object):

    def test_returns_list(self, component_plugins_provider, component_plugin):
        result = component_plugins_provider.all()

        assert list(result) == [
            (component_plugin.name, component_plugin.plugin),
        ]


class TestPuglinsProviderFilter(object):

    def test_not_filtered(self, component_plugins_provider, component_plugin):
        filtered = component_plugin.name + '123'
        result = component_plugins_provider.filter(filtered)

        assert list(result) == []

    def test_filtered(self, component_plugins_provider, component_plugin):
        filtered = component_plugin.name
        result = component_plugins_provider.filter(filtered)

        assert list(result) == [
            (component_plugin.name, component_plugin.plugin),
        ]
