from django import template


register = template.Library()

# register using decrotor
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all the values of arg from the string!
    """
    return value.replacve(arg,'')

# register.filter('cut',cut)
