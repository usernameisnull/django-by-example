# encoding:utf-8
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    """
    自定义的manager
    """
    def get_queryset(self):    
        temp = super(PublishedManager, self).get_queryset().filter(status='published')
        return temp

class Post(models.Model):
    # todo:下面用了自定义的manager，这里就必须显示的定义默认的manager，why？
    objects=models.Manager()
    # 上面自定义的manger
    published=PublishedManager()
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
    """
    在模板里要用到的反向url
    """
        return reverse('blog:post_detail',  # blog应该是mysite/urls.py里的namespace, post_detail应该是blog/urls.py里的name
                        args=[self.publish.year,    # 这里应该是往url里传的参数，列表里的元素的顺序应该是有讲究的，这里是不是                                                    #能用字典？
                              self.publish.strftime('%m'),  # 这里的2个strftime的格式化字符串生成的都是两位数的，为了和url里#                                                            # 的正则相匹配
                              self.publish.strftime('%d'),
                              self.slug])

