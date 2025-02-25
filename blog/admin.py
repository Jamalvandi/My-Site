from django.contrib import admin
from blog.models import Post , Category, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "Empty"
    list_display = ("title","author","counted_views","state","published_date","created_date")
    list_filter = ("state","author")
    search_fields = ["title" , "content"]
    summernote_fields = ('content',)
    # ordering = ["created time"] :just for admin
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "Empty"
    list_display = ("name","post","approved","created_date")
    list_filter = ("post","approved")
    search_fields = ["name" , "post"]
    
    
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)