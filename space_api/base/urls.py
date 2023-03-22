from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('api/', views.getRoutes, name='get-routes'),
]