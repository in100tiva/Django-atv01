from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'author', 'publication_date', 'isbn' )
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titulo do Livro'}),
            'author': forms.TextInput(attrs={'placeholder': 'Nome do Autor'}),
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'isbn': forms.TextInput(attrs={'placeholder': 'ISBN'}),
        }