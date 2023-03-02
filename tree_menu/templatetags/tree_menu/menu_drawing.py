from django import template
from tree_menu import Menu

register = template.Library()


@register.inclusion_tag('template_markups/menu.html', takes_context=True)
def draw_menu(context, slug):
	try:
	 # here I could use the 'select_related()' method but it's only
	 # used in case of a single object, whereas the 'prfetch_selected()' one 
	 # does the same stuff but with a whole set of things
		menu = Menu.objects.prefetch_related('items__items__items__items').get(slug=slug)

		return {'menu': menu, 'context': context}
	except Model.DoesNotExist:
		return {'menu': '', 'context': context}