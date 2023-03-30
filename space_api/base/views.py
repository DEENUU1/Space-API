from rest_framework import generics, permissions
from .models import Planet, System, Galaxy, Rocket, Mission
from .serializers import PlanetSerializer, SystemSerializer, GalaxySerializer, RocketSerializer, MissionSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.pagination import PageNumberPagination


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


class ApiPagination(PageNumberPagination):
    """
    A custom pagination class that extends Django Rest Framework's PageNumberPagination class.
    This class is designed to handle paginated responses for API views. It sets the default page size to 2 but can be
    customized by setting the page_size attribute.
    Attributes:
    page_size (int): The number of items to include on each page. Defaults to 2.
    """
    page_size = 10


class PlanetList(generics.ListAPIView):
    """
    This view provides a read-only list of all the Planet objects.
    Inherits from the ListAPIView class provided by DRF.
    Attributes:
        queryset: The queryset of Planet objects to be listed
        serializer_class: The serializer class to be used for serialization of the queryset
        authentication_class: A tuple of authentication classes to be used fot API key authentication.
        permission_classes: A tuple of permission classes to be used for user authentication
        pagination_class: A custom pagination class that extends Django Rest Framework's PageNumberPagination class.
    Methods:
        get_queryset(): Returns the queryset of Planet objects to be listed based on the presence of an api_key
        query parameter in the request URL
    """
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

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
        pagination_class: A custom pagination class that extends Django Rest Framework's PageNumberPagination class.
    Methods:
        get_queryset(): Returns the queryset of System objects to be listed based on the presence of an api_key
        query parameter in the request URL
    """
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

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
        pagination_class: A custom pagination class that extends Django Rest Framework's PageNumberPagination class.
    Methods:
        get_queryset(): Returns the queryset of Galaxy objects to be listed based on the presence of an api_key
        query parameter in the request URL
    """
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

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
        pagination_class: A custom pagination class that extends Django Rest Framework's PageNumberPagination class.
    Methods:
        get_queryset: returns the queryset of System objects filtered by the galaxy_id parameter passed in the URL.
        If an API key is provided in the request. If no API key is provided, returns None.
    """
    serializer_class = SystemSerializer
    queryset = Galaxy.objects.all()
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

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
        pagination_class: A custom pagination class that extends Django Rest Framework's PageNumberPagination class.
    Methods:
        get_queryset: returns the queryset of Planets objects filtered by the galaxy_id parameter passed in the URL.
        If an API key is provided in the request. If no API key is provided, returns None.
    """
    serializer_class = PlanetSerializer
    queryset = Galaxy.objects.all()
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

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
        pagination_class: A custom pagination class that extends Django Rest Framework's PageNumberPagination class.
    Methods:
        get_queryset: returns the queryset of Planets objects filtered by the system_id parameter passed in the URL.
        If an API key is provided in the request. If no API key is provided, returns None.
    """
    serializer_class = PlanetSerializer
    queryset = System.objects.all()
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

    def get_queryset(self):

        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            system_id = self.kwargs['system_id']
            return Planet.objects.filter(system_id=system_id)
        else:
            return None


class PlanetDetail(generics.RetrieveAPIView):
    """
    This view provides a read-only detail view of a single Planet object.
    Inherits from the RetrieveAPIView class provided by DRF.
    This view is using cache_page set on 2 hours.
    Attributes:
        queryset: The queryset of Planet objects to be retrieved
        serializer_class: The serializer class to be used for serialization of the queryset
        authentication_class: A tuple of authentication classes to be used for API key authentication.
        permission_classes: A tuple of permission classes to be used for user authentication
    """
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    @method_decorator(cache_page(60 * 60 * 2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SystemDetail(generics.RetrieveAPIView):
    """
    This view provides a read-only detail view of a single System object.
    Inherits from the RetrieveAPIView class provided by DRF.
    This view is using cache_page set on 2 hours.
    Attributes:
        queryset: The queryset of System objects to be retrieved
        serializer_class: The serializer class to be used for serialization of the queryset
        authentication_class: A tuple of authentication classes to be used for API key authentication.
        permission_classes: A tuple of permission classes to be used for user authentication
    """
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    @method_decorator(cache_page(60 * 60 * 2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class GalaxyDetail(generics.RetrieveAPIView):
    """
    This view provides a read-only detail view of a single Galaxy object.
    Inherits from the RetrieveAPIView class provided by DRF.
    This view is using cache_page set on 2 hours.
    Attributes:
        queryset: The queryset of Galaxy objects to be retrieved
        serializer_class: The serializer class to be used for serialization of the queryset
        authentication_class: A tuple of authentication classes to be used for API key authentication.
        permission_classes: A tuple of permission classes to be used for user authentication
    """
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    @method_decorator(cache_page(60 * 60 * 2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class RocketList(generics.ListAPIView):
    """
    This view provides a read-only list of all the Rocket objects.
    Inherits from the ListAPIView class provided by DRF.
    Attributes:
        queryset: The queryset of Rocket objects to be listed
        serializer_class: The serializer class to be used for serialization of the queryset
        authentication_class: A tuple of authentication classes to be used fot API key authentication.
        permission_classes: A tuple of permission classes to be used for user authentication
        pagination_class: A custom pagination class that extends Django Rest Framework's PageNumberPagination class.
    Methods:
        get_queryset(): Returns the queryset of Rocket objects to be listed based on the presence of an api_key
        query parameter in the request URL
    """
    queryset = Rocket.objects.all()
    serializer_class = RocketSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            return Rocket.objects.all()
        else:
            return None


class RocketCreateView(generics.CreateAPIView):
    """
    This view provides a POST method to create a new Rocket object.
    Inherits from the CreateAPIView class provided by DRF.
    Attributes:
        serializer_class: The serializer class to be used for serialization of the Rocket object
        authentication_class: A tuple of authentication classes to be used for API key authentication.
        permission_classes: A tuple of permission classes to be used for user authentication
    """
    serializer_class = RocketSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class MissionList(generics.ListAPIView):
    """
    This view provides a read-only list of all the Mission objects.
    Inherits from the ListAPIView class provided by DRF.
    Attributes:
        queryset: The queryset of Mission objects to be listed
        serializer_class: The serializer class to be used for serialization of the queryset
        authentication_class: A tuple of authentication classes to be used fot API key authentication.
        permission_classes: A tuple of permission classes to be used for user authentication
        pagination_class: A custom pagination class that extends Django Rest Framework's PageNumberPagination class.
    Methods:
        get_queryset(): Returns the queryset of Mission objects to be listed based on the presence of an api_key
        query parameter in the request URL
    """
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ApiPagination

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key', None)
        if api_key:
            return Mission.objects.all()
        else:
            return None


class MissionCreateView(generics.CreateAPIView):
    """
    This view provides a POST method to create a new Mission object.
    Inherits from the CreateAPIView class provided by DRF.
    Attributes:
        serializer_class: The serializer class to be used for serialization of the Mission object
        authentication_class: A tuple of authentication classes to be used for API key authentication.
        permission_classes: A tuple of permission classes to be used for user authentication
    """
    serializer_class = MissionSerializer
    authentication_classes = (ApiKeyAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)