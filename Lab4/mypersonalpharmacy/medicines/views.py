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
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    image_url = response.json()['message']
    context = {
        'title': 'О нас',
        'image_url': image_url,
    }
    return render(request, 'medicines/about.html', context)


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


def bying(request, bying_id):
    purchase = Medication.objects.get(pk=bying_id)
    saled = Sale.objects.all()
    for el in saled:
        if el.medication == purchase:
            print("dkdkd")
            el.quantity += 1
            purchase.quantity -= 1
            if purchase.quantity == 0:
                purchase.is_available = False
    return render(request, 'medicines/bying.html', {'title': 'Покупка', 'purchase': purchase})


def thanks(request):
    posts = Sale.objects.order_by('medication')
    return render(request, 'medicines/thanks.html', {'posts': posts, 'title': 'Куплено'})


def w_registr(request):
    return render(request, 'medicines/w_registr.html', {'title': 'Добро пожаловать!'})


def medhomew(request):
    posts = Medication.objects.order_by('title')
    return render(request, 'medicines/medhomew.html', {'posts': posts, 'title': 'Лекарства'})
