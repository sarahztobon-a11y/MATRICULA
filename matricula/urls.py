from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('estudiantes', views.EstudianteViewSet, basename='estudiante')
router.register('cursos', views.CursoViewSet, basename='curso') 

urlpatterns = [
    path('resumen/', views.resumen, name='resumen_matricula'),
    path('cursos-api/', views.CursoAPIView.as_view(), name='cursos_api'),
    path('', include(router.urls)),
]