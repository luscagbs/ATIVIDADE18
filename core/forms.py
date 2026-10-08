from django import forms
from .models import Evento


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