=====
Views
=====

.. class:: registration.views.RegistrationView
    
    Subclass of `FormView <https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/#formview>`_.
    Uses `SuccessMessageMixin <https://docs.djangoproject.com/en/1.9/ref/contrib/messages/#django.contrib.messages.views.SuccessMessageMixin>`_ to push success messages.

    ``RegistrationView`` handles initial user registration, in which the user enters all of their desired account information (username, password, etc.) It both displays the form and handles form submissions.

    To customize this view, override the following attributes and methods:

    .. attribute:: template_name

        Default: ``'registration/registration_form.html'``

        The template used to display the user registration form. 

        Context passed to template:

            ``form``: Instance of ``RegistrationView.form_class`` 
            (which by default is ``dappr.forms.RegistrationForm``)

            ``messages``: List of messages to be displayed. This will include 
            the success message given upon submission of the form.
            For more information on Django's messaging system, click 
            `here <https://docs.djangoproject.com/en/1.10/ref/contrib/messages/>`_.

    .. attribute:: form_class

        Default: ``dappr.forms.RegistrationForm``

        The form class to be used in the registration template.
        Must be a subclass of 'django.forms.Form'.

    .. attribute:: success_url

        Default: ``'#'.``

        The URL to redirect the user after a successful registration.
        Note that this must be a true URL, not the name of a URL pattern.

    .. attribute:: success_message

        Default: ``'Please check your email to confirm your address'``

        The message to be displayed upon successful form submission.


    .. method:: get_form_class()

        Use this method to determine the form class on a request-by-request
        basis. Must return a descendent of ``django.forms.Form``.

    .. method:: get_success_url()

        Use this method to determine the success url on a request-by-request
        basis. Must return a valid URL string.

    .. method:: pre_registration()

        Called before initial user registration takes place.

    .. method:: post_registration()

        Called after initial user registration takes place.

.. class:: EmailConfirmView
    
    Subclass of `TemplateView <https://docs.djangoproject.com/en/1.9/ref/class-based-views/base/#templateview>`_

    ``EmailConfirmView`` handles GET requests sent by email confirmation links. When one is received with a valid confirmation code, the corresponding ``RegistrationProfile.identity_confirmed`` is set to ``True``, and the site admins are notified via email that someone has requested an account. 

    .. attribute:: template_name

        Default: ``'registration/email_confirmed.html'``

        The template used to display the email confirmation success message.

        No extra context is passed to this template.

    .. method:: pre_confirmation()

        Called before the account status is changed and the admins are notified.

    .. method:: post_confirmation()

        Called after the account status is changed and the admins are notified.