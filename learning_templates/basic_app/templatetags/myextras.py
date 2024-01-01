from django import template

register = template.Library()

@register.filter(name='cut')
#when passing a func inside a func call
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)