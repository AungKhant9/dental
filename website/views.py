from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def contact(request):
    return render(request, 'contact.html', {})
