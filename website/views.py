from django.shortcuts import render
from django.http import HttpResponse , JsonResponse 


def indexView (request) :
    return HttpResponse("<h1>HOME Page<h1>")
def aboutView (request) :
    return HttpResponse("<h1>ABOUT Page<h1>")
def contactView (request) :
    return HttpResponse("<h1>CONTACT Page<h1>")