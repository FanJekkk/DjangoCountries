from django.db import models


# В рамках обучающего проекта, такая реализация имеет место быть
# Но, как видно из вашего кода во views.py, после получения информации из БД, вам приходится обрабатывать ее "вручную",
# чтобы получить нужный формат(вид).
# Информацию о странах и языках лучше хранить в виде моделей со связями многие-ко-многим, о реализации можно почитать
# тут: https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_many/#many-to-many-relationships
# тут: https://metanit.com/python/django/5.7.php
# или тут: https://django.fun/ru/docs/django/4.0/topics/db/examples/many_to_many/#many-to-many-relationships
class Country(models.Model):
   country = models.CharField(max_length=100)
   languages = models.CharField(max_length=5000)

