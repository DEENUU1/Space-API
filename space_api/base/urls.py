from django.urls import path
from .views import getRoutes

app_name = 'base'

urlpatterns = [
    path('', getRoutes, name='get-routes'),
]