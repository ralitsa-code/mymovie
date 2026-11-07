from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from accounts.forms import AppUserCreateForm

# def register(request):
#     form = UserCreationForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         user = form.save()
#         login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#         return redirect('home')
#
#     return render(request, 'register.html', {'form': form})

UserModel = get_user_model()

class RegisterAppUserView(CreateView):
    model = UserModel
    form_class = AppUserCreateForm
    template_name = 'register.html'
    success_url = 'home'


class LoginAppUserView(LoginView):
    template_name = ''
