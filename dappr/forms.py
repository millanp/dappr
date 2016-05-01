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