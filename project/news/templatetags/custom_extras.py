from django import template

register = template.Library()

@register.filter
def lower(value):
    return value.lower()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag(takes_context = True, name = "tagname")
def func(context, other_arg):
    pass


@register.filter
def hide_forbidden(value):
    words = value.split()
    result = []
    for word in words:
        if word in forbidden_words:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)