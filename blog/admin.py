from django.contrib import admin
from blog.models import Post , Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "Empty"
    list_display = ("title","author","counted_views","state","published_date","created_date")
    list_filter = ("state","author")
    search_fields = ["title" , "content"]
    # ordering = ["created time"] :just for admin
admin.site.register(Post,PostAdmin)
admin.site.register(Category)