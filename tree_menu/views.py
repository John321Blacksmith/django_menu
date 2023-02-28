from django.http import HttpResponse
from .models import BaseMenu
# Create your views here.


class Categories:
	model = BaseMenu
	template_name = 'index.html'

	def get(self, request, **kwargs):
		context = super().get_context_data(*args, **kwargs)

		context['categories'] = BaseMenu.objects.all.filter(existence=True)

		return HttpResponse(context)