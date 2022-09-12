from django.db import models

class Country(models.Model):
   country = models.CharField(max_length=100)
   languages = models.CharField(max_length=5000)

