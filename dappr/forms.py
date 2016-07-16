from django.forms import fields
from django import forms
from django.contrib.auth import get_user_model


class PlaceholderInsteadOfLabelMixin(object):
    """
    A form mixin that replaces ugly text field <label>s with pretty HTML5 placeholders.
    """
    def __init__(self, *args, **kwargs):
        super(PlaceholderInsteadOfLabelMixin, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, forms.DateInput):
                    field.widget = forms.TextInput(attrs={'placeholder': field.label})
                    field.label = None


class RegistrationForm(forms.Form):
    """
    A form for the first step of user registration.
    User enters their desired username, along with their email address
    for identity confirmation.
    """

    username = fields.CharField(required=True)
    email = fields.EmailField(required=True)
    password = fields.CharField(widget=forms.PasswordInput)
    password1 = fields.CharField(widget=forms.PasswordInput, label="Re-enter password")

    def clean(self):
        # Get entered data
        cleaned_data = super(RegistrationForm, self).clean()

        # Check if passwords match
        password = cleaned_data.get("password")
        password1 = cleaned_data.get("password1")
        if password and password1 and password != password1:
            raise forms.ValidationError("Passwords do not match")

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
