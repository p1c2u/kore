class ComponentFactory(object):

    def create(self, component_class, namespace):
        return component_class(namespace=namespace)
