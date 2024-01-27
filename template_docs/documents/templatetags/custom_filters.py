from django import template

register = template.Library()

@register.filter
def get_dictionary_item(dictionary,key):
    return dictionary.get(key)

@register.filter
def index(arr, idx):
    try:
        return arr[idx]
    except (IndexError, TypeError):
        return None
    
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, None)

@register.filter(name='range')
def filter_range(start, end):
    return range(start, end)


@register.filter
def get_index(sequence, position):
    return sequence[position]