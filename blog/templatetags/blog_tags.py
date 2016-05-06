# encoding:utf-8
from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag
def total_posts():
    # 返回一个数字，总的已发表的blog数,tag名:total_posts
    return Post.published.all().count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    # 最近发表的blog(默认为5)，按照发表时间，降序排列，tag名:show_latest_posts,渲染的html为blog/post/latest_posts.html
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.assignment_tag
def get_most_commented_posts(count=5):
    # 评论最多的blog(默认为5)，降序排列，tag名:get_most_commented_posts
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='mark_down')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
