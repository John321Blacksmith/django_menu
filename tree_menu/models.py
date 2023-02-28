from django.db import models
from django.urls import reverse

# Create your models here.

class BaseMenu(models.Model):
	
	existence = models.BooleanField(default=True, verbose_name='visibility')

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


# define a blueprint of the base menu object
class Menu(BaseMenu):
	"""The father model that represents a menu item in general."""
	title = models.CharField(max_length=50, verbose_name='title')
	slug = models.SlugField(max_length=255, verbose_name='slug', unique=True,
							help_text='Use this snippet along with a template tag as a name of the rendered menu')
	named_url = models.CharField(max_length=255)

	def __str__(self):
		return self.title


class MenuEntity(BaseMenu):
	"""This blueprint"""
	menu = models.ForeignKey(BaseMenu, on_delete=models.CASCADE)
	title = # title of the menu item
	parent = # parent menu items
	url = # unique url for the item
	named_url = # defined url pattern

	class Meta:
		verbose_name = 'menu title'
		verbose_name_plural = 'menu titles'

	def __str__(self):
		return self.title
