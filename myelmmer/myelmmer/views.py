
from django.shortcuts import render

# Create your views here.
def tnelmer(request):

    # render function takes argument  - request
    # and return HTML as response
    return render(request, "home.html")


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