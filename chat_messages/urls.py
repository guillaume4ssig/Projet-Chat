from django.urls import path
from .views import message, create_salon, salon_list

urlpatterns = [
    path('salons/', salon_list, name='salon_list'),
    path('salons/create', create_salon, name='create_salon'),
    path('salons/<int:salon_id>/', message, name='salon_messages'),
]
