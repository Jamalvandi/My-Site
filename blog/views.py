from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.

def blogView (request, **kwargs):
    posts = Post.objects.filter(state = 1)
    if kwargs.get("cat_name") != None:
        posts = posts.filter(category__name = kwargs["cat_name"])
    if kwargs.get("author_name")!= None :
        posts = posts.filter(author__name = kwargs["author_name"])
    posts = {"posts": posts}
    return render(request, "blog/blog-home.html" , posts)
def singleView(request, pid):
    post = get_object_or_404(Post, pk = pid, state = 1)
    post = {"post": post}
    return render(request, "blog/blog-single.html", post)

def test (request , name):
    name ={"name":name}
    return render(request, "test.html" ,name)