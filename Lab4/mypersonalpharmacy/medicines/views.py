from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def test(request):
    return HttpResponse("Страница приложения medicines.")


def mlist(request, medid):
    if request.GET:
        print(request.GET)  # http://127.0.0.1:8000/medicines/medlist/1/?name=George&type=medic
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Список лекарств</h1><p>{medid}</p>")


def archive(request, year):
    if int(year) > 2023:
        return redirect('medhome')
    if int(year) < 1800:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Мы не нашли страницу, которую вы искали :( </h1><p>Попробуйте перепроверить поисковый запрос.</p>")
