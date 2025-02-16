from django.contrib import admin
from website.models import Contact , Newsletter 
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_Value_display = "Empty"
    list_display = ("name", "email","created_date")
    list_filter = ("email",)
    search_fields = ("name" , "massage")



admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
