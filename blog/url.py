from django.urls import path
from blog.views import * # type: ignore

app_name = "blog"

urlpatterns = [
    path("", blogView , name= "index"),
    path("<int:pid>", singleView , name= "single"),
    # path("<str:name>", test , name= "test"),
]
