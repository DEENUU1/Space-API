from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Planet
from .serializers import PlanetSerializer
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
            'Endpoint': '/',
            'method': 'GET',
            'body': None,
            'description': 'Some text'
        },
    ]
    return Response(routes)


class ApiKeyAuthentication(TokenAuthentication):
    def authenticate(self, request):
        api_key = request.query_params.get('api_key')
        if not api_key:
            return None
        try:
            token = Token.objects.get(key=api_key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid API key')

        return token.user, token
