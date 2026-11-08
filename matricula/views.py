from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Estudiante, Curso
from .serializers import EstudianteSerializer, CursoSerializer

def resumen(request):
    total_estudiantes = Estudiante.objects.count()
    total_cursos = Curso.objects.count()
    return HttpResponse(f"Actualmente hay {total_estudiantes} estudiantes y {total_cursos} cursos registrados en matrícula.")

# ViewSets automáticos para CRUD completo (igual al ejemplo del profesor)
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('nom_curso')
    serializer_class = CursoSerializer

# APIView manual de control total (GET y POST)
class CursoAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)