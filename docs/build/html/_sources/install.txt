============
Installation
============

1. Install the package::

.. code-block:: python

	pip install dappr

2. Add it to your INSTALLED_APPS::

.. code-block:: python

	INSTALLED_APPS = [
		...
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'dappr',
	]

3. Migrate the database::

.. code-block:: python

	python manage.py migrate