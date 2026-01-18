from django.shortcuts import render, redirect
from .models import Message
from django.http import HttpResponse
from django.template import Template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def message(request):
    if request.method =='POST':
       
        print(request.user)

        message = request.POST.get("content")

        Message.objects.create(sender=request.user, content=message)
        return redirect('envoie')
    msgs = Message.objects.order_by('-date')

    return render(request, "messages/message.html", {"msgs": msgs})

