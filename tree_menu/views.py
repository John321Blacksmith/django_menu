from django.shortcuts import render
from django.views.generic import TemplateView
# from django.views.generic.base import ContextMixin
from .models import Menu, MenuEntity
# Create your views here.


class MainView(TemplateView):
	"""This class represents a main menu and all the corresponding behavior on the page."""
	model = Menu
	template_name = 'tree_menu/index.html'

	def get_context_data(self, *args, **kwargs):
		"""This method returns a bunch of menus that do exist and their respective items."""
		context = super().get_context_data(*args, **kwargs)
		context['main_points'] = self.model.objects.all().filter(existence=True)

		print(context)

		return context