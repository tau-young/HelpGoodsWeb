from django import template

register = template.Library()

@register.simple_tag
def digin(alist, index):
	return alist[index]

@register.simple_tag
def titler(head):
	return head.replace('_', ' ').title() if not head.isupper() else head.replace('_', ' ')

@register.simple_tag
def underline(head):
	return head.replace(' ', '_')