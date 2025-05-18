from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = 'name', 'quantity'


@admin.register(models.EventsLog)
class EventsLogAdmin(admin.ModelAdmin):
    list_display = 'medicine', 'event_type', 'quantity', 'timestamp'