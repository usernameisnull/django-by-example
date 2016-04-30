# encoding:utf-8
from django.conf.urls import url
from . import views

# 注意列表里的每个元素的正则都是以'$'结尾，因为这是在app(blog)里
# 在mysite的urls.py里的每个正则则反过来，都不要以'$'结尾。
urlpatterns = [
    # post views
    url(r'^$', views.post_detail, name='post_detail'),
]
