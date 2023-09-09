from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import *
import random
import requests
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class MedList(ListView):
    model = Medication
    template_name = 'medicines/med_list.html'
    context_object_name = 'posts'
    ordering = ('title',)


class Pharmacies(ListView):
    model = Department
    template_name = 'medicines/pharms.html'
    context_object_name = 'posts'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class NoAvailable(ListView):
    model = Sale
    template_name = 'medicines/no_avail.html'
    context_object_name = 'posts'
    ordering = ('medication', )


def home(request):
    return render(request, "medicines/home.html")


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


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Мы не нашли страницу, которую вы искали :( </h1><p>Попробуйте перепроверить поисковый запрос.</p>")


def bying(request, bying_id):
    purchase = Medication.objects.get(pk=bying_id)

    return render(request, 'medicines/bying.html', {'title': 'Покупка', 'purchase': purchase})


def thanks(request, thanks_id):
    posts = Sale.objects.order_by('medication')
    purchase = Medication.objects.get(pk=thanks_id)
    saled = Sale.objects.all()
    if purchase.quantity == 0:
        purchase.is_available = False
        return render(request, 'medicines/no_avail.html', {'posts': posts, 'title': 'Не куплено'})
    for el in saled:
        if el.medication == purchase:
            el.quantity += 1
            purchase.quantity -= 1
            if purchase.quantity == 0:
                purchase.is_available = False
            el.save()
            purchase.save()
    return render(request, 'medicines/thanks.html', {'posts': posts, 'title': 'Куплено'})


def w_registr(request):
    return render(request, 'medicines/w_registr.html', {'title': 'Добро пожаловать!'})


def medhomew(request):
    posts = Medication.objects.order_by('title')
    return render(request, 'medicines/medhomew.html', {'posts': posts, 'title': 'Лекарства'})


class MedWithoutHome(ListView):
    model = Medication
    template_name = 'medicines/medhomew.html'
    context_object_name = 'posts'
    ordering = ('title', )
