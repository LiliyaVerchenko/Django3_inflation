from django import template

register = template.Library()

@register.filter()
def to_color(value):
    if value:
        value = float(value)
        if value < 0:
            return '#008000'
        elif 1 <= value <= 1.99:
            return '#FFB6C1'
        elif 2 <= value <= 4.99:
            return '#F08080'
        elif value >= 5:
            return '#FF0000'
    return '#FFFFFF'
