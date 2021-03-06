from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView,LogoutView)
from .forms import LoginForm

#ログインページ

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'account/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'account/login.html'