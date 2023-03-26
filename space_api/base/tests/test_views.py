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


class SystemListByGalaxyTestCase(BaseTestCase):
    def test_system_list_by_galaxy_with_api_key_authentication(self) -> None:
        """
        Test that the system list for a given galaxy can be retrieved with valid API key authentication.
        This test sends a GET request to the 'system-list-by-galaxy' endpoint with a valid API key for authentication.
        The galaxy ID is set to 1, which is assumed to exist in the database.
        The test checks that the response status code is HTTP_200_OK and that the response data contains one system.
        """
        galaxy_id = 1
        url = reverse('base:system-list-by-galaxy', args=[galaxy_id])
        response = self.client.get(url, {'api_key': self.api_key})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_system_list_by_galaxy_without_authentication(self) -> None:
        """
        Test that the system list for a given galaxy cannot be retrieved without authentication.
        This test sends a GET request to the 'system-list-by-galaxy' endpoint without any authentication.
        The galaxy ID is set to 1, which is assumed to exist in the database.
        The test checks that the response status code is HTTP_401_UNAUTHORIZED.
        """
        galaxy_id = 1
        url = reverse('base:system-list-by-galaxy', args=[galaxy_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_system_list_by_galaxy_invalid_api_key(self) -> None:
        """
        Test that the system list for a given galaxy cannot be retrieved with an invalid API key.
        This test sends a GET request to the 'system-list-by-galaxy' endpoint with an invalid API key for authentication
        The galaxy ID is set to 1, which is assumed to exist in the database.
        The test checks that the response status code is HTTP_401_UNAUTHORIZED.
        """
        galaxy_id = 1
        url = reverse('base:system-list-by-galaxy', args=[galaxy_id])
        response = self.client.get(url, {'api_key': 'invalid_api_key'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PlanetListByGalaxyTestCase(BaseTestCase):
    def test_planet_list_by_galaxy_with_api_key_authentication(self) -> None:
        """
        Test that the planet list for a given galaxy can be retrieved with valid API key authentication.
        This test sends a GET request to the 'planet-list-by-galaxy' endpoint with a valid API key for authentication.
        The galaxy ID is set to 1, which is assumed to exist in the database.
        The test checks that the response status code is HTTP_200_OK and that the response data contains one system.
        """
        galaxy_id = 1
        url = reverse('base:planet-list-by-galaxy', args=[galaxy_id])
        response = self.client.get(url, {'api_key': self.api_key})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_planet_list_by_galaxy_without_authentication(self) -> None:
        """
        Test that the planet list for a given galaxy cannot be retrieved without authentication.
        This test sends a GET request to the 'planet-list-by-galaxy' endpoint without any authentication.
        The galaxy ID is set to 1, which is assumed to exist in the database.
        The test checks that the response status code is HTTP_401_UNAUTHORIZED.
        """
        galaxy_id = 1
        url = reverse('base:planet-list-by-galaxy', args=[galaxy_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_planet_list_by_galaxy_invalid_api_key(self) -> None:
        """
        Test that the planet list for a given galaxy cannot be retrieved with an invalid API key.
        This test sends a GET request to the 'planet-list-by-galaxy' endpoint with an invalid API key for authentication
        The galaxy ID is set to 1, which is assumed to exist in the database.
        The test checks that the response status code is HTTP_401_UNAUTHORIZED.
        """
        galaxy_id = 1
        url = reverse('base:planet-list-by-galaxy', args=[galaxy_id])
        response = self.client.get(url, {'api_key': 'invalid_api_key'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PlanetListBySystemTestCase(BaseTestCase):
    def test_planet_list_by_system_with_api_key_authentication(self) -> None:
        """
        Test that the planet list for a given system can be retrieved with valid API key authentication.
        This test sends a GET request to the 'planet-list-by-system' endpoint with a valid API key for authentication.
        The system ID is set to 1, which is assumed to exist in the database.
        The test checks that the response status code is HTTP_200_OK and that the response data contains one system.
        """
        system_id = 1
        url = reverse('base:planet-list-by-system', args=[system_id])
        response = self.client.get(url, {'api_key': self.api_key})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_planet_list_by_system_without_authentication(self) -> None:
        """
        Test that the planet list for a given system cannot be retrieved without authentication.
        This test sends a GET request to the 'planet-list-by-system' endpoint without any authentication.
        The system ID is set to 1, which is assumed to exist in the database.
        The test checks that the response status code is HTTP_401_UNAUTHORIZED.
        """
        system_id = 1
        url = reverse('base:planet-list-by-galaxy', args=[system_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_planet_list_by_system_invalid_api_key(self) -> None:
        """
        Test that the planet list for a given system cannot be retrieved with an invalid API key.
        This test sends a GET request to the 'planet-list-by-system' endpoint with an invalid API key for authentication
        The system ID is set to 1, which is assumed to exist in the database.
        The test checks that the response status code is HTTP_401_UNAUTHORIZED.
        """
        system_id = 1
        url = reverse('base:planet-list-by-system', args=[system_id])
        response = self.client.get(url, {'api_key': 'invalid_api_key'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
