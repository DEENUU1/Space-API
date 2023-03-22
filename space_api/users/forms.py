from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    """
    This class form allows to create a new user
    """
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']