from django.urls import path
from . import views

# define an app name
app_name = 'tree_menu'

# my urls are below
urlpatterns = [
	path('', views.MainView.as_view(), name='index'),
	
]