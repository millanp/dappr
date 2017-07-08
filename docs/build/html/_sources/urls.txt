==================
URLs used by Dappr
==================

Registration URL
----------------

.. method:: url(r'register', views.RegistrationForm.as_view(), name='registration_view')
	
	Routes to the view that displays and handles the registration form

Email confirmation URL
----------------------

.. method:: url(r'confirm/(?P<conf_key>[0-9]+)', views.EmailConfirmView.as_view(), name='confirmation_view')
	
	Using the provided confirmation key, routes to the view that sets the user's identity confirmation status to confirmed, and displays a success message.
