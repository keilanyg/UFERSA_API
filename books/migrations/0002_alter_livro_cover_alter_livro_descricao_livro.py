# Generated by Django 4.2.2 on 2024-08-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='cover',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='livro',
            name='descricao_livro',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição do Livro'),
        ),
    ]
