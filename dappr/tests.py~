from django.test import TestCase
from django.test.client import Client

# Create your tests here.
class RegistrationProfileTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    def test_requestview_responds(self):
        get_response = self.client.get('/register')
        self.assertEqual(get_response.status_code, 200, "Request view not providing OK response")
        post_response = self.client.post('/register', {
            "username":"testUsername",
            "email":"malabarhousereservations@gmail.com",
            "email1":"malabarhousereservations@gmail.com"
        })
        self.assertEqual(post_response.status_code, 200)
        