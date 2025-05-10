from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    for item in dictionary:
        if item['id_sender__id'] == key:
            return item['total']
    return 0 