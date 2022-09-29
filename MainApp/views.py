from django.shortcuts import render, HttpResponse
import json
import string
from django.core.paginator import Paginator
import json
import sqlite3
from MainApp.models import Country

with open("data/countries-list.json") as f:
    countries_data = json.load(f)

# Использовать глобальные переменные крайне не рекомендуется
# ТЕм более, что в рамках данного проекта в этом нет никакой необходимости
COUNTRIES_ON_PAGE = 10
langs = set()
lg = Country.objects.values('languages')

# Форматируйте код в соответствии со стандартом оформления PEP-8
# Например, в PyCharm достаточно нажать: Ctrl + Alt + L - для автоформатирования по PEP-8
def home(request):
    return render(request,"index.html")

def countries(request):
    alphabet = string.ascii_uppercase
    country_names = Country.objects.values('country')
    word = request.GET.get("word")
    if word:
        country_names = Country.objects.values('country').filter(country__startswith=word)
    paginator = Paginator(list(country_names), COUNTRIES_ON_PAGE)
    page_number = request.GET.get('page')
    page_countries = paginator.get_page(page_number)
    return render(request, "countries.html",
                  {"page_countries": page_countries, "alphabet": alphabet, "word": word})

def languages(request):
    for lang in lg:
        langs.update(lang['languages'].split(", "))
    return render(request, 'languages.html', {"languages": sorted(langs)})

def countries_languages(request,language):
    country_names = []
    alphabet = string.ascii_uppercase
    lang_country= Country.objects.values()
    for lc in lang_country:
        langs.update(lc["languages"].split(", "))
    word = request.GET.get("word")
    if language:
        country_names = Country.objects.values().filter(languages__contains=language)
    if word:
        country_names = Country.objects.values().filter(country__startswith=word)
    paginator = Paginator(list(country_names), COUNTRIES_ON_PAGE)
    page_number = request.GET.get('page')
    page_countries = paginator.get_page(page_number)
    return render(request, 'countries.html', {"alphabet": alphabet, "page_countries": page_countries, "word": word,
                                              "languages": langs})

def country_page(request,country_name):
    page_country= Country.objects.values().filter(country=country_name)
    for pg in page_country:
        languages = pg["languages"].split(", ")
    return render(request, 'country_page.html', {"page_country": page_country, "languages": languages })
