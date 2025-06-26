from plistlib import dumps

from django import template

register = template.Library()


@register.filter(name='is_current_category')
def is_current_category(current_category, category_slug=None):
    if (category_slug is None and current_category == '') or current_category == category_slug:
        return 'active'
    return ''


@register.filter()
def minus(price, discount):
    return price - discount


