from django.urls import path
from .views import \
    (getRoutes,
     PlanetList,
     SystemList,
     GalaxyList,
     SystemListByGalaxyView,
     PlanetListByGalaxyView,
     PlanetListBySystemView)

app_name = 'base'

urlpatterns = [
    path('', getRoutes, name='get-routes'),
    path('planets/', PlanetList.as_view(), name='planet-list'),
    path('systems/', SystemList.as_view(), name='system-list'),
    path('galaxies/', GalaxyList.as_view(), name='galaxy-list'),
    path('galaxies/<int:galaxy_id>/systems/', SystemListByGalaxyView.as_view(), name='system-list-by-galaxy'),
    path('galaxies/<int:galaxy_id>/planets/', PlanetListByGalaxyView.as_view(), name='planet-list-by-galaxy'),
    path('system/<int:system_id>/planets/', PlanetListBySystemView.as_view(), name='planet-list-by-system'),

]