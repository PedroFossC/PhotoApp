from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	pass

class ImageFolder(models.Model):
	name = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	country = models.CharField(max_length=30, default='')

def handle_upload(instance, filename):
	return f'images/{instance.user.id}/{instance.ImageFolder.pk}/{filename}'
class Image(models.Model):
	ImageFolder = models.ForeignKey(ImageFolder, on_delete=models.CASCADE, related_name=f'image')
	image = models.ImageField(upload_to=handle_upload)