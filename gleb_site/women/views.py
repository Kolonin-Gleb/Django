from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

# Функции формирующие ответы для разных url адресов.

def index(request):
    return HttpResponse("Страница приложения women.")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям приложения women</h1>")

