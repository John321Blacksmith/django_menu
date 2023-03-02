from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Menu, MenuEntity
# Create your views here.


class AbsView(TemplateView):
	"""
	This blueprint gives a template of the view to be applied to all the pages.
	"""
	model = Menu

	def get_context_data(self, *args, **kwargs):
		"""This method returns a bunch of menus that do exist and their respective items."""
		context = super().get_context_data(*args, **kwargs)
		context['main_points'] = self.model.objects.all().filter(existence=True)

		return context


class IndexView(AbsView):
	"""Index view class."""
	template_name = 'tree_menu/index.html'


class ProductView(AbsView):
	"""Products view class."""
	template_name = 'tree_menu/products.html'


class VehicleView(AbsView):
	"""Vehicles view class."""
	template_name = 'tree_menu/vehicles.html'