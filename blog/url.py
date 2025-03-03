from django.urls import path
from blog.views import * # type: ignore
from blog.feed import LatestEntriesFeed

app_name = "blog"

urlpatterns = [
    path("", blog_view , name= "index"),
    path("<int:pid>", single_view , name= "single"),
    path("category/<str:cat_name>", blog_view , name= "category"),
    path("tag/<str:tag_name>", blog_view , name= "tag"),
    path("author/<str:author_name>", blog_view , name= "author"),
    path("search/", blog_search , name= "search"),
    path("rss/feed/", LatestEntriesFeed()),
    # path("<str:name>", test , name= "test"),
]
