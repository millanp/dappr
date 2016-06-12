============
Installation
============

1. Install the package::

	pip install dappr

2. Add it to your INSTALLED_APPS::

	INSTALLED_APPS = [
		...
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'dappr',
	]

3. Migrate the database::

	python manage.py migrate