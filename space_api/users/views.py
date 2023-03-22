from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib import messages


class SignUpView(View):
    """
    This view allows user to create a new account
    """
    form_class = CreateUserForm
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if User.objects.filter(email=form.data['email']).exists():
            messages.error(request,
                           'This email address already exist')

        if form.is_valid():
            form.save()
            messages.success(request,
                             'Your account has been created')
            return redirect('/')
        else:
            messages.error(request,
                           'Account creation failed')

        return render(request, self.template_name, {'form': form})

