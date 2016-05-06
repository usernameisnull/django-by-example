# encoding:utf-8

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    """
    自定义的manager
    """

    def get_queryset(self):
        temp = super(PublishedManager, self).get_queryset().filter(status='published')
        return temp


class Post(models.Model):
    tags = TaggableManager()
    # todo:下面用了自定义的manager，这里就必须显示的定义默认的manager，why？
    objects = models.Manager()
    # 上面自定义的manger
    published = PublishedManager()
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # 反向查找
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             # 这里应该是往url里传的参数，列表里的元素的顺序应该是有讲究的，这里是不是能用字典
                             self.publish.strftime('%m'),
                             # 这里的2个strftime的格式化字符串生成的都是两位数的，为了和url里的参数匹配
                             self.publish.strftime('%d'),
                             self.slug])
        # 测试reverse url，在mysite.urls里定义了对于的url
        #  return reverse('blog1:post_detail')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return u'Comment by {} on {}'.format(self.name, self.post)
