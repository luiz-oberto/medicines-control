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


# Entrada ou saída de medicamentos
def registrar_evento(request):
    if request.method == 'POST':
        form = EventsLogForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
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
        form = EventsLogForm()

    return render(request, 'home/registrar_evento.html', {'form': form})


# visualizar quantidade de medicamentos
def visualizar_medicamentos(request):
    medicines = Medicine.objects.order_by('name')
    context = {
        'medicines': medicines
    }
    return render(request, 'home/quantidade_medicamentos.html', context)


# Formulário para registrar novos medicamentos
def registrar_medicamento(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicamento_novo = form.save(commit=False)

            medicamento_novo.save()
            messages.success(request, 'Medicamento registrado com sucesso.')
            return redirect('registrar_medicamento')
    else:
        form = MedicineForm()

    return render(request, 'home/registrar_medicamento.html', {'form': form})