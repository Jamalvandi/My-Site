from django.urls import path
from website.views import *
urlpatterns = [
    path('' , indexView),
    path('about' , aboutView),
    path('contact' , contactView)
]