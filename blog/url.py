from django.urls import path
from blog.views import * # type: ignore

app_name = "blog"

urlpatterns = [
    path("", blogView , name= "index"),
    path("blog/single", singleView , name= "single"),
]
