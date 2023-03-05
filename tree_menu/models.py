from django.db import models
from django.urls import reverse


# Create your models here.

class AbsMenu(models.Model):
	"""
	The abstract class that gives the common featuers appliable to all classes below.
	"""
	existence = models.BooleanField(default=True, verbose_name='visibility')
	order = models.IntegerField(default=10, verbose_name='order')

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


# define a blueprint of the base menu object
class Menu(AbsMenu):
	"""
	The father model that represents a menu item in general.
	"""
	title = models.CharField(max_length=50, verbose_name='title')
	slug = models.SlugField(max_length=255, verbose_name='slug', 
							help_text='Use this snippet along with a template tag as a name of the rendered menu')
	named_url = models.CharField(max_length=255, blank=True, verbose_name='named_url')
	url = models.CharField(max_length=255, verbose_name='url')

	class Meta:
		verbose_name = 'menu'
		verbose_name_plural = 'menus'

	def __str__(self):
		return self.title


class MenuEntity(AbsMenu):
	"""
	This blueprint represents a child entity of the base menu.
	"""
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='menu', blank=True, null=True)
	title = models.CharField(max_length=50, verbose_name='title')
	named_url = models.CharField(max_length=255, verbose_name='named_url', blank=True)

	class Meta:
		verbose_name = 'menu entity'
		verbose_name_plural = 'menu entities'
		
	def __str__(self):
		return self.title


class SubMenuEntity(AbsMenu):
	"""
	This blueprint represents a child entity from the Menu entity.
	"""
	menu_entity = models.ForeignKey(MenuEntity, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, verbose_name='title')
	named_url = models.CharField(max_length=255, verbose_name='named_url', blank=True)
	
	class Meta:
		verbose_name = 'sub-entity'
		verbose_name_plural = 'sub-entities'

	def __str__(self):
		return self.title