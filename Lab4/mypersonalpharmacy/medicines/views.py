from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["О нас", "Список лекарств", "Войти"]
menu1 = ["Вы знаете", "Что этот сайт", "Сделан для Вас :3"]


def test(request):
    return render(request, 'medicines/test.html', {'menu': menu, 'title': 'Домашняя страница'})


def about(request):
    return render(request, 'medicines/about.html', {'menu': menu1, 'title': 'О нас'})


def mlist(request):
    posts = Medicines.objects.all()
    if request.GET:
        print(request.GET)  # http://127.0.0.1:8000/medicines/medlist/?name=George&type=medic
    if request.POST:
        print(request.POST)
    return render(request, 'medicines/med_list.html', {'posts': posts, 'menu': menu1, 'title': 'Лекарства'})


def archive(request, year):
    if int(year) > 2023:
        return redirect('medhome')
    if int(year) < 1800:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Мы не нашли страницу, которую вы искали :( </h1><p>Попробуйте перепроверить поисковый запрос.</p>")
