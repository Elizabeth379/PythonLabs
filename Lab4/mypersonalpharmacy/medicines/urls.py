from django.urls import path

from .views import *

urlpatterns = [
    path('', test),  # http://127.0.0.1:8000/medicines/
    path('medlist/', mlist),  # http://127.0.0.1:8000/medicines/medlist/

]
