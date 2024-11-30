from django.shortcuts import render
from django.http import HttpResponse , JsonResponse 


def indexView (request) :
    return render(request , "index.html")
def aboutView (request) :
    return render(request , "about.html")
def contactView (request) :
    return render(request , "website/contact.html")    