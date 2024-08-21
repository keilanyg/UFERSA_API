from rest_framework import serializers
from .models import Categoria, Editora, Autor, Livro

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    autor_obj = serializers.SerializerMethodField()
    editora_obj = serializers.SerializerMethodField()
    categoria_obj = serializers.SerializerMethodField()

    class Meta:
        model = Livro
        fields = ['id', 'nome_livro', 'data_cadastro', 'data_lancamento', 'quantidade', 'descricao_livro', 'categoria', 'editora', 'autor', 'autor_obj', 'cover', 'editora_obj', 'categoria_obj']

    def get_autor_obj(self, instance):
        autor = Autor.objects.get(id=instance.autor.id)
        serializer = AutorSerializer(autor)
        return serializer.data

    def get_editora_obj(self, instance):
        editora = Editora.objects.get(id=instance.editora.id)
        serializer = EditoraSerializer(editora)
        return serializer.data

    def get_categoria_obj(self, instance):
        categoria = Categoria.objects.get(id=instance.categoria.id)
        serializer = CategoriaSerializer(categoria)
        return serializer.data
