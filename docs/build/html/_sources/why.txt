==============
Why use Dappr?
==============

Purpose
-------

:code:`dappr` provides a user registration system with an admin approval step.
Sound familiar? That is because the purpose of :code:`dappr` is very similar to
that of `django-inspectional-registration <https://github.com/lambdalisue/django-inspectional-registration>`_, a popular app based off of 
`django-registration <https://github.com/ubernostrum/django-registration/>`_ that
does just that.

What makes Dappr better?
------------------------

Simplicity and Comprehensibility
~~~~~~~~~~

To put it simply, the other options are bloated, unintuitive, and insecure.
To avoid the first two, :code:`dappr` was built from scratch to only
support :code:`Django>=1.8`. This is because 1.8 is the first LTS version of Django that does not rely on South for database migration, allowing us to eliminate lots of cumbersome compatibility checks and provisions.

We have tried to make the code of :code:`dappr` as easy-to-follow and commented as possible, so that if you want to tweak it, forking and modifying is easy.

Security
~~~~~~~~

It is also much more secure than :code:`django-inspectional-registration`. This is what their process of user registration looks like:

	#. User fills out registration form, providing all necessary details except desired password

	#. Admin is sent an email notifying them of a new account request

	#. Admin approves/rejects the account request

	#. If they approve the request, user is sent an email that allows them to set their password

	#. User sets password, activating their account

Do you see the risk here? Think about step 4 of this process. When the user receives this email, it will always come out of the blue, whenever the admin finds the time to approve or reject their request. This email demands an action that can only be performed by clicking a link in the email. This means that there is a great inherent risk of phishing with this system.

Not only this, but the admin approving the accounts, the one that supposedly can make an informed choice about who to let in to the website, has no idea whether the email of a potential user is legitimate. The primary purpose of the email-sent password setting link is to verify the user's identity. If this step takes place after the admin has approved the user, disastrous things can happen.

Here is :code:`dappr`'s approach to user registration:

	#. User fills out registration form, providing all necessary details including password. They are told to check their email for a confirmation link.

	#. User clicks link in email, confirming email address.

	#. Admin is sent an email notifying them of a new account request

	#. Admin approves/rejects the account request, either activating or deleting the user's account.
	
Simply by reordering the steps of user registration, the two security risks are eliminated. Not only this, but registration is made easier for both the user and the admin: the user only has to do one chunk of work all at once, and the admin will never have to wait for a user to set their password after they have approved their account.

No "*_complete" templates
~~~~~~~~~~~~~~~~~~~~~~~~~

One kind of annoying thing I noticed while using Django is that a lot of the time, you need to provide two templates to display any form: one with the form itself, and one with the success message. In dappr, the success message is provided as a django message to the original template. 