# encoding: utf-8
from django.contrib import admin
from .models import Post,Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # 当在后台点开Post这个链接出现详细页面的时候，出现的字段。
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # 详细页面的右侧边栏
    list_filter = ('status', 'created', 'publish', 'author')
    # 搜索框
    search_fields = ('title', 'body')
    # 用models.Post.title预先填充models.Post.slug这个字段。
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    # 这个ordering应该只是在获得数据库结果的排序。
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
