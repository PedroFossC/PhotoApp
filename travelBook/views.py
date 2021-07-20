from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from .models import ImageFolder, Image
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

class ImagesFolderList(LoginRequiredMixin, ListView):
	template_name = 'travel/images_list.html'
	context_object_name = 'images'

	def get_queryset(self):
		folder = get_object_or_404(ImageFolder, pk=self.kwargs['pk'])
		queryset = Image.objects.filter(folder=folder)
		print(queryset[0].image.url)
		return queryset
