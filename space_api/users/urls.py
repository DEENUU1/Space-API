from django.urls import path

from .views import GetTokenView, DeleteTokenView

app_name = 'users'

urlpatterns = [
    path('token/', GetTokenView.as_view(), name='get-token'),
    path('delete-token/', DeleteTokenView.as_view(), name='delete-token')

]