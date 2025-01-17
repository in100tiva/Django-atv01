from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    author = models.CharField(max_length=100, verbose_name='Autor')
    publication_date = models.DateField(verbose_name='Data de Publicação')
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

