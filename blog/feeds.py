from django.contrib.syndication.views import Feed
from .models import Post
from django.template.defaultfilters import truncatewords


class LatestPostsFeed(Feed):
    title = "My Blog"
    link = '/blog/'
    description = 'Newest posts of my blog'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
