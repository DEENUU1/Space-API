from django.urls import path
from .views import SignUpView, LoginView, ProfilView, LogoutView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfilView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),

]