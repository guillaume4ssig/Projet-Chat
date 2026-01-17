from django.shortcuts import render, redirect
from .models import Message
from django.http import HttpResponse
from django.template import Template
from django.contrib.auth.models import User


def message(request):
    if request.method =='POST':
        message = request.POST.get("content")

        Message.objects.create(sender='anonyme(pour mtn)', content=message)
        return redirect('envoie')
    msgs = Message.objects.order_by('-date')
    return render(request, "messages/message.html", {"msgs": msgs})