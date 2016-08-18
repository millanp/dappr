=====
Views
=====

.. class:: RegistrationView
    
    Subclass of `FormView <https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-editing/#formview>`_.
    Uses `SuccessMessageMixin <https://docs.djangoproject.com/en/1.9/ref/contrib/messages/#django.contrib.messages.views.SuccessMessageMixin>`_ to display success messages.

    To customize this view, override the following attributes and methods:

    .. attribute:: template_name

        The template used to display the user registration form. Defaults to ``'registration/registration_form.html'``

        Context passed to template:

            ``form``: Instance of ``RegistrationView.form_class`` 
            (which by default is ``dappr.forms.RegistrationForm``)

            ``messages``: List of messages to be displayed. This will include 
            the success message given upon submission of the form.
            For more information on Django's messaging system, click 
            `here <https://docs.djangoproject.com/en/1.10/ref/contrib/messages/>`_.

    .. attribute:: form_class

        The form class to be used in the registration template.
        Must be a subclass of 'django.forms.Form'.
        Defaults to ``dappr.forms.RegistrationForm``.

    .. attribute:: success_url

        If you use ``dappr``'s recommended workflow, in which the success message
        for the registration form is displayed right in the registration form template,
        there is no need to override this attribute. 

        However, if you don't like it, you
        can override success_url to route the user to a separate URL upon successfully 
        submitting the form.
        Defaults to ``'#'.``

    .. attribute:: success_message

        The message to be displayed upon successful form submission.
        Defaults to ``'Please check your email to confirm your address'``


    .. method:: get