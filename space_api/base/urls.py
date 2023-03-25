from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import \
    (getRoutes,
     PlanetList,
     SystemList,
     GalaxyList,
     SystemListByGalaxyView,
     PlanetListByGalaxyView,
     PlanetListBySystemView,
     )

app_name = 'base'


schema_view = get_schema_view(
    openapi.Info(
        title="Space API documentation",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
)


urlpatterns = [
    path('', getRoutes, name='get-routes'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('planets/', PlanetList.as_view(), name='planet-list'),
    path('systems/', SystemList.as_view(), name='system-list'),
    path('galaxies/', GalaxyList.as_view(), name='galaxy-list'),
    path('galaxies/<int:galaxy_id>/systems/', SystemListByGalaxyView.as_view(), name='system-list-by-galaxy'),
    path('galaxies/<int:galaxy_id>/planets/', PlanetListByGalaxyView.as_view(), name='planet-list-by-galaxy'),
    path('system/<int:system_id>/planets/', PlanetListBySystemView.as_view(), name='planet-list-by-system'),

]