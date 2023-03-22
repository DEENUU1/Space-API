from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from users.forms import CreateUserForm
from django.contrib.messages import get_messages
from django.contrib import auth
import users.urls


class SignUpViewTestCase(TestCase):
    """
    Test Case for testing the SignUpView view.

    Tests:
    - test_signup_page_loads_successfully ensures that the
        sign-up page loads successfully and uses the correct template
    """
    def setUp(self) -> None:
        self.client = Client()
        self.signup_url = reverse('users:signup')
        self.login_url = reverse('users:login')

    def test_signup_page_loads_successfully(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')\


