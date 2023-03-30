from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import \
    (PlanetList,
     SystemList,
     GalaxyList,
     SystemListByGalaxyView,
     PlanetListByGalaxyView,
     PlanetListBySystemView,
     PlanetDetail,
     SystemDetail,
     GalaxyDetail,
     RocketList,
     RocketCreateView,
     MissionList,
     MissionCreateView,
     )

app_name = 'base'


schema_view = get_schema_view(
    openapi.Info(
        title="Space API documentation",
        default_version='v1',
        description="test api key: 150af2b4256f7b9a3e0b68c6c6b92eb974cbef0c",
    ),
    public=True,
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('planets/', PlanetList.as_view(), name='planet-list'),
    path('systems/', SystemList.as_view(), name='system-list'),
    path('galaxies/', GalaxyList.as_view(), name='galaxy-list'),
    path('galaxies/<int:galaxy_id>/systems/', SystemListByGalaxyView.as_view(), name='system-list-by-galaxy'),
    path('galaxies/<int:galaxy_id>/planets/', PlanetListByGalaxyView.as_view(), name='planet-list-by-galaxy'),
    path('system/<int:system_id>/planets/', PlanetListBySystemView.as_view(), name='planet-list-by-system'),
    path('planet/<int:pk>/', PlanetDetail.as_view(), name='planet-detail'),
    path('system/<int:pk>/', SystemDetail.as_view(), name='system-detail'),
    path('galaxy/<int:pk>/', GalaxyDetail.as_view(), name='galaxy-detail'),
    path('rockets/', RocketList.as_view(), name='rocket-list'),
    path('rocket/create', RocketCreateView.as_view(), name='rocket-create'),
    path('missions/', MissionList.as_view(), name='mission-list'),
    path('mission/create', MissionCreateView.as_view(), name='mission-create'),


]