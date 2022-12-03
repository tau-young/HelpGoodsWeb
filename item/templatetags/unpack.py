from django import template

register = template.Library()

@register.simple_tag
def unpack(alist, index):
	return alist[index]