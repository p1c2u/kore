kore
****

.. role:: strike
    :class: strike

.. image:: https://badge.fury.io/py/kore.png
    :target: http://badge.fury.io/py/kore

.. image:: https://travis-ci.org/p1c2u/kore.svg?branch=master
    :target: https://travis-ci.org/p1c2u/kore

.. image:: https://img.shields.io/codecov/c/github/p1c2u/kore/master.svg?style=flat
    :target: https://codecov.io/github/p1c2u/kore?branch=master

Kore - core app framework


Installation
============

Recommended way (via pip):

.. code-block:: bash

   $ pip install kore

Alternatively you can download the code and install from the repository:

.. code-block:: bash

   $ pip install -e git+https://github.com/p1c2u/kore.git#egg=kore


Testing
=======

Install packages required for testing:

.. code-block:: bash

   $ pip install -r requirements_dev.txt

Run tests with pytest:

.. code-block:: bash

   $ py.test

Alternatively:

.. code-block:: bash

   $ python setup.py test
 

Creating application
====================

Add kore to your package requirements:

.. code-block:: bash

   $ echo "kore" >> requirements.txt

Create your own application plugin (see `Creating component plugins`_) or use existing ones:

- kore-plugins-celery for `Celery`_ application
- kore-plugins-falcon for `Falcon`_ application


Creating component plugins
==========================

Create your plugin module:

.. code-block:: bash

   $ vi my_own_plugin.py

Every plugin can have many componenets. A component creates and returns a particular value or object. It has the ability to utilize an injected container to retrieve the necessary configuration settings and dependencies.

The container expects a component to adhere to the following rules:

1. It must be method.
2. It must accept the container as the only argument.
3. It must return anything except ``None``.

There are two types of component:
1. factory - non cached component. Return value is created on every call.
2. service - cached component. Return value is created only once.

Create plugin class inside plugin module which inherits from ``kore.components.plugins.BasePluginComponent`` class:

.. code-block:: python

   from kore.components.plugins import BasePluginComponent


   class MyOwnPlugin(BasePluginComponent):

Create ``get_factories`` method that returns two-element iterable with first element as component name and second factory function.

Create ``get_services`` method that returns two-element iterable with first element as component name and second service function.

.. code-block:: python

   class MyOwnPlugin(BasePluginComponent):

       def get_factories(self):
           return (
               ('my_own_component_1', self.my_own_component_1),
           )

       def get_services(self):
           return (
               ('my_own_component_2', self.my_own_component_2),
           )

       def my_own_component_1(self, container):
           return ComponentFactory()

       def my_own_component_2(self, container):
           return ComponentService()


Creating plugin hooks
---------------------

A component hook is one time components usage. Inside hooks you can connect them together or configure.

You can define the following hooks:

1. Pre hook - executed before all componenets are added.
2. Post hook - executed after all componenets are added.

The container expects a component hook to adhere to the following rules:

1. It must be method.
2. It must accept the container as the only argument.

Create ``post_hook`` method inside plugin class:

.. code-block:: python

   class MyOwnPlugin(BasePluginComponent):

       def post_hook(self, container):
           application = container('application')
           my_own_component_1 = container('my_project.my_own_component_1')

           application.add_signal('launched', my_own_component_1)

.. _Celery: http://www.celeryproject.org/
.. _Falcon: https://falconframework.org/


Enabling plugin
===============

Every plugin should have entry point(s) in `setup.py` to be enabled.

.. code-block:: python
   
    entry_points = """\
    [kore.components]
    my_project = my_own_plugin:MyOwnPlugin
    """

    setup(
        name='my_project',
        # ..
        entry_points=entry_points,
    )

Entry point name is plugin namespace. Every component inside the plugin will be registered under that namespace.
