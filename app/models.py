from django.db import models
from django.utils import timezone

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class EventsLog(models.Model):
    ENTRY = 'EN'
    EXIT = 'SA'
    EVENT_TYPES = [
        (ENTRY, 'Entrada'),
        (EXIT, 'Saída'),
    ]

    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=2, choices=EVENT_TYPES)
    quantity = models.PositiveIntegerField()  # Sempre positivo, o tipo define o sentido
    timestamp = models.DateTimeField(default=timezone.now)
    # responsible = models.CharField(max_length=100)  # Ou um ForeignKey para User se tiver login

    def __str__(self):
        return f"{self.get_event_type_display()} de {self.quantity} {self.medicine.name} em {self.timestamp.strftime('%d/%m/%Y %H:%M')}" # type: ignore
