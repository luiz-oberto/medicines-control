from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EventsLog, Medicine
from .forms import EventsLogForm, MedicineForm


# Página inicial - Log de eventos
def index(request):
    eventos = EventsLog.objects.order_by('-timestamp')

    context = {
        'eventos': eventos,
    }

    return render(request, 'home/index.html', context)


# Entrada ou saída de medicamentos e registrar novos medicamentos
def registrar_evento(request):
    if request.method == 'POST':
        if 'submit_medicine' in request.POST:
            form_register = MedicineForm(request.POST)
            form_events = EventsLogForm()

            if form_register.is_valid():
                form_register.save()
                messages.success(request, 'Medicamento adicionado com sucesso.')
                return redirect('registrar_evento')
            
        else:
            form_events = EventsLogForm(request.POST)
            form_register = MedicineForm()
            if form_events.is_valid():
                evento = form_events.save(commit=False)
                medicamento = evento.medicine

                if evento.event_type == EventsLog.ENTRY:
                    medicamento.quantity += evento.quantity
                elif evento.event_type == EventsLog.EXIT:
                    if evento.quantity > medicamento.quantity:
                        messages.error(request, 'Quantidade insuficiente no estoque.')
                        return redirect('registrar_evento')
                    medicamento.quantity -= evento.quantity

                medicamento.save()
                evento.save()
                messages.success(request, 'Evento registrado com sucesso.')
                return redirect('registrar_evento')
        
    else:
        form_events = EventsLogForm()
        form_register = MedicineForm()

    return render(request, 'home/registrar_evento.html', {'form_events': form_events, 'form_register': form_register})


# visualizar quantidade de medicamentos
def visualizar_medicamentos(request):
    medicines = Medicine.objects.order_by('name')
    context = {
        'medicines': medicines
    }
    return render(request, 'home/quantidade_medicamentos.html', context)
