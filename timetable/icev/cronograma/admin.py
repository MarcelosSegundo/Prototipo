from django.contrib import admin
from .models import Professor, Materia, Sala, Turma, Horario

admin.site.register(Professor)
admin.site.register(Materia)
admin.site.register(Sala)
admin.site.register(Turma)
admin.site.register(Horario)
