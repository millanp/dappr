============
Installation
============

    1. Install the package

    .. code-block:: python

    	pip install dappr

    2. Add it to your INSTALLED_APPS

    .. code-block:: python

    	INSTALLED_APPS = [
    		...
    		'django.contrib.messages',
    		'django.contrib.staticfiles',
    		'dappr',
    	]

    3. Make sure that the builtin django auth urls are activated. Remember that you will need to write `some templates <https://docs.djangoproject.com/en/1.9/topics/auth/default/#all-authentication-views>`_ for these urls to work properly!

    .. code-block:: python

        urlpatterns = [
            ...
            url(r'^auth/', include('django.contrib.auth.urls')),
        ]

    4. Include the dappr urls

    .. code-block:: python

        urlpatterns = [
            ...
            url(r'^auth/', include('django.contrib.auth.urls')),
            url(r'^registration/', include('dappr.urls')),
        ]

    5. Set up email sending in Django. This will probably involve getting an account with an SMTP service like `SendGrid <https://sendgrid.com/>`_, then following their instructions. In SendGrid's case, you will need to add the following to your settings.py:

    .. code-block:: python

        ...
        EMAIL_HOST = 'smtp.sendgrid.net'
        # Make sure this information is not committed to a public repo!
        EMAIL_HOST_USER = 'sendgrid_username'
        EMAIL_HOST_PASSWORD = 'sendgrid_password'
        EMAIL_PORT = 587
        EMAIL_USE_TLS = True

    6. Set your ADMINS

    .. code-block:: python

        ...
        ADMINS = (('username', 'email'),)

    7. Test your email setup.
    If you are using :code:`Django>=1.9`, you can use this handy command.

    .. code-block:: python
        
        python manage.py sendtestemail --admins

    8. Migrate the database

    .. code-block:: python

    	python manage.py migrate