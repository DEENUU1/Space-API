from django.urls import path
from .views import getRoutes, PlanetList

app_name = 'base'

urlpatterns = [
    path('', getRoutes, name='get-routes'),
    path('planets/', PlanetList.as_view(), name='planet-list'),
]