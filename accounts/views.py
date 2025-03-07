from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def login_view(request):
    
    if request.method == "POST":
        if request.user.is_authenticated:
            username = request.POST["username"]
            password = request.POST["password"]    
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                print("Authentication failed")
        else:
            print("Fuke no")
    return render(request,"accounts/login.html")

def logout_view(request):
    pass

def register_view(request):
    return render(request, "accounts/register.html")