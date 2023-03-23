from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Planet, System
from .serializers import PlanetSerializer, SystemSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def getRoutes(request):
    """
    This view allows to display all available endpoints in the API
    """
    routes = [
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
    authentication_classes = (ApiKeyAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            return Planet.objects.all()
        else:
            return None


class SystemList(generics.ListAPIView):
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
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    authentication_classes = (ApiKeyAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            return System.objects.all()
        else:
            return None

