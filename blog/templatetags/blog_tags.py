from django import template
from blog.models import Post
from blog.models import Category
register = template.Library()

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value):
    return value[:20]

@register.inclusion_tag('blog/blog-popularpost.html')
def popularpost():
    posts = Post.objects.filter(status=1).order_by('published_date')
    return {'posts': posts}

@register.inclusion_tag('blog/blog-catgories.html')
def postCatgories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'catgories': cat_dict}

