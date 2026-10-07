from django.contrib import admin
from .models import Evento, Tarefa


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ("nome", "data")


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "prioridade", "concluido", "evento")
    list_filter = ("prioridade", "concluido", "evento")