from django.shortcuts import render, redirect, get_object_or_404
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


def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)

    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)

        if form.is_valid():
            form.save()
            return redirect("listar_eventos")
    else:
        form = EventoForm(instance=evento)

    return render(
        request,
        "core/editar_evento.html",
        {"form": form, "evento": evento}
    )


def excluir_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)

    if request.method == "POST":
        evento.delete()
        return redirect("listar_eventos")

    return render(
        request,
        "core/excluir_evento.html",
        {"evento": evento}
    )