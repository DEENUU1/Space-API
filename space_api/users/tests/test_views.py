from django.test import TestCase, Client
from django.urls import reverse


class TestGetTokenViewTestCase(TestCase):
    """
    Test Case for testing the GetTokenView.
    """

    def setUp(self) -> None:
        self.client = Client()
        self.token_url = reverse('users:get-token')

    def test_signup_page_loads_successfully(self) -> None:
        """
        This test should return status code with value 405 because it do not access GET method
        Only POST is available
        """
        response = self.client.get(self.token_url)
        self.assertEqual(response.status_code, 405)
