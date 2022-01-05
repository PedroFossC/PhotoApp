from django.urls import path

from .views import (
	HomePageView, 
	ImagesListView, 
	FolderCreateView, 
	ImageCreateView,
)

app_name='travel_book'

urlpatterns = [
	path('', HomePageView.as_view(), name='home_page'),
	path('create-folder/', FolderCreateView.as_view(), name='folder_create'),
	path('<int:pk>/', ImagesListView.as_view(), name='images_list'),
	path('<int:pk>/add', ImageCreateView.as_view(), name='image_create')
] 