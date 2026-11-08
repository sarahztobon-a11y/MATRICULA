from django.contrib import admin
from .models import Estudiante, Curso

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido')
    search_fields = ('nombre', 'apellido')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_curso', 'amnio')
    search_fields = ('nom_curso',)
    list_filter = ('amnio',)