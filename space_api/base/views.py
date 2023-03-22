from django.shortcuts import render
from django.http import response
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/',
            'method': 'GET',
            'body': None,
            'description': 'Some text'
        },
    ]
    return Response(routes)