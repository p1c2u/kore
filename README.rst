kore
****

Kore


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

Create your own application plugin (see `Creating plugins`_) or use existing ones:

- kore-plugins-falcon for Falcon application
- kore-plugins-wimq for WIMQ application
