from django.db import models
from django.urls import reverse


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
	slug = models.SlugField(max_length=255, verbose_name='slug', 
							help_text='Use this snippet along with a template tag as a name of the rendered menu')
	named_url = models.CharField(max_length=255, blank=True, verbose_name='unique_name')
	url = models.CharField(max_length=255, verbose_name='url')

	class Meta:
		verbose_name = 'menu'
		verbose_name_plural = 'menus'

	def get_full_path(self):
		if self.named_url:
			url = reverse(self.named_url)
		else:
			url = f'/{self.slug}/'

		return url

	def __str__(self):
		return self.title


class MenuEntity(BaseMenu):
	"""
	This blueprint represents a child entity of the base menu.
	"""
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='menu', blank=True, null=True)
	title = models.CharField(max_length=50, verbose_name='title')
	named_url = models.CharField(max_length=255, verbose_name='url pattern', blank=True)

	class Meta:
		verbose_name = 'menu entity'
		verbose_name_plural = 'menu entities'

	def get_url(self):
		if self.named_url:
			url = reverse(self.named_url)
		elif self.url:
			url = self.url
		else:
			url = '/'

		return url

	def __str__(self):
		return self.title


class SubMenuEntity(BaseMenu):
	"""
	This blueprint represents a child entity from the Menu entity.
	"""
	menu_entity = models.ForeignKey(MenuEntity, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, verbose_name='title')
	named_url = models.CharField(max_length=255, verbose_name='url pattern', blank=True)
	
	class Meta:
		verbose_name = 'sub-entity'
		verbose_name_plural = 'sub-entities'

	def get_full_url(self):
		"""This method gets a url of the parent item and 
		   returns a full url of the entity."""
		parent_url = None
		pass

	def __str__(self):
		return self.title