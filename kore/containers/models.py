from knot import Container


class NamespacedContainer(Container):

    namespace_separator = '.'

    def __call__(self, *args, **kwargs):
        """A shortcut method for convenience.
        For more information see :meth:`Container.provide`.
        """
        return self.provide(*args, **kwargs)

    def provide(self, name, namespace=None):
        provider_name = self.get_provider_name(name, namespace=namespace)
        return super(NamespacedContainer, self).provide(provider_name)

    def get_provider_name(self, name, namespace=None):
        if namespace is None:
            return name

        return self.namespace_separator.join([namespace, name])
