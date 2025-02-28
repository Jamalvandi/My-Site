from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from blog.form import CommentForm
from django.contrib import messages

# Create your views here.

def blog_view (request, **kwargs):
    posts = Post.objects.filter(state = 1)
    if kwargs.get("cat_name") != None:
        posts = posts.filter(category__name = kwargs["cat_name"])
    if kwargs.get("author_name")!= None :
        posts = posts.filter(author__name = kwargs["author_name"])
    if kwargs.get("tag_name")!= None :
        posts = posts.filter(tags__name__in = [kwargs["tag_name"]])
    
    paginator = Paginator(posts,3)
    
    
    try:
        page_number = request.GET.get("page")
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(1)
   
   

    posts = {"posts": posts}
    return render(request, "blog/blog-home.html" , posts)

def single_view(request, pid):
    form = CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your comment didnt submiter')
    post = get_object_or_404(Post, pk = pid, state = 1)
    comments = Comment.objects.filter(post = post.id, approved =True)
    context = {'post':post,'comments':comments,'form':form}
    return render(request, "blog/blog-single.html", context)


def blog_search(request):
    posts = Post.objects.filter(state = 1)
    if request.method == "GET":
        if s :=request.GET.get("s"):
            print(s)
            posts = posts.filter(content__contains = s)
    posts ={"posts" : posts}
    return render(request, "blog/blog-home.html",posts)

def test (request , name):
    name ={"name":name}
    return render(request, "test.html" ,name)

    