from django.urls import path
from accounts.views import *


app_name = "accounts"

urlpatterns =[
    # login
    # path("login", login_view, name = "login"),
    path('login' , login_view, name="login"),
    
    # registrations
    path("register", register_view, name= "register"),
    # logout
    # path("logout" ,logout_view , name= "logout"),
]
