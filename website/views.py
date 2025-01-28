from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse 
from website.form import ContactForm, NewsletterForm

def index_view (request) :
    return render(request , "website/index.html")
def about_view (request) :
    return render(request , "website/about.html")
def contact_view (request) :
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:        
        form= ContactForm(request.GET)
        
    c_form = {"form" : form}
    return render(request , "website/contact.html", c_form)

def newsletter_view (request) :
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            referer_url = request.META.get('HTTP_REFERER', '/')
            return redirect(referer_url)
        return HttpResponse("/")

def elements_view (request) :
    return render(request , "website/elements.html")    