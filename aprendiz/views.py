from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import aprendiz

from .forms import (
    AprendizForm,
    ProgramaForm,
    InstructorForm,
    CompetenciaForm
)

def registrar_aprendiz(request):
    if request.method == 'POST':
        form = AprendizForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'El aprendiz fue creado correctamente')
            return redirect('registrar_aprendiz')
    else:
        form = AprendizForm()

    return render(request, 'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': 'Registrar aprendiz'
    })


def registrar_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registrar_programa')
    else:
        form = ProgramaForm()

    return render(request,'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': 'Registrar programa'
    })


def registrar_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registrar_instructor')
    else:
        form = InstructorForm()

    return render(request, 'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': 'Registrar instructor'
    })


def registrar_competencia(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registrar_competencia')
    else:
        form = CompetenciaForm()

    return render(request, 'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': 'Registrar competencia'
    })


def editar_aprendiz(request, documento):
    mi_aprendiz = get_object_or_404(aprendiz, documento=documento)
    if request.method == 'POST':
        form = AprendizForm(request.POST, instance=mi_aprendiz)
        if form.is_valid():
            form.save()
            messages.success(request, 'El aprendiz fue editado de manera correcta')
            return redirect('lista')  # Redirige a tu lista de aprendices
    else:
        form = AprendizForm(instance=mi_aprendiz)

    return render(request, 'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': f'Editar {mi_aprendiz.nombre} {mi_aprendiz.apellido}'
    })
def eliminar_aprendiz(request, documento):
    mi_aprendiz = get_object_or_404(aprendiz, documento=documento)
    
    if request.method == 'POST':
        mi_aprendiz.delete()
        messages.success(request, 'Se eliminó el usuario correctamente')
        return redirect('lista') 
        
    return render(request, 'aprendiz/eliminar.html', {'aprendiz': mi_aprendiz})




def lista_aprendices(request):

    aprendices = aprendiz.objects.all()

    contexto = {
        "aprendices":aprendices
    }
    return render(request, 'aprendiz/index.html', contexto)



