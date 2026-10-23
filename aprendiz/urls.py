from django.urls import path 
from .views import lista_aprendices

urlpatterns = [
    path('', lista_aprendices, name ='lista')
]