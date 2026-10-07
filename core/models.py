from django.db import models


class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    PRIORIDADES = [
        ("BAIXA", "Baixa"),
        ("MEDIA", "Média"),
        ("ALTA", "Alta"),
    ]

    titulo = models.CharField(max_length=200)
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADES,
        default="MEDIA"
    )
    concluido = models.BooleanField(default=False)
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )

    def __str__(self):
        return self.titulo