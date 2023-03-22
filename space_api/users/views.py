from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token


class SignUpView(View):
    """
    This view allows user to create a new account
    """
    FORM_CLASS = CreateUserForm
    TEMPLATE_NAME = 'registration/register.html'

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
    This view allows users to log in.
    """
    TEMPLATE_NAME = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile')
        return render(request, self.TEMPLATE_NAME)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request,
                          'Try again')
            return render(request, self.TEMPLATE_NAME)


class ProfilView(LoginRequiredMixin, View):
    """
    This view allows log in user to generate a API_KEY
    """
    TEMPLATE_NAME = 'registration/profile.html'

    def get(self, request):
        token, created = Token.objects.get_or_create(user=request.user)
        context = {
            'token': token.key,
        }

        return render(request,
                      self.TEMPLATE_NAME,
                      context)
