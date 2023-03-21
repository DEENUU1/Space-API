from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('galaxy', views.galaxy, name='galaxy'),
    path('systems', views.systemy, name='systemy'),
    path('planets', views.planets, name='planets'),
    path('system-galaxy', views.system_of_galaxy, name='system-galaxy'),
    path('planets-of-system', views.planets_of_system, name='planets-system')
]