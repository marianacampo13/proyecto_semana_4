from django.contrib import admin
from .models import aprendiz, programa, instructores, competencias

# Register your models here.

admin.site.register(aprendiz)
admin.site.register(programa)
admin.site.register(instructores)
admin.site.register(competencias)
