from django.urls import path
from . import views


urlpatterns = [
    path("", views.listar_eventos, name="listar_eventos"),
    path("novo/", views.criar_evento, name="criar_evento"),
    path("editar/<int:pk>/", views.editar_evento, name="editar_evento"),
    path("excluir/<int:pk>/", views.excluir_evento, name="excluir_evento"),
]