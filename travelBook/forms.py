from django import forms
from .models import ImageFolder, Image, User
from django.contrib.auth.forms import UserCreationForm, UsernameField


class FolderCreateForm(forms.ModelForm):
	class Meta:
		model = ImageFolder
		fields = ('name', 'description', 'city', 'country')

class ImageCreateForm(forms.Form):
	images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}