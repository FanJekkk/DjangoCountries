Import Django
import json
from MainApp.models import Country, Language

with open("data/countries-list.json") as f:
    countries_data = json.load(f)
    for country_dict in countries_data:
        country = Country(name=country_dict["country"])
        country.save()
        for language_name in country_dict["languages"]:
            language, created = Language.objects.get_or_create(name=language_name)
            country.languages.add(language)
