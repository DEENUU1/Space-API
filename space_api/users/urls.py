from django.urls import path

from .views import GetTokenView

app_name = 'users'

urlpatterns = [
    path('token/', GetTokenView.as_view(), name='get-token'),

]