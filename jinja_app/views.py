from django.shortcuts import render


# Create your views here.

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')


def gallery(request):
    return render(request, 'gallery.html')
