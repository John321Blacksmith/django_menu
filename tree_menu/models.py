from django.db import models


# Create your models here.

class BaseMenu(models.Model):
	existence = models.BooleanField(default=True, verbose_name='visibility')
	order = models.IntegerField(default=10, verbose_name='order')

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
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='menu', blank=True, null=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='parent', blank=True, null=True)
	title = models.CharField(max_length=50, verbose_name='title')
	url = models.CharField(max_length=255, verbose_name='url')
	named_url = models.CharField(max_length=255, verbose_name='url pattern', blank=True)

	class Meta:
		verbose_name = 'menu title'
		verbose_name_plural = 'menu titles'

	def __str__(self):
		return self.title