from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, mail_admins
from django.template.loader import render_to_string
from django.contrib.sites.models import Site

# Create your models here.
class RegistrationProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    identity_confirmed = models.BooleanField(default=False)
    confirmation_key = models.CharField(max_length=20, null=True, blank=True)
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    def send_user_confirmation(self):
        self.confirmation_key = get_random_string(length=20, allowed_chars='0123456789')
        self.save()
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
        self.identity_confirmed = True
        self.save()
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
        context = {
           "site": Site.objects.get(pk=settings.SITE_ID),
        }
        self.user.email_user(
            render_to_string("registration/success_email_subject.txt", context=context),
            render_to_string("registration/success_email.html", context=context),
            html_message=render_to_string("registration/success_email.html", context=context),           
        )
    def send_rejection_notification(self):
        context = {
            "site": Site.objects.get(pk=settings.SITE_ID),
        }
        self.user.email_user(
            render_to_string("registration/rejection_email_subject.txt", context=context),
            render_to_string("registration/rejection_email.html", context=context),
            html_message=render_to_string("registration/rejection_email.html", context=context),           
        )