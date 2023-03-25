from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.authtoken.models import Token

from .forms import CreateUserForm


class SignUpView(View):
    """
    View for registering a new user account.
    Attributes:
        FORM_CLASS -> The form class used for registering a new user.
        TEMPLATE_NAME -> The name of the template used to render a registration form
    Methods:
        dispatch(request, *args, **kwargs) -> Overrides the default dispatch behavior to check if the user is auth.
        get(request, *args, **kwargs) -> Renders the registration form
        post(request, *args, **kwargs) -> Processes the registration form and creates a new user account if valid.
    """
    FORM_CLASS = CreateUserForm
    TEMPLATE_NAME: str = 'registration/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.FORM_CLASS
        return render(request, self.TEMPLATE_NAME, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.FORM_CLASS(request.POST)

        if User.objects.filter(email=form.data['email']).exists():
            messages.error(request,
                           'This email address already exist')

        if User.objects.filter(username=form.data['username']).exists():
            messages.error(request,
                           'This username already exist')

        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your account has been created')
            return redirect('/')
        else:
            messages.error(request,
                           'Account creation failed')

        return render(request, self.TEMPLATE_NAME, {'form': form})


class SignInView(LoginView):
    """
    View for log in a user.
    Attributes:
        TEMPLATE_NAME -> The name of the template used to render the login form.
    Methods:
        get(request) -> Renders the login form.
        post(request) -> Attempts to authenticate the user and log them in if successful.
    """
    TEMPLATE_NAME: str = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return render(request, self.TEMPLATE_NAME)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('user:profile')
        else:
            messages.info(request,
                          'Try again')
            return render(request, self.TEMPLATE_NAME)


class ProfilView(LoginRequiredMixin, View):
    """
    View for displaying the user's profile.
    Attributes:
        TEMPLATE_NAME -> The name of the template used to render the profile information.
    Methods:
        get(request) ->  Renders the user's profile information.
    """
    TEMPLATE_NAME: str = 'registration/profile.html'

    def get(self, request):
        token, created = Token.objects.get_or_create(user=request.user)
        context = {
            'token': token.key,
        }

        return render(request,
                      self.TEMPLATE_NAME,
                      context)


class LogoutUserView(LogoutView):
    """
    View for logging out a user.
    Methods:
        get(request) -> Logs the user
    """
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


def main(request):
    return render(request, 'main.html')
