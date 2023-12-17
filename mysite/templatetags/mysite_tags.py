from django import template
from blog.models import Post
from blog.models import Category
register = template.Library()

@register.simple_tag
def get_last_six_posts():
    return Post.objects.all().prefetch_related('category').order_by('-published_date')[:6]
    