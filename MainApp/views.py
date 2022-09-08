from django.shortcuts import render, HttpResponse
import json
import string
from django.core.paginator import Paginator

with open("data/countries-list.json") as f:
    countries_data = json.load(f)
COUNTRIES_ON_PAGE = 5

def home(request):
    return render(request,"index.html")

def countries(request):
    alphabet = string.ascii_uppercase
    country_names = []
    for country_dict in countries_data:
        country_names.append(country_dict["country"])
    word = request.GET.get("word")
    if word:
        country_names = list(filter(lambda name: name[0] == word, country_names))
    paginator = Paginator(country_names, COUNTRIES_ON_PAGE)
    page_number = request.GET.get('page')
    page_countries = paginator.get_page(page_number)
    return render(request, "countries.html",
                  {"page_countries": page_countries, "alphabet": alphabet, "word": word})

def languages(request):
    langs = set()
    for country in countries_data:
        langs.update(country["languages"])
    return render(request, 'languages.html', {"languages": sorted(langs)})

def countries_languages(request,language):
    country_names = []
    alphabet = string.ascii_uppercase
    for country_dict in countries_data:
        if language in country_dict["languages"]:
            country_names.append(country_dict["country"])
    return render(request, 'countries.html', {"alphabet": alphabet, "page_countries": country_names})

def country_page(request,country_name):
    country = {}
    for country_dict in countries_data:
        if country_dict["country"] == country_name:
            country["name"] = country_dict["country"]
            country["languages"] = country_dict["languages"]
            return render(request, 'country_page.html', {"country": country})