from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(state=True)

    def lastmod(self, obj):
        return obj.published_date
    
    # use def location or Models:get_absolute_url 
    def location(self, obj):
        return reverse("blog:single", kwargs={"pid" : obj.id})