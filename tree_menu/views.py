from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import BaseMenu
# Create your views here.

class MainView(TemplateView):
	template = 'index.html'