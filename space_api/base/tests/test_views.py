from django.test import TestCase, Client
from django.urls import reverse


class MainViewTestCase(TestCase):
    """
    Test Case for testing the getRoutes view.
    """
    def setUp(self) -> None:
        self.client = Client()
        self.signup_url = reverse('base:get-routes')

    def test_getRoutes_page_loads_successfully(self) -> None:
        """
        Ensures that the getRoutes page loads successfully
        """
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)

