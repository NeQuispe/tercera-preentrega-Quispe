from django import forms
from .models import Paciente, Medico, Turno, Receta

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'