from django import template
from tree_menu.models import Menu

register = template.Library()


@register.inclusion_tag('tree_menu/template_markup/menu_blueprint.html', takes_context=True)
def draw_menu(context, slug):
	"""
	This function does creation of the menu based on the slug-word spicified on the django admin page.
	"""
	try:
		# trying to receive the menus dedicated for a menu with a particular slug only
		menu_objects = Menu.objects.all().filter(slug=slug)
		return {'menu_objects': menu_objects, 'context': context}
		
	except Menu.DoesNotExist as err:
		print(err)
		return {'menu_objects': '', 'context': context}