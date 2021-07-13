from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
# Create your views here.


class HomePage(LoginRequiredMixin, TemplateView):
	template_name = 'travel/home.html'
