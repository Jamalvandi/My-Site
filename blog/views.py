from django.shortcuts import render

# Create your views here.

def blogView (request):
    return render(request, "blog/blog-home.html")
def singleView(request):
    return render(request, "blog/blog-single.html")