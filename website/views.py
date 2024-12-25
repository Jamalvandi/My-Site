from django.shortcuts import render
from django.http import HttpResponse , JsonResponse 


def indexView (request) :
    return render(request , "website/index.html")
def aboutView (request) :
    return render(request , "website/about.html")
def contactView (request) :
    return render(request , "website/contact.html")
def elementsView (request) :
    return render(request , "website/elements.html")    