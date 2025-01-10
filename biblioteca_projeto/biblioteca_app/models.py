from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    author = models.CharField(max_length=100, verbose_name='Autor')
    publication_date = models.CharField(max_length=8, verbose_name='Data de Publicação')
    isbn = models.CharField(max_length=14, unique=True, verbose_name='ISBN')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'