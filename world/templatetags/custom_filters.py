from django import template
import math

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    """Multiplies the given value by the argument."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def floor(value):
    """向下舍入到最近的整数。"""
    try:
        return math.floor(float(value))
    except (ValueError, TypeError):
        return value
