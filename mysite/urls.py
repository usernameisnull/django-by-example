# encoding: utf-8
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
blog1_pattern = []
sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # app_name:  application namespace
    # namespace: instance namespace
    # 下面这行app_name和namespace一致，表示是default application instance
    # 当在blog/templates/blog/post/list.html里进行url反向查找post.get_absolute_url的时候，
    # 去models.py里对于的Post类的get_absolute_url方法，reverse(blog:post_detail)
    # 冒号前面的blog的查找就在这里查找
    # 根据官方文档,查找顺序如下:
    # 1. 找current_app，这里是没有的
    # 2. 在url定义里app_name和namespace都为blog的，找到第一个，如果没找到往下
    # 3. 找最后一个app_name为blog的
    # 4. 找namespace为polls的
    url(r'^blog/', include('blog.urls',
                           namespace='blog',  # namespace
                           app_name='blog')),  # application namespace

    url('^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitempaps.views.sitemap'),
    url(r'^blog1/', include('blog1.urls',
                            namespace='blog1',
                            app_name='blog3')),
    url(r'^blog2/', include('blog2.urls',
                            namespace='blog2',
                            app_name='blog2')),
]
