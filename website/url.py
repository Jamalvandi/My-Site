from django.urls import path
from website.views import *
# if had molty app and url name be in more than one place
app_name = "website"
urlpatterns = [
    path('' , index_view, name="index"),
    path('about' , about_view, name= "about"),
    path('contact' , contact_view, name= "contact"),
    path('newsletter' , newsletter_view, name= "newsletter"),
    path('elements' , elements_view, name="elements"),
]