from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from users.forms import CreateUserForm
from django.contrib.messages import get_messages
from django.contrib import auth
import users.urls


class TestSignUpViewTestCase(TestCase):
    """
    Test Case for testing the SignUpView view.
    """
    def setUp(self) -> None:
        self.client = Client()
        self.signup_url = reverse('users:signup')

    def test_signup_page_loads_successfully(self) -> None:
        """
        Ensures that the sign-up page loads successfully and uses the correct template
        """
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')\



class TestSingInView(TestCase):
    """
    Test Case for testing the SignInView view.
    """
    def setUp(self) -> None:
        self.client = Client()
        self.login_url = reverse('users:login')

    def test_login_page_loads_successfully(self) -> None:
        """
        Ensures that the log-in page loads successfully and uses the correct template
        """
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


class TestProfileView(TestCase):
    """
    Test Case for testing the ProfileView view.
    """
    def setUp(self) -> None:
        self.client = Client()
        self.profile_url = reverse('users:profile')

    def test_profile_page_loads_successfully(self) -> None:
        """
        Ensures that the log-in page loads successfully.
        It returns 302 because test user is not log-in and the view redirect user to another url
        """
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)


class TestLogoutView(TestCase):
    """
    Test Case for testing the LogoutView view.
    """
    def setUp(self) -> None:
        self.client = Client()
        self.logout_url = reverse('users:logout')

    def test_logout_view_works_successfully(self) -> None:
        """
        Ensures that the log-out functions works successfully.
        """
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200)
