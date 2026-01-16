from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestPostsFeed(Feed):
    title = "Мой Блог - Последние посты"
    link = "/rss/"
    description = "Последние посты из моего блога"

    def items(self):
        return Post.objects.order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_pubdate(self, item):
        return item.pub_date

    def item_link(self, item):
        return reverse("post-detail", args=[item.pk])
