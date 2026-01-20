from django.shortcuts import render, redirect
from .models import Message, Salon
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from django.shortcuts import get_object_or_404


@login_required
def message(request, salon_id):
    salon = Salon.objects.get(id=salon_id)
    if request.method == 'POST':

        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.salon = salon
            msg.save()
            return redirect('salon_messages', salon_id=salon_id)
    else:
        form = MessageForm()

    msgs = salon.messages.order_by('date')
    return render(request, "messages/message.html", {
        "salon": salon,
        "msgs": msgs,
        "form": form
    })

@login_required
def get_messages_json(request, salon_id):
    """Renvoie tous les messages d’un salon en JSON pour le chat live"""
    salon = Salon.objects.get(id=salon_id)
    messages = salon.messages.order_by('date')
    data = [
        {
            'sender': msg.sender.username,
            'content': msg.content,
            'date': msg.date.strftime("%Y-%m-%d %H:%M")
        }
        for msg in messages
    ]
    return JsonResponse({'messages': data})


@login_required
def create_salon(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Salon.objects.create(name=name,admin=request.user)
        return redirect("salon_list")

    return render(request, "salons/create_salon.html")

@login_required
def delete_salon(request, salon_id):
    salon = get_object_or_404(Salon, id=salon_id)

    if request.method == "POST":
        if salon.admin != request.user:
            return redirect('salon_messages',salon_id=salon_id)
        salon.delete()
        return redirect("salon_list")

    return redirect("salon_list")


@login_required
def salon_list(request):
    salons = Salon.objects.all()
    return render(request, "salons/salon_list.html", {"salons": salons})


