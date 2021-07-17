

from django import template
from blog.models import Post
register = template.Library()

@register.inclusion_tag('blog/latest_posts.html')
def latest_posts():
    l_posts = Post.objects.all()[0:5]
    context ={
    'l_posts':l_posts
    }
    return context

