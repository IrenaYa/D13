from django import template

register = template.Library()

censored_words = ['украли', 'читеров', 'Windows', 'чипов']

@register.filter()
def censor(value):
    for word in censor_list:
        value = value.replace(word[1:], '*' * len(word[1:]))

    return value

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()