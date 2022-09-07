from django.shortcuts import render, HttpResponse
import json
import string

def home(request):
    text="Добро пожаловать! Посмотрите <a href='countries-list'>список стран</a>"
    return HttpResponse(text)
def countries(request):
    with open("data/countries-list.json") as f:
        countries_data = json.load(f)
    alphabet = string.ascii_uppercase
    country_names = []
    for country_dict in countries_data:
        country_names.append(country_dict["country"])
    print(country_names)
    result = f"{alphabet}<ol>"
    for i in countries_data:
        result += f"<li><a href='/country/{i['country']}'>{i['country']}</a></li>"
    result+= "</ol>"
    return HttpResponse(result)
def country_page(request,country_name):
    result = f"<h1>{country_name}</h1><br><a href='/countries-list'>К списку стран</a>"
    return HttpResponse(result)