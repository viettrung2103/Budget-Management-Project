from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import SignUpForm


class OwnPasswordChange(PasswordChangeView):
    template_name = 'password_change_form.html'


class OwnPasswordChangeDone(PasswordChangeDoneView):
    template_name = 'password_change_done.html'


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

class ProfileView():
    pass