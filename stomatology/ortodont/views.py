from django.shortcuts import render


def index(request):
    return render(request, 'ortodont/index.html')


def about(request, slug):
    return render(request, 'ortodont/about.html')


def contact(request, slug):
    return render(request, 'ortodont/contact.html')


def services(request, slug):
    return render(request, 'ortodont/services.html')
