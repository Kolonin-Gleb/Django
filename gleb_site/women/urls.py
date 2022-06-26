# Файл с маршрутами приложения women
# Позволяет реализовать принцип независимости приложений.

from django.urls import path

from .views import *

urlpatterns = [
    # Здесь '' соответствует http://127.0.0.1:8000/ + women/
    # women присоединяется, т.к. в осн. пакете конфигурации сказано, что
    # суффикс нужно добавлять к адресу women/ Т.Е. http://127.0.0.1:8000/women/
    path('', index),
    path('cats/', categories)
]
