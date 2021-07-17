

from django import template
from blog.models import Comment
register = template.Library()

@register.inclusion_tag('blog/latest_comments.html')
def latest_comments():
    l_comments = Comment.objects.filter(active=True)[0:5]
    context ={
    'l_comments':l_comments
    }
    return context

