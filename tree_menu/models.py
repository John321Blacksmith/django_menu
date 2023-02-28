from django.db import models
from django.urls import reverse

# Create your models here.

# define a blue print of the base menu object
class BaseMenu(models.Model):
	title = models.CharField(max_length=50, verbose_name='title')
	slug = models.SlugField(max_length=255, verbose_name='slug', unique=True,
							help_text='Use this snippet along with a template tag as a name of the rendered menu')
	named_url = models.CharField(max_length=255)


	def __str__(self):
		return self.title
