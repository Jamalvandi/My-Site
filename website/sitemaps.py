from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "never"

    def items(self):
        return ["website:index", "website:contact", "website:about"]

    def location(self, item):
        return reverse(item)
