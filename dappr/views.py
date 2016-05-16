from django.shortcuts import render
from django.views.generic import edit
from dappr import forms
from braces.views import FormValidMessageMixin
from dappr.models import RegistrationProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.http.response import Http404
from django.core.urlresolvers import reverse_lazy

# Create your views here.
# class Confirmation
class UserPasswordUpdate(FormValidMessageMixin, edit.UpdateView):
    model = get_user_model()
    template_name = 'registration/user_password_set_form.html'
    form_class = SetPasswordForm
    form_valid_message = ("We will review your account request as soon as possible. "
                          "Expect an email in a couple days informing you of "
                          "our decision")
    success_url = reverse_lazy("registration_view")
    def get_form_kwargs(self):
        kwgs = edit.UpdateView.get_form_kwargs(self)
        kwgs['user'] = self.object
        # TODO: Find out why you need to delete this
        del kwgs['instance']
        return kwgs
    def form_valid(self, form):
        if self.get_registration_profile().identity_confirmed:
            raise Http404
        response = FormValidMessageMixin.form_valid(self, form)
        self.get_registration_profile().send_admin_notification()
        return response
    def get_object(self, queryset=None):
        return self.get_registration_profile().user
    def get_registration_profile(self):
        r = RegistrationProfile.objects.get(confirmation_key=self.kwargs['conf_key'])
        return r
    def get(self, *args, **kwargs):
        if not RegistrationProfile.objects.filter(confirmation_key=self.kwargs['conf_key']).exists():
            return render('registration/invalid_confirmation_code.html')
        return super(UserPasswordUpdate, self).get(self, *args, **kwargs)
class RegistrationForm(FormValidMessageMixin, edit.FormView):
    template_name = 'registration/registration_form.html'
    form_class = forms.RegistrationForm
    success_url = "#"# reverse('login')
    form_valid_message = "Please check your email for a link to set your password"
    
    def form_valid(self, form):
        data = form.cleaned_data
        del data['email1']
        user = get_user_model().objects.create_user(
            **data    
#             username=form.cleaned_data['username'],
#             password='',
#             email=form.cleaned_data['email']
        )
        user.set_unusable_password()
        user.is_active = False
        user.save()
        reg_profile = RegistrationProfile.objects.create(user=user)
        reg_profile.send_user_confirmation()
        return super(RegistrationForm, self).form_valid(form)