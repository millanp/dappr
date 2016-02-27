from django.test import TestCase
from django.test.client import Client
from dappr.models import RegistrationProfile
from django.core.urlresolvers import reverse

# Create your tests here.

class ResponseCodeAttrsMixin(object):
    FORM_GET_RESPONSE_CODE = 200
    FORM_ERROR_RESPONSE_CODE = 200
    FORM_SUCCESS_RESPONSE_CODE = 302

class RegistrationViewTestCase(ResponseCodeAttrsMixin, TestCase):
    def setUp(self):
        self.client = Client()
    def test_regview_responds(self):
        get_response = self.client.get('/register')
        self.assertEqual(get_response.status_code, self.FORM_GET_RESPONSE_CODE, "Register view not providing OK response")
    def test_regview_form_emails_different(self):
        post_response = self.client.post('/register', {
            "username":"testUsername",
            "email":"extratextmalabarhousereservations@gmail.com",
            "email1":"malabarhousereservations@gmail.com"
        })
        # This should redirect the user to some other success page
        self.assertEqual(post_response.status_code, self.FORM_ERROR_RESPONSE_CODE, ("Register form giving false success "
                                                                                    "when email != email1"))
    def test_regview_form_username_exists(self):
        self.client.post('/register', {
            "username":"testUsername",
            "email":"malabarhousereservations@gmail.com",
            "email1":"malabarhousereservations@gmail.com"
        })
        post_response = self.client.post('/register', {
            "username":"testUsername",
            "email":"malabarhousereservations@gmail.com",
            "email1":"malabarhousereservations@gmail.com"
        })
        self.assertEqual(post_response.status_code, self.FORM_ERROR_RESPONSE_CODE, ("Register form giving false success "
                                                                                    "when username already exists "))
    # C means a component of another test
    def c_test_regview_form_success(self):
        username = "testUsername"
        post_response = self.client.post(reverse('registration_view'), {
            "username":username,
            "email":"malabarhousereservations@gmail.com",
            "email1":"malabarhousereservations@gmail.com"
        })
        # This should redirect the user to some other success page
        self.assertEqual(post_response.status_code, self.FORM_SUCCESS_RESPONSE_CODE, ("Register form giving false failure "
                                                                                      "or not redirecting"))
        r = RegistrationProfile.objects.get(user__username=username)
        self.assertEqual(r.approved, False, "Registration profile started out approved")
        self.assertIsNotNone(r.confirmation_key, "Confirmation key not set")
        self.assertEqual(r.active, True, "Registration profile started out not active")
        self.assertEqual(r.identity_confirmed, False, "Registration profile started out identity confirmed")
#         self.assertEqual(r.user.is_active, False, "user activated before identity confirmation")
        return r
    # Remember, component...
    def c_test_pwdsetview_responds(self):
        r = self.c_test_regview_form_success()
        url = reverse('confirmation_view', kwargs={"conf_key":r.confirmation_key})
        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, self.FORM_GET_RESPONSE_CODE, "Password set view not providing OK response")
        return r, url
    def c_test_pwdsetview_form_success(self):
        r, url = self.c_test_pwdsetview_responds()
        post_response = self.client.post(url, {
            "new_password1":"t",
            "new_password2":"t",
        })
        r.refresh_from_db()
        self.assertEqual(post_response.status_code, self.FORM_SUCCESS_RESPONSE_CODE, ("Password set form giving false failure "
                                                                                      "or not redirecting"))
        self.assertEqual(r.identity_confirmed, True, "Identity confirmed not set after user confirms identity")
        self.assertEqual(r.user.check_password("t"), True, "Password not correctly set in user instance")
        return r