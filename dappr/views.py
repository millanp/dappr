from django.shortcuts import render
from django.views.generic import edit
from django.views.generic import base
from dappr import forms
from braces.views import FormValidMessageMixin
from dappr.models import RegistrationProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.http.response import Http404
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class EmailConfirmView(base.TemplateView):
    template_name = 'registration/email_confirmed.html'

    def get_registration_profile(self):
        r = RegistrationProfile.objects.get(confirmation_key=self.kwargs['conf_key'])
        return r

    def get(self, *args, **kwargs):
        if self.get_registration_profile().identity_confirmed:
            return render(self.request, 'registration/invalid_confirmation_code.html')
        self.get_registration_profile().send_admin_notification(self.request)
        return super(EmailConfirmView, self).get(self, *args, **kwargs)


class RegistrationForm(FormValidMessageMixin, edit.FormView):
    template_name = 'registration/registration_form.html'
    form_class = forms.RegistrationForm
    success_url = "#"# reverse('login')
    form_valid_message = "Please check your email to confirm your address"

    def form_valid(self, form):
        data = form.cleaned_data
        del data['password1']
        user = get_user_model().objects.create_user(**data)
        user.set_unusable_password()
        user.is_active = False
        user.save()
        reg_profile = RegistrationProfile.objects.create(user=user)
        reg_profile.send_user_confirmation(self.request)
        return super(RegistrationForm, self).form_valid(form)