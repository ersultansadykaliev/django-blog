from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import Post
class LatestPostsFeed(Feed):
    title = "Мой Блог - Последние посты"
    link = reverse_lazy('post-list')
    description = "Последние посты из моего блога"

    def items(self):
        return Post.objects.all()[:10]

    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.content[:500] + "..." if len(item.content) > 500 else item.content
    def item_pubdate(self, item):
        return item.pub_date