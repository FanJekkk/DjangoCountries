"""DjangoCountires URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('countries-list', views.countries, name="countries"),
    path('country/<str:country_name>',views.country_page, name="country"),
    path('countries-list/<str:language>', views.countries_languages, name="countries_languages"),
    path('languages/', views.languages, name="languages")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Вы создали неплохой .gitignore, но, видимо, вы сначала сделали коммит, а только потом добавили gitignore:
# 1. Настройки PyCharm(.idea) также ошибочно были затянуты в репозиторий
# 2. Файл .DS_Store - определенной в репозитории лишний
# 3. Файл БД тоже попал в репозиторий
