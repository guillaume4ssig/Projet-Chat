from django.shortcuts import render, redirect
from .models import Message
from django.http import HttpResponse
from django.template import Template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Salon

@login_required
def message(request,salon_id):
    salon = Salon.objects.get(id=salon_id)
    if request.method == 'POST':

        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.salon = salon
            msg.save()
            return redirect('salon_messages',salon_id=salon_id)
    else:
        form = MessageForm()

    msgs = salon.messages.order_by('date')
    return render(request, "messages/message.html", {
        "salon":salon,
        "msgs": msgs,
        "form": form
    })


def create_salon(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Salon.objects.create(name=name)
        return redirect("salon_list")

    return render(request, "salons/create_salon.html")

@login_required
def salon_list(request):
    salons = Salon.objects.all()
    return render(request, "salons/salon_list.html", {"salons": salons})