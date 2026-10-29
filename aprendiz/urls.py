from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_aprendices, name='lista'),
    path('aprendices/registrar/', views.registrar_aprendiz, name='registrar_aprendiz'),
    path('aprendices/editar/<str:documento>/', views.editar_aprendiz, name='editar_aprendiz'),
    path('programas/registrar/', views.registrar_programa, name='registrar_programa'),
    path('instructores/registrar/', views.registrar_instructor, name='registrar_instructor'),
    path('competencias/registrar/', views.registrar_competencia, name='registrar_competencia'),
    path('aprendices/eliminar/<str:documento>/', views.eliminar_aprendiz, name='eliminar_aprendiz'),
]

