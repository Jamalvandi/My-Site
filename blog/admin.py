from django.contrib import admin
from blog.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "Empty"
    list_display = ("title","counted_views","state","published_date","created_date")
    list_filter = ("state",)
    search_fields = ["title" , "content"]
    # ordering = ["created time"] :just for admin
admin.site.register(Post,PostAdmin)