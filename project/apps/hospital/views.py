from django.shortcuts import render, redirect
from .models import Paciente, Medico, Turno, Receta
from .forms import PacienteForm, MedicoForm, TurnoForm, RecetaForm

# Mostrar datos guardados en la base de datos
def index(request):
    """ Muestra la lista de pacientes, medicos, turnos y recetas"""
    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()
    turnos = Turno.objects.all()
    recetas = Receta.objects.all()
    datos = {
        'pacientes': pacientes,
        'medicos': medicos,
        'turnos': turnos,
        'recetas': recetas
    }
    
    return render(request, 'hospital/index.html', datos)

# Formularios para crear pacientes, medicos, turnos y recetas
def crear_paciente(request):
    """ Crear un paciente nuevo """
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hospital:index")
    else:
        form = PacienteForm()
    return render(request, 'hospital/crear_paciente.html', {'form': form})

def crear_medico(request):
    """ Crear un medico nuevo """
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hospital:index")
    else:
        form = MedicoForm()
    return render(request, 'hospital/crear_medico.html', {'form': form})

def crear_turno(request):
    """ Crear un turno nuevo """
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hospital:index")
    else:
        form = TurnoForm()
    return render(request, 'hospital/crear_turno.html', {'form': form})

def crear_receta(request):
    """ Crear una receta nueva """
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hospital:index")
    else:
        form = RecetaForm()
    return render(request, 'hospital/crear_receta.html', {'form': form})


