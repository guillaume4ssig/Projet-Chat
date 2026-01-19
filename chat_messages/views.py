from django.shortcuts import render, redirect
from .models import Message
from django.http import HttpResponse
from django.template import Template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import MessageForm

@login_required
def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('envoie')
    else:
        form = MessageForm()

    msgs = Message.objects.order_by('date')
    return render(request, "messages/message.html", {
        "msgs": msgs,
        "form": form
    })


