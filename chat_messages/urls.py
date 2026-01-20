from django.urls import path
from .views import message, create_salon, salon_list, get_messages_json, delete_salon

urlpatterns = [
    path('salons/', salon_list, name='salon_list'),
    path('salons/create', create_salon, name='create_salon'),
    path('salons/<int:salon_id>/', message, name='salon_messages'),
    path('salon/<int:salon_id>/messages-json/', get_messages_json, name='get_messages_json'),
    path("salon/<int:salon_id>/delete/", delete_salon, name="delete_salon"),

]
