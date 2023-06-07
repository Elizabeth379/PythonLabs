from django.urls import path, re_path

from .views import *
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('medhome/', views.test, name='medhome'),  # http://127.0.0.1:8000/medicines/
    path('about/', views.about, name='about'),  # http://127.0.0.1:8000/medicines/about/
    path('medlist/', views.mlist, name='medlist'),  # http://127.0.0.1:8000/medicines/medlist/
    path('pharms/', views.pharms, name='pharms'),
    path('bying/<int:bying_id>/', views.bying, name='bying'),
    path('thanks/<int:thanks_id>/', views.thanks, name='thanks'),
    path('no_avail/', views.no_avail, name='no_avail'),
    path('w_registr/', views.w_registr, name='w_registr'),
    path('medhomew/', views.medhomew, name='medhomew'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # http://127.0.0.1:8000/medicines/archive/1999/

]
