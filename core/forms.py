from django import forms
from .models import Evento, Tarefa


class EventoForm(forms.ModelForm):
    data = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=forms.DateInput(
            format="%d/%m/%Y",
            attrs={
                "placeholder": "DD/MM/AAAA"
            }
        )
    )

    class Meta:
        model = Evento
        fields = ["nome", "descricao", "data"]

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ["titulo", "prioridade", "concluido", "evento"]