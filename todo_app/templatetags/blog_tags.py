from django import template

from ..models import Todo

register = template.Library()

@register.inclusion_tag('todo_app/priorities.html')
def high_priority(count = 5):
	todos = Todo.objects.filter(priority = 'high').order_by('-created')[:count]
	return {'todos':todos}

@register.inclusion_tag('todo_app/priority_low.html')
def low_priority(count = 5):
	todos = Todo.objects.filter(priority = 'low').order_by('-created')[:count]
	return {'todos':todos}

@register.inclusion_tag('todo_app/priority_medium.html')
def medium_priority(count = 5):
	todos = Todo.objects.filter(priority = 'medium').order_by('-created')[:count]
	return {'todos':todos}