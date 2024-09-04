from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50, verbose_name="Categoria")

    def __str__(self):
        return self.nome_categoria

class Editora(models.Model):
    nome_editora = models.CharField(max_length=250, verbose_name="Editora")

    def __str__(self):
        return self.nome_editora

class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nome_autor = models.CharField(max_length=250, verbose_name="Autor")

    def __str__(self):
        return self.nome_autor

class Livro(models.Model):
    nome_livro = models.CharField(max_length=100, verbose_name="Nome do Livro")
    data_cadastro = models.DateField(auto_now_add=True, verbose_name="Data de Cadastro")
    data_lancamento = models.DateField(verbose_name="Data de Lançamento")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    descricao_livro = models.TextField(verbose_name="Descrição do Livro", blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name="Editora")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor")
    instituicao = models.CharField(max_length=100, verbose_name="Instituição", default="IFRN")
    cover = models.URLField(max_length=200)
    
    def __str__(self):
        return self.nome_livro
