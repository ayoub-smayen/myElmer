
from django.shortcuts import render,redirect

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView




def error_404(request):
        data = {}
        return render(request,'404.html', data)

def error_500(request):
        data = {}
        return render(request,'500.html', data)

def blogfire(req):
    return render(req,"blogfire.html")

def create_news(req):
    return render(req,"news.html")

def forum1(req):
    return render(req,"forums.html")
def cooments(req):
    return render(req , "mycomment.html")

def foodhome(request):
    return render(request, "main/home.html")
def bookhomepage(request):
    return redirect("https://mysocialchaty.netlify.app/bookevent.html")

# Create your views here.
def tnelmer(request):

    # render function takes argument  - request
    # and return HTML as response
    return render(request, "home.html")

def bookevent(request):
    return render(request,"bookevent.html")
def tnelmer3(request):

    # render function takes argument  - request
    # and return HTML as response
    return render(request, "mymaps.html")


def tnelmer2(request):

    # render function takes argument  - request
    # and return HTML as response
    return render(request, "notes.html")

def tnelmer4(request):

    # render function takes argument  - request
    # and return HTML as response
    return render(request, "clashGame.html")

def tnelmer5(request):

    # render function takes argument  - request
    # and return HTML as response
    return render(request, "mysites.html")