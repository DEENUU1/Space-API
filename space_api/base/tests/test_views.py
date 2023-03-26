from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from base.models import Planet, Galaxy, System
from base.serializers import PlanetSerializer, SystemSerializer, GalaxySerializer


class BaseTestCase(APITestCase):
    @classmethod
    def setUp(cls) -> None:
        """
        Sets up the test data and creates a user, token, galaxy, system and planet objects for the test.
        """
        super().setUpClass()
        cls.user = User.objects.create_user(username='test', password='test123')
        cls.token = Token.objects.create(user=cls.user)
        cls.api_key = cls.token.key
        cls.galaxy = Galaxy.objects.create(name='Milky way', description='Our galaxy')
        cls.system = System.objects.create(name='Solar system', description='Our system', galaxy=cls.galaxy)
        cls.planet = Planet.objects.create(name='Mercury', description='First planet', galaxy=cls.galaxy, system=cls.system)
        cls.planet_expected_data = PlanetSerializer([cls.planet], many=True).data
        cls.system_expected_data = SystemSerializer([cls.system], many=True).data
        cls.galaxy_expected_data = GalaxySerializer([cls.galaxy], many=True).data


class PlanetListTestCase(BaseTestCase):
    def test_planet_list_with_api_key_authentication(self) -> None:
        """
        Tests the planet list view with API key authentication.
        It sends a GET request to the planet-list endpoint with a valid API key and expects a 200 OK response.
        It also compares the response data with the expected data using the `PlanetSerializer`.
        """
        url = reverse('base:planet-list')
        response = self.client.get(url, {'api_key': self.api_key})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, self.planet_expected_data)

    def test_planet_list_without_authentication(self) -> None:
        """
        Tests the planet list view without authentication.
        It sends a GET request to the planet-list endpoint without an API key and expects a 401 UNAUTHORIZED response.
        """
        url = reverse('base:planet-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_planet_list_with_invalid_api_key(self) -> None:
        """
        Tests the planet list view with an invalid API key.
        It sends a GET request to the planet-list endpoint with an invalid API key and expects a 401 UNAUTHORIZED
        response.
        """
        url = reverse('base:planet-list')
        response = self.client.get(url, {'api_key': 'invalid_api_key'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class SystemListTestCase(BaseTestCase):
    def test_system_list_with_api_key_authentication(self) -> None:
        """
        Tests the system list view with API key authentication.
        It sends a GET request to the planet-list endpoint with a valid API key and expects a 200 OK response.
        It also compares the response data with the expected data using the `SystemSerializer`.
        """
        url = reverse('base:system-list')
        response = self.client.get(url, {'api_key': self.api_key})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, self.system_expected_data)

    def test_system_list_without_authentication(self) -> None:
        """
        Tests the system list view without authentication.
        It sends a GET request to the system-list endpoint without an API key and expects a 401 UNAUTHORIZED response.
        """
        url = reverse('base:system-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_system_list_with_invalid_api_key(self) -> None:
        """
        Tests the system list view with an invalid API key.
        It sends a GET request to the system-list endpoint with an invalid API key and expects a 401 UNAUTHORIZED
        response.
        """
        url = reverse('base:system-list')
        response = self.client.get(url, {'api_key': 'invalid_api_key'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class GalaxyListTestCase(BaseTestCase):
    def test_galaxy_list_with_api_key_authentication(self) -> None:
        """
        Tests the galaxy list view with API key authentication.
        It sends a GET request to the planet-list endpoint with a valid API key and expects a 200 OK response.
        It also compares the response data with the expected data using the `GalaxySerializer`.
        """
        url = reverse('base:galaxy-list')
        response = self.client.get(url, {'api_key': self.api_key})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, self.galaxy_expected_data)

    def test_galaxy_list_without_authentication(self) -> None:
        """
        Tests the galaxy list view without authentication.
        It sends a GET request to the system-list endpoint without an API key and expects a 401 UNAUTHORIZED response.
        """
        url = reverse('base:galaxy-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_galaxy_list_with_invalid_api_key(self) -> None:
        """
        Tests the galaxy list view with an invalid API key.
        It sends a GET request to the galaxy-list endpoint with an invalid API key and expects a 401 UNAUTHORIZED
        response.
        """
        url = reverse('base:galaxy-list')
        response = self.client.get(url, {'api_key': 'invalid_api_key'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)