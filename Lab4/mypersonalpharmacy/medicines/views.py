from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    return HttpResponse("Страница приложения medicines.")


def mlist(request):
    return HttpResponse("<h1>Список лекарств</h1>")
