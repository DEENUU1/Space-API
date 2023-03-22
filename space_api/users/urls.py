from django.urls import path
from .views import SignUpView, LoginView, ProfilView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfilView.as_view(), name='profile'),
]