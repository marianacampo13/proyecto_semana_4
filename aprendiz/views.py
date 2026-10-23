from django.shortcuts import render

# Create your views here.
from .models import aprendiz

def lista_aprendices(request):

    aprendices = aprendiz.objects.all()

    contexto = {
        "aprendices":aprendices
    }
    return render(request, 'aprendiz/index.html', contexto)
