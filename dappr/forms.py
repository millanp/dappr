from django.forms import fields
from django import forms
from django.contrib.auth import get_user_model


class PlaceholdersInsteadOfLabelsMixin(object):
    """Untested!!!"""
    def __init__(self, arg):
        for field in self.fields.values():
            field.widget.attrs["placeholder"] = field.label
            del field.label
        super(PlaceholdersInsteadOfLabelsMixin, self).__init__()


class RegistrationForm(forms.Form):
    """
    A form for the first step of user registration.
    User enters their desired username, along with their email address
    for identity confirmation.
    """

    username = fields.CharField(required=True)
    email = fields.EmailField(required=True)
    email1 = fields.EmailField(required=True, label="Re-enter email")

    def clean(self):
        # Get entered data
        cleaned_data = super(RegistrationForm, self).clean()

        # Check if email addresses match
        email = cleaned_data.get("email")
        email1 = cleaned_data.get("email1")
        if email and email1 and email != email1:
            raise forms.ValidationError("Email addresses do not match")

        # Check if username is in use
        username = cleaned_data.get("username")
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError("Username is taken")


class RegistrationFormUniqueEmail(RegistrationForm):
    """
    Subclass of RegistrationForm to prevent users from creating two accounts
    with the same email address.
    """
    def clean_email(self):
        """
        Make sure that no existing Users have the same email
        """
        duplicates = get_user_model().objects.filter(email__iexact=self.cleaned_data['email'])
        if duplicates.exists():
            raise forms.ValidationError("This email address is already taken.")
        return self.cleaned_data['email']
