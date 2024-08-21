from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet, GenericViewSet


from .models import *
from .serializers import *


class CategoriaViewSet(ModelViewSet):
    
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ('nome_categoria',)
    http_method_names = ['get', 'head', 'options']
    
class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    search_fields = ('nome_editora',)
    http_method_names = ['get', 'head', 'options']
    
class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    search_fields = ('nome_autor',)
    http_method_names = ['get', 'head', 'options']
    
class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    search_fields = ('nome_livro',)
    http_method_names = ['get', 'head', 'options']