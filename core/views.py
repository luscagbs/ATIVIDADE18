from django.shortcuts import render, redirect
from .forms import EventoForm
from .models import Evento


def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, "core/listar_eventos.html", {"eventos": eventos})


def criar_evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("listar_eventos")
    else:
        form = EventoForm()

    return render(request, "core/criar_evento.html", {"form": form})