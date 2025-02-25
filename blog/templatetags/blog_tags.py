from unicodedata import category
from django import template
from blog.models import Post , Category ,Comment

register = template.Library()

@register.inclusion_tag("blog/blog-latest-posts.html")
def latestposts(arg = 2):
    sql_posts = Post.objects.filter(state = 1).order_by("published_date")[:arg]
    posts = {"posts": sql_posts}
    return posts

@register.inclusion_tag("blog/blog-categories.html")
def postcategories():
    cat_dec ={}
    posts = Post.objects.filter(state = 1)
    categories = Category.objects.all()
    for name in categories:
            cat_dec[name] = posts.filter(category = name).count()
     
    return  {"categories": cat_dec}
@register.simple_tag(name = "comments_count")
def functions(pid):
    return Comment.objects.filter(post = pid, approved =True).count()
