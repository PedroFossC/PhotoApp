from django.urls import path
from .views import HomePage, ImagesFolderDetail

app_name = 'travel_book'

urlpatterns = [
	path('', HomePage.as_view(), name='home_page'),
	path('<int:pk>/', ImagesFolderDetail.as_view(), name='folder_detail')
]