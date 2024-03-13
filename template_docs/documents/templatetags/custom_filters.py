from django import template
from num2words import num2words
from datetime import datetime


register = template.Library()



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

@register.filter
def custom_range(value):
   return range(1, value + 1)

# @register.filter(name='number_to_words')
# def number_to_words(value, lang='en'):
#     return num2words(value, lang=lang)


@register.filter(name='number_to_words')
def number_to_words(value, args):

    array = args.split(',')

    currency = array[0]
    lang = array[1]
     
    try:
        cleaned_value = value.replace(' ', '').replace(',', '.')

        if cleaned_value.startswith('-'):
           cleaned_value = cleaned_value[1:]

        value = float(cleaned_value)
    except ValueError:
        return value

    integer_part, decimal_part = str(value).split('.')

    integer_text = num2words(int(integer_part), lang=lang)

    decimal_text = f"and {decimal_part}/100" if decimal_part else ""

    result = f"{integer_text} {currency}"
    if decimal_text:
        result += f" {decimal_text}"

    return result

@register.filter
def string_to_date(date_str, format_str):
    return datetime.strptime(date_str, format_str)


    