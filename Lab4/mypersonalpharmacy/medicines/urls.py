from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', test, name = 'medhome'),  # http://127.0.0.1:8000/medicines/
    path('about/', about, name='about'),  # http://127.0.0.1:8000/medicines/about/
    path('medlist/', mlist),  # http://127.0.0.1:8000/medicines/medlist/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # http://127.0.0.1:8000/medicines/archive/1999/

]
