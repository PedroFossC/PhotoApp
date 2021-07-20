from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	pass

class ImageFolder(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='folder')
	name = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	country = models.CharField(max_length=30, default='')

	def __str__(self):
		return f'{self.name}'

def handle_upload(instance, filename):
	return f'images/{instance.folder.user}/{instance.folder.pk}/{filename}'
class Image(models.Model):
	folder = models.ForeignKey(ImageFolder, on_delete=models.CASCADE, related_name=f'image')
	image = models.ImageField(upload_to=handle_upload)