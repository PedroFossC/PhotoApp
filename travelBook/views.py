from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from .models import ImageFolder
# Create your views here.

class LandingPage(TemplateView):
	template_name = 'landing_page.html'
	def dispatch(self, request):
		if request.user.is_authenticated:
			return redirect('travel_book:home_page')
		return super().dispatch(request, *args, **kwargs)

class HomePage(LoginRequiredMixin, ListView):
	model = ImageFolder
	template_name = "travel\image_folder_list.html"
	context_object_name = 'image_folder_list'

class ImagesFolderDetail(LoginRequiredMixin, DetailView):
	model = ImageFolder
	template_name = 'travel/image_folder_detail.html'
	context_object_name = 'images'
