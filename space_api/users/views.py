from .serializers import GetTokenSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GetTokenView(APIView):
    """
    View for registering a new user.

    Accepts a POST request with user data in the request body.
    If the data is valid, a new user is created and a 201 Created response is returned.
    If the data is invalid, a 400 Bad Request response is returned with a message describing the errors.

    """

    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
