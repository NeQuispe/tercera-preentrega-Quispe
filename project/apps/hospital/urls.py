from django.urls import path
from .views import *

urlpatterns = [
    path("hospital/", index, name="index"),
    path("crear_paciente/", crear_paciente, name="crear_paciente"),
    path("crear_medico/", crear_medico, name="crear_medico"),
    path("crear_turno/", crear_turno, name="crear_turno"),
    path("crear_receta/", crear_receta, name="crear_receta"),
]

