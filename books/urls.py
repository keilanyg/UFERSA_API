from django.urls import path, include
from .viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
app_name = 'books'
router.register("categoria", CategoriaViewSet)
router.register("editora", EditoraViewSet)
router.register("autor", AutorViewSet)
router.register("livro", LivroViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
