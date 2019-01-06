from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def convert_slashes(value):
    return value.replace('/','forward_slash')
