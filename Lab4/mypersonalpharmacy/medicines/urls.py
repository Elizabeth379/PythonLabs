from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', test, name = 'medhome'),  # http://127.0.0.1:8000/medicines/
    path('medlist/<int:medid>/', mlist),  # http://127.0.0.1:8000/medicines/medlist/1/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # http://127.0.0.1:8000/medicines/archive/1999/

]
