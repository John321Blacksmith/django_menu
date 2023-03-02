from django import template

register = template.Library()


@register.inclusion_tag('tree_menu/template_markup/dropdown_menu.html', takes_context=True)
def make_dropdown(context, entity):
	absolute_path = context.request.get_full_path()

	return {
		'entity': entity,
		'abs_path': absolute_path
	}