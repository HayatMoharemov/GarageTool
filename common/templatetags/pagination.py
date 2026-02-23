from django import template
from django.core.paginator import Paginator

register = template.Library()

@register.inclusion_tag('common/paginator.html', takes_context=True)
def paginator(context, object_list, per_page=10):
    page = context['request'].GET.get('page', 1)
    page_obj = Paginator(object_list, per_page).get_page(page)

    return {
        'page_obj': page_obj
    }