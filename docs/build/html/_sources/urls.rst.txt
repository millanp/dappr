==========
URL routes
==========


.. _registrationurl:
Registration URL
----------------

+--------------------+--------------------------------------------------------+-----------------------------+
| Route              | View                                                   | Name                        |
+====================+========================================================+=============================+
| :code:`'register'` | :ref:`dappr.views.RegistrationView <registrationview>` | :code:`'registration_view'` |
+--------------------+--------------------------------------------------------+-----------------------------+
	
Routes to the view that displays and handles the registration form

.. _emailconfirmationurl:
Email confirmation URL
----------------------

+----------------------------------------+--------------------------------------------------------+-----------------------------+
| Route                                  | View                                                   | Name                        |
+========================================+========================================================+=============================+
| :code:`'confirm/(?P<conf_key>[0-9]+)'` | :ref:`dappr.views.EmailConfirmView <emailconfirmview>` | :code:`'confirmation_view'` |
+----------------------------------------+--------------------------------------------------------+-----------------------------+
	
Using the provided confirmation key, routes to the view that sets the user's identity confirmation status to confirmed, and displays a success message.
