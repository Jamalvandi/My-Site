from django.urls import path
from website.views import *
# if had molty app and url name be in more than one place
app_name = "website"
urlpatterns = [
    path('' , indexView, name="index"),
    path('about' , aboutView, name= "about"),
    path('contact' , contactView, name= "contact"),
    path('elements' , elementsView, name="elements"),
]