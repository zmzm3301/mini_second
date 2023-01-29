from django import template

from webapp.models import Info

register = template.Library()


@register.simple_tag
def recent_posts(count):
    posts = Info.objects.order_by('-pk')[:count]
    return posts