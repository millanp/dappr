from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string
from django.core.mail import mail_admins
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model

class RegistrationProfile(models.Model):
    """
    A model to store information about ongoing account requests.
    Associated (OneToOne) with a puppet User instance, which will be manipulated through
    this package during the registration process.
    """
    
    # The User object associated with this profile. 
    # Only activated once account request approved.
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    
    # Whether or not the user has confirmed their identity through the emailed link
    # to the password set form
    identity_confirmed = models.BooleanField(default=False)
    
    # Key sent with password set email to user in order to match them with their profile
    confirmation_key = models.CharField(max_length=20, null=True, blank=True)
    
    # Whether or not this account request has been approved by an administrator
    approved = models.BooleanField(default=False)
    
    # Whether or not this is an active request
    # (requests are made inactive when an admin has takes action on them)
    active = models.BooleanField(default=True)
    
    def send_user_confirmation(self):
        """
        Called after user completes initial registration form.
        Generate a confirmation key, then
        send an email to the associated user with a link (containing the key) 
        to a form allowing them to set their password and confirm their identity.
        """
        
        # Generate and set a random confirmation key
        self.confirmation_key = get_random_string(length=20, allowed_chars='0123456789')
        self.save()
        
        # Use appropriate email templates to generate and send the email
        context = {
            "site": Site.objects.get(pk=settings.SITE_ID),
            "conf_key": self.confirmation_key,
        }
        self.user.email_user(
            render_to_string("registration/confirmation_email_subject.txt", context=context),
            render_to_string("registration/confirmation_email.html", context=context),
            html_message=render_to_string("registration/confirmation_email.html", context=context),
        )

    def send_admin_notification(self):
        """
        Called after user confirms identity and sets password. 
        Set identity confirmed to true, then send an email to the admin to notify
        them that someone requested an account at their site.
        """
        
        # Set identity confirmed to true
        self.identity_confirmed = True
        self.save()
        
        # Use appropriate email templates to generate and send the email
        context = {
           "site": Site.objects.get(pk=settings.SITE_ID),
           "user": self.user
        }
        mail_admins(
            render_to_string("registration/admin_notification_email_subject.txt", context=context),
            render_to_string("registration/admin_notification_email.html", context=context),
            html_message=render_to_string("registration/admin_notification_email.html", context=context),
        )

    def send_approval_notification(self):
        """
        Called after admin approves account request.
        Send email notification to user that they can now use the website.
        """
        
        # Use appropriate email templates to generate and send the email
        context = {
           "site": Site.objects.get(pk=settings.SITE_ID),
        }
        self.user.email_user(
            render_to_string("registration/success_email_subject.txt", context=context),
            render_to_string("registration/success_email.html", context=context),
            html_message=render_to_string("registration/success_email.html", context=context),           
        )

    def send_rejection_notification(self):
        """
        Called after admin rejects account request.
        Send email notification to user that their account request has been rejected.
        """
        
        # Use appropriate email templates to generate and send the email
        context = {
            "site": Site.objects.get(pk=settings.SITE_ID),
        }
        self.user.email_user(
            render_to_string("registration/rejection_email_subject.txt", context=context),
            render_to_string("registration/rejection_email.html", context=context),
            html_message=render_to_string("registration/rejection_email.html", context=context),           
        )