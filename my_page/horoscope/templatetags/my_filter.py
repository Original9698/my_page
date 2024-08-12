from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
@register.filter(name = 'split')
def split(value,key=' '):
    return value.split(key)