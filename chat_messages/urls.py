from django.urls import path
from . import views

urlpatterns=[
    path('envoie', views.message, name='envoie')
]