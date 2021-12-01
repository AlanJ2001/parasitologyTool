from django import template
from parasitologyTool.models import Parasite

register = template.Library()

@register.inclusion_tag('parasitologyTool/parasite_list.html')
def get_parasite_list(current_category=None):
	return {'parasites': Parasite.objects.all(),
	        'current_category':current_category}