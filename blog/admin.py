from django.contrib import admin
from blog.models import Post , Category
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
admin.site.register(Post,PostAdmin)
admin.site.register(Category)