import requests
from django.core.management.base import BaseCommand
from books.models import Livro, Categoria, Editora, Autor

class Command(BaseCommand):
    help = 'Load books from JSON server and save to database'

    def handle(self, *args, **kwargs):
        url = 'http://localhost:3000/livros'
        response = requests.get(url)
        livros = response.json()

        for livro_data in livros:
            categoria, _ = Categoria.objects.get_or_create(id=livro_data['categoria'])
            editora, _ = Editora.objects.get_or_create(id=livro_data['editora'])
            autor, _ = Autor.objects.get_or_create(id=livro_data['autor'])

            livro, created = Livro.objects.get_or_create(
                id=livro_data['id'],
                defaults={
                    'nome_livro': livro_data['nome_livro'],
                    'descricao_livro': livro_data['descricao_livro'],
                    'data_cadastro': livro_data['data_cadastro'],
                    'data_lancamento': livro_data['data_lancamento'],
                    'quantidade': livro_data['quantidade'],
                    'categoria': categoria,
                    'editora': editora,
                    'autor': autor,
                    'instituicao': livro_data['instituicao'],
                    'cover': livro_data['cover']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Livro "{livro.nome_livro}" criado com sucesso'))
            else:
                self.stdout.write(self.style.WARNING(f'Livro "{livro.nome_livro}" já existe'))
