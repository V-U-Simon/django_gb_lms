from django import template
from django.urls import reverse
from django.utils.html import format_html

register = template.Library()


# @register.simple_tag(takes_context=True)
# def current_time(context, pattern):
# 	request = context['request']
# 	if re.search(pattern, request.path):

# 		return 'active'
# 	return ''


@register.simple_tag(takes_context=True)
def nav_url(context, params, text_inside, *args, **kwargs):
    """
    render item of navigation.

    necessarily params: url_name_space & text_inside
    additional params: active_class & other_classes by default will be class='active'


    {% load nav_tags %}
    {% nav_url 'url_name_space text_inside' %}
    {% nav_url 'url_name_space text_inside other_classes' %} {# class='active' #}
    {% nav_url 'url_name_space text_inside other_classes active_class' %}

    {% nav_url 'news Новости nav-link active' %}
    """

    url_name_space, *classes = params.split(" ")

    if not "acitve" in classes:
        active_class = "active"
        other_classes = classes
    else:
        active_class, *other_classes = classes
    other_classes = " ".join(other_classes)

    if not url_name_space == "#":
        url = reverse(url_name_space)
    else:
        url = url_name_space

    request = context["request"]
    active_class = active_class if request.path == url else ""

    if kwargs:
        kwargs = "".join({f'{k}="{v}"' for k, v in kwargs.items()})
    else:
        kwargs = ""

    tag = f'<a href="{url}" class="{other_classes} {active_class}" {kwargs}>{text_inside}</a>'
    return format_html(tag)
