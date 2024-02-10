from django import template
from pooltables.models.gallery import Like

register = template.Library()

@register.simple_tag
def total_likes(photo_id):
    return Like.objects.filter(photo_id=photo_id).count()
