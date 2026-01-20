from django.contrib import admin
from .models import Salon, Message

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'salon', 'sender', 'date')
    list_filter = ('salon', 'sender')
    search_fields = ('content',)