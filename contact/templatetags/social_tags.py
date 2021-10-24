from django import template
from ..models import Social, About

register = template.Library()


@register.simple_tag()
def get_social_tags():
    """Вывод ссылок соц.сетей"""
    return Social.objects.all()


@register.simple_tag()
def get_about():
    """Вывод инфо о нас"""
    return About.objects.last()
