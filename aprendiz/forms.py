
from django import forms
from .models import aprendiz, programa, instructores, competencias


class AprendizForm(forms.ModelForm):
    class Meta:
        model = aprendiz
        fields = [
            'nombre',
            'apellido',
            'tipo_documento',
            'documento',
            'telefono',
            'correo',
            'ficha',
            'programa'
        ]


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = programa
        fields = [
            'nombre',
            'ficha',
            'jornada',
            'duracion',
            'modalidad',
            'nivel_formacion',
            'descripcion'
        ]


class InstructorForm(forms.ModelForm):
    class Meta:
        model = instructores
        fields = [
            'nombre',
            'apellido',
            'especialidad',
            'documento',
            'ficha_asignada',
            'correo',
            'telefono'
        ]


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = competencias
        fields = [
            'nombre',
            'ficha',
            'programa',
            'instructores'
        ]
