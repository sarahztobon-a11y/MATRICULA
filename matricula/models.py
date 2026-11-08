from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Curso(models.Model):
    nom_curso = models.CharField(max_length=150)
    amnio = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )

    def __str__(self):
        return self.nom_curso

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso, related_name='estudiantes', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"