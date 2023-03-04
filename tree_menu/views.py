from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Menu
# Create your views here.


class AbsView(TemplateView):
	"""
	This blueprint gives a template of the view to be applied to all the pages.
	"""
	# pick up the working model
	model = Menu
	
	def get_context_data(self, *args, **kwargs):
		"""This method returns a bunch of menus that do exist and their respective items and subitems."""
		context = super().get_context_data(*args, **kwargs)
		context['menu_objects'] = self.model.objects.all()
		print(context)
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

	
class BooksView(AbsView):
	"""Vehicles view class."""
	template_name = 'tree_menu/books.html'
	