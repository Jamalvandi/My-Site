from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "blog newest posts"
    link = "/rss/feed"
    description = "Best post ever ."

    def items(self):
        return Post.objects.filter(state = True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]

    # item_link is only needed if Post has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse("news-item", args=[item.pk])