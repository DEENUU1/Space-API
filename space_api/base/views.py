from rest_framework.decorators import api_view
from rest_framework.response import Response


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
