from django import template
from django.conf import settings

register = template.Library()

@register.filter
def subtract(value, arg):
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return 0
    
@register.simple_tag
def get_photo_base_url():
    return settings.PHOTO_BASE_URL
