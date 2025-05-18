from django import forms
from .models import EventsLog, Medicine


class EventsLogForm(forms.ModelForm):
    EVENT_CHOICES = [
        ('EN', 'Entrada'),
        ('SA', 'Saída'),
    ]

    event_type = forms.ChoiceField(
        choices=EVENT_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True,
    )
    class Meta:
        model = EventsLog
        fields = ['medicine', 'event_type', 'quantity'] # 'responsible' -> para quando tivermos usuários envolvidos
        widgets = {
            'medicine': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name']
        