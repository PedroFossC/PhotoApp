from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView, View
from .models import ImageFolder, Image, User
from .forms import FolderCreateForm, ImageCreateForm, CustomUserCreationForm

class SignUpView(CreateView):
	form_class= CustomUserCreationForm
	template_name = 'registration/sign_up.html'
	def get_success_url(self):
		return reverse('login')

class LandingPageView(TemplateView):
	template_name = 'landing_page.html'
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('travel_book:home_page')
		return super().dispatch(request, *args, **kwargs)

class HomePageView(LoginRequiredMixin, ListView):
	model = ImageFolder
	template_name = "travel\images_folder_list.html"
	context_object_name = 'image_folder_list'

class ImagesListView(LoginRequiredMixin, ListView):
	template_name = 'travel/images_list.html'
	context_object_name = 'images'

	def get_queryset(self):
		folder = get_object_or_404(ImageFolder, pk=self.kwargs['pk'])
		queryset = Image.objects.filter(folder=folder)
		return queryset

class FolderCreateView(LoginRequiredMixin, CreateView):
	template_name = 'travel/images_folder_create.html'
	form_class = FolderCreateForm

	def form_valid(self, form):
		folder = form.save(commit=False)
		folder.user = self.request.user
		folder.save()
		return super(FolderCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse('travel_book:home_page')
class ImageCreateView(LoginRequiredMixin, View):
	template_name = 'travel/images_create.html' 
	form_class = ImageCreateForm

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {'form': self.form_class})

	def post(self, request, *args, **kwargs):
		form = ImageCreateForm(request.POST or None, request.FILES)
		if form.is_valid():
			images = request.FILES.getlist('images')
			for image in images:
				folder = ImageFolder.objects.get(pk=self.kwargs['pk'])
				Image.objects.create(folder=folder, image= image)
			return redirect('travel_book:images_list', self.kwargs['pk'])