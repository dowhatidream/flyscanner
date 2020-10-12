from django.shortcuts import render
from .models import Country


def index(request):
    countries = Country.objects.all()
    return render(request, 'recommender/index.html', {
        'index': countries
    })


def detail(request, cID):
    country = Country.objects.get(pk=cID)
    return render(request, 'recommender/detail.html', {
        'detail': country
    })
