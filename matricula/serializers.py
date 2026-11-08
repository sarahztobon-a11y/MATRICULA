# Importa "serializers" de Django REST Framework (DRF), una herramienta que
# se instala aparte y sirve para crear APIs: páginas que entregan y reciben
# datos en formato JSON (el formato que usan las apps y páginas web modernas
# para intercambiar información).
from rest_framework import serializers

# Importa los modelos (tablas) que creaste en models.py.
from .models import Estudiante, Curso

# Un SERIALIZER es un "traductor":
#   - Convierte los datos de la base de datos (objetos de Python) a JSON
#     para enviarlos al usuario.
#   - Convierte el JSON que llega del usuario en datos que se pueden
#     guardar en la base de datos (y revisa que sean válidos).
# ModelSerializer es una versión que se arma casi sola a partir de un modelo.
class CursoSerializer(serializers.ModelSerializer):

    # La clase "Meta" guarda la CONFIGURACIÓN del serializer.
    class Meta:
        # Indica de qué modelo (tabla) se van a traducir los datos.
        model = Curso

        # Lista de columnas que se incluirán en el JSON.
        # Un curso se verá así: {"id": 1, "nom_curso": "Matemáticas", "amnio": 2026}
        fields = ['id', 'nom_curso', 'amnio']


# Serializer para la tabla Estudiante.
class EstudianteSerializer(serializers.ModelSerializer):

    # Campo EXTRA que no existe en la tabla, pero que se calcula al momento
    # de mostrar los datos. Sirve para ver los NOMBRES de los cursos del
    # estudiante, y no solo sus números de id.
    #   - source='cursos': toma los datos del campo "cursos" del modelo.
    #   - many=True: porque un estudiante puede tener varios cursos.
    #   - read_only=True: es solo de LECTURA; sirve para mostrar, pero no
    #     se puede usar para enviar ni guardar datos.
    # StringRelatedField usa el método __str__ del modelo Curso
    # (el que devuelve nom_curso), por eso muestra el nombre del curso.
    curso_nombres = serializers.StringRelatedField(source='cursos', many=True, read_only=True)

    # Configuración del serializer.
    class Meta:
        # Modelo (tabla) del que se toman los datos.
        model = Estudiante

        # Campos que aparecerán en el JSON:
        #   - id, nombre, apellido: columnas normales de la tabla.
        #   - cursos: lista con los IDs de los cursos (sirve para ASIGNAR
        #     cursos al crear o editar un estudiante).
        #   - curso_nombres: el campo extra de arriba, con los nombres
        #     (sirve solo para VER).
        fields = ['id', 'nombre', 'apellido', 'cursos', 'curso_nombres']