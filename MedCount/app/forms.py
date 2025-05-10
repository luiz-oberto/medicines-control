from django import forms
from .models import EventsLog, Medicine


class EventsLogForm(forms.ModelForm):
    class Meta:
        model = EventsLog
        fields = ['medicine', 'event_type', 'quantity'] # 'responsible' -> para quando tivermos usuários envolvidos
        widgets = {
            'event_type': forms.RadioSelect
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name']
        