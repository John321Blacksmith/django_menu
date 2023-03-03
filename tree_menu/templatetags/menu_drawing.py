from django import template
from tree_menu.models import Menu

register = template.Library()


@register.inclusion_tag('tree_menu/template_markup/menu_blueprint.html', takes_context=True)
def draw_menu(context, slug):
	try:
		main_points = Menu.objects.all().filter(existence=True)

		return {'main_points': main_points, 'context': context}
	except Menu.DoesNotExist as err:
		print(err)
		return {'main_points': '', 'context': context}