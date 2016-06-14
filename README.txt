Dappr is a Django app for filtered user registration, requiring each user that requests an account to be approved by the site administrator before gaining an enabled user profile.

The workflow to register a user looks like this:
	1. User registers at site, providing all details except password. Recieves a notification to check their email in order to set password.
	2. User opens email, clicks link (confirming identity), then enters password at site. Receives email telling them that their registration request is complete, and the admin will see to it as soon as possible.
	3. Notification is sent to admin of a new user request. Admin goes to django admin site, and on the RegistrationProfile page, performs the "Approve" action on whichever requests they want to approve.
	4. The user now has a working account with all of the information they entered at the beginning! Email notification is sent to user informing them of the admin's decision, and welcoming them to the site.

This ordering of the steps to registration is very important. Notice that the identity confirmation email is sent immediately after the user registers, rather than after the admin approves them. This kills two birds with one stone; the risk of phishing attacks is greatly diminished, because the user is expecting the password set email the moment they receive it, and the admin is safe in the knowledge that the email address of the user they are approving is the actual address of that user.

I am in the process of posting the docs for this package, but in the meantime, here are some simple steps for setup:
	1. Add "dappr" to INSTALLED_APPS
	2. Migrate database
	3. Add include(dappr.urls) to your urlpatterns
	4. Visit <path_to_dappr_urls>/register/ to test it out!