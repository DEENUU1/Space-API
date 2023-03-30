from django.test import TestCase, Client
from django.urls import reverse


class TestGetTokenViewTestCase(TestCase):
    """
    Test Case for testing the GetTokenView.
    """

    def setUp(self) -> None:
        self.client = Client()
        self.token_url = reverse('users:get-token')

    def test_get_token_html_status_code_value(self) -> None:
        """
        This test should return status code with value 405 because it do not access GET method
        Only POST is available
        """
        response = self.client.get(self.token_url)
        self.assertEqual(response.status_code, 405)


class TestRemoveTokenViewTestCase(TestCase):
    """
    Test Case for testing the DeleteTokenView.
    """

    def setUp(self) -> None:
        self.client = Client()
        self.token_url = reverse('users:delete-token')

    def test_delete_token_html_status_code_value(self) -> None:
        """
        This test should return status code with value 405 because it do not access GET method
        Only POST is available
        """
        response = self.client.get(self.token_url)
        self.assertEqual(response.status_code, 405)