from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Planet, System, Galaxy
from .serializers import PlanetSerializer, SystemSerializer, GalaxySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
def getRoutes(request):
    """
    This view allows to display all available endpoints in the API
    """
    routes = [
        {
            'Test_api_key': '150af2b4256f7b9a3e0b68c6c6b92eb974cbef0c'
        },
        {
            'Endpoint': 'api/planets/',
            'method': 'GET',
            'body': None,
            'description': '?api_key=<<YOUR API KEY>>'
        },
        {
            'Endpoints': 'api/systems',
            'method': 'GET',
            'body': None,
            'description': '?api_key=<<YOUR API KEY>>'
        },
        {
            'Endpoint': 'api/galaxies',
            'method': 'GET',
            'body': None,
            'description': '?api_key=<<YOUR API KEY>>'
        },
        {
            'Endpoint': 'galaxies/<int:galaxy_id>/systems/',
            'method': 'GET',
            'body': None,
            'description': '?api_key=<<YOUR API KEY>>',
        },
        {
            'Endpoint': 'galaxies/<int:galaxy_id>/planets/',
            'method': 'GET',
            'body': None,
            'description': '?api_key=<<YOUR API KEY>>'
        },
        {
            'Endpoint': 'system/<int:system_id/planets/',
            'method': 'GET',
            'body': None,
            'description': '?api_key<<YOUR API KEY>>'
        },
    ]
    return Response(routes)


class ApiKeyAuthentication(TokenAuthentication):
    """
    This authentication class extends the TokenAuthentication class
    to allow authentication using API keys passed as query parameters
    in the request URL.
    """

    def authenticate(self, request):
        api_key = request.query_params.get('api_key')
        if not api_key:
            return None
        try:
            token = Token.objects.get(key=api_key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid API key')

        return (token.user, token)


class PlanetList(generics.ListAPIView):
    """
    This view provides a read-only list of all the Planet objects.
    Inherits from the ListAPIView class provided by DRF
    Attributes:
        queryset: The queryset of Planet objects to be listed
        serializer_class: The serializer class to be used for serialization of the queryset
        authentication_class: A tuple of authentication classes to be used fot API key authentication.
        permission_classes: A tuple of permission classes to be used for user authentication
    Methods:
        get_queryset(): Returns the queryset of Planet objects to be listed based on the presence of an api_key
        query parameter in the request URL
    """
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            return Planet.objects.all()
        else:
            return None


class SystemList(generics.ListAPIView):
    """
    This view provides a read-only list of all the System objects.
    Inherits from the ListAPIView class provided by DRF
    Attributes:
        queryset: The queryset of System objects to be listed
        serializer_class: The serializer class to be used for serialization of the queryset
        authentication_class: A tuple of authentication classes to be used fot API key authentication.
        permission_classes: A tuple of permission classes to be used for user authentication
    Methods:
        get_queryset(): Returns the queryset of System objects to be listed based on the presence of an api_key
        query parameter in the request URL
    """
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            return System.objects.all()
        else:
            return None


class GalaxyList(generics.ListAPIView):
    """
    This view provides a read-only list of all the Galaxy objects.
    Inherits from the ListAPIView class provided by DRF
    Attributes:
        queryset: The queryset of Galaxy objects to be listed
        serializer_class: The serializer class to be used for serialization of the queryset
        authentication_class: A tuple of authentication classes to be used fot API key authentication.
        permission_classes: A tuple of permission classes to be used for user authentication
    Methods:
        get_queryset(): Returns the queryset of Galaxy objects to be listed based on the presence of an api_key
        query parameter in the request URL
    """
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            return Galaxy.objects.all()
        else:
            return None


class SystemListByGalaxyView(generics.ListAPIView):
    """
    This API view returns a list of systems in a given galaxy.
    It requires authentication via an API key and only allows access to authenticated users.
    Attributes:
        serializer_class: the serializer class used to serialize the data for response
        queryset: the query set used to retrieve the Galaxy objects from the database
        authentication_classes: the authentication classes used to authenticate the user making the request
        permission_classes: the permission classes used to determine whether the user making the request has permission
        to access the view
    Methods:
        get_queryset: returns the queryset of System objects filtered by the galaxy_id parameter passed in the URL.
        If an API key is provided in the request. If no API key is provided, returns None.
    """
    serializer_class = SystemSerializer
    queryset = Galaxy.objects.all()
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):

        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            galaxy_id = self.kwargs['galaxy_id']
            return System.objects.filter(galaxy_id=galaxy_id)
        else:
            return None


class PlanetListByGalaxyView(generics.ListAPIView):
    """
    This API view returns a list of planets in a given galaxy.
    It requires authentication via an API key and only allows access to authenticated users.
    Attributes:
        serializer_class: the serializer class used to serialize the data for response
        queryset: the query set used to retrieve the Galaxy objects from the database
        authentication_classes: the authentication classes used to authenticate the user making the request
        permission_classes: the permission classes used to determine whether the user making the request has permission
        to access the view
    Methods:
        get_queryset: returns the queryset of Planets objects filtered by the galaxy_id parameter passed in the URL.
        If an API key is provided in the request. If no API key is provided, returns None.
    """
    serializer_class = PlanetSerializer
    queryset = Galaxy.objects.all()
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):

        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            galaxy_id = self.kwargs['galaxy_id']
            return Planet.objects.filter(galaxy_id=galaxy_id)
        else:
            return None


class PlanetListBySystemView(generics.ListAPIView):
    """
    This API view returns a list of planets in a given system.
    It requires authentication via an API key and only allows access to authenticated users.
    Attributes:
        serializer_class: the serializer class used to serialize the data for response
        queryset: the query set used to retrieve the Galaxy objects from the database
        authentication_classes: the authentication classes used to authenticate the user making the request
        permission_classes: the permission classes used to determine whether the user making the request has permission
        to access the view
    Methods:
        get_queryset: returns the queryset of Planets objects filtered by the system_id parameter passed in the URL.
        If an API key is provided in the request. If no API key is provided, returns None.
    """
    serializer_class = PlanetSerializer
    queryset = System.objects.all()
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):

        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            system_id = self.kwargs['system_id']
            return Planet.objects.filter(system_id=system_id)
        else:
            return None
