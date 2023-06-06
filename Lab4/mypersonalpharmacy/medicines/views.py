from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *
import random
import requests
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


def home(request):
    return render(request, "medicines/home.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def test(request):
    response = requests.get('https://cat-fact.herokuapp.com/facts')
    facts = response.json()

    random_fact = None
    if facts:
        random_fact = random.choice(facts)
        if 'source' not in random_fact:
            random_fact['source'] = 'Unknown'
    data = {
        'title': 'Домашняя страница',
        'random_fact': random_fact,
    }
    return render(request, 'medicines/test.html', data)


def about(request):
    return render(request, 'medicines/about.html', {'title': 'О нас'})


def mlist(request):
    posts = Medication.objects.order_by('title')
    if request.GET:
        print(request.GET)  # http://127.0.0.1:8000/medicines/medlist/?name=George&type=medic
    if request.POST:
        print(request.POST)
    return render(request, 'medicines/med_list.html', {'posts': posts, 'title': 'Лекарства'})


def archive(request, year):
    if int(year) > 2023:
        return redirect('medhome')
    if int(year) < 1800:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Мы не нашли страницу, которую вы искали :( </h1><p>Попробуйте перепроверить поисковый запрос.</p>")
