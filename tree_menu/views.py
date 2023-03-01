from django.shortcards import render
from django.views.generic import TemplateView
# from django.views.generic.base import ContextMixin
from .models import Menu, MenuEntity
# Create your views here.


class MainView(TemplateView):
	"""This class represents a main menu and all the corresponding behavior on the page."""
	models = (Menu, MenuEntity)
	template_file = 'index.html'

	def get_context(self, **kwargs):
		"""This method returns a bunch of menus that do exist and their respective items."""
		context = super().get_context(**kwargs)
		context['main_points'] = self.models[0].objects.all().filter(existence=True)
		context['subpoints'] = self.models[1].objects.all()

		return context