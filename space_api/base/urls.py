from django.urls import path
from .views import getRoutes, PlanetList, SystemList, GalaxyList

app_name = 'base'

urlpatterns = [
    path('', getRoutes, name='get-routes'),
    path('planets/', PlanetList.as_view(), name='planet-list'),
    path('systems/', SystemList.as_view(), name='system-list'),
    path('galaxies/', GalaxyList.as_view(), name='galaxy-list'),

]