from django.shortcuts import render, HttpResponse, Http404
import json
import string
from django.core.paginator import Paginator
import json
import sqlite3
from MainApp.models import Country, Language

# with open("data/countries-list.json") as f:
#    countries_data = json.load(f)

# Использовать глобальные переменные крайне не рекомендуется
# ТЕм более, что в рамках данного проекта в этом нет никакой необходимости
COUNTRIES_ON_PAGE = 10


# Форматируйте код в соответствии со стандартом оформления PEP-8
# Например, в PyCharm достаточно нажать: Ctrl + Alt + L - для автоформатирования по PEP-8
def home(request):
    return render(request, "index.html")


def countries(request):
    alphabet = string.ascii_uppercase
    country_names = Country.objects.values('name').order_by('name').distinct()
    word = request.GET.get('word')
    if word:
        country_names = Country.objects.values('name').filter(name__startswith=word)
    paginator = Paginator(list(country_names), COUNTRIES_ON_PAGE)
    page_number = request.GET.get('page')
    page_countries = paginator.get_page(page_number)
    return render(request, "countries.html",
                  {"page_countries": page_countries, "alphabet": alphabet, "word": word})


def languages(request):
    langs = Language.objects.values('name').order_by('name')
    return render(request, 'languages.html', {"languages": langs})


def countries_languages(request, language):
    alphabet = string.ascii_uppercase
    word = request.GET.get('word')
    country_names = Country.objects.values().filter(languages__name=language)
    if word:
        country_names = Country.objects.values().filter(name__startswith=word)
    return render(request, 'countries.html', {"alphabet": alphabet, "page_countries": country_names})


def country_page(request, country_name):
    languages = Language.objects.values().filter(country__name=country_name)
    country = Country.objects.values('name').filter(name=country_name).distinct()
    return render(request, 'country_page.html', {"country": country, "languages": languages})
