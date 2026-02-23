from django import template

register = template.Library()

@register.filter
def currency(value):
    try:
        value = float(value)
    except (ValueError, TypeError):
        return value
    finally:
        formatted = f"{value:.2f}".replace(","," ")
        return f"{formatted} $"
