from django.urls import path
from . import views


urlpatterns = [
    path("", views.listar_eventos, name="listar_eventos"),
    path("novo/", views.criar_evento, name="criar_evento"),
    path("editar/<int:pk>/", views.editar_evento, name="editar_evento"),
    path("excluir/<int:pk>/", views.excluir_evento, name="excluir_evento"),
    path("tarefas/", views.listar_tarefas, name="listar_tarefas"),
    path("tarefas/nova/", views.criar_tarefa, name="criar_tarefa"),
    path("tarefas/editar/<int:pk>/", views.editar_tarefa, name="editar_tarefa"),
    path("tarefas/excluir/<int:pk>/", views.excluir_tarefa, name="excluir_tarefa"),
]