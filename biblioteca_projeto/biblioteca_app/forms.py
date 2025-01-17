from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date', 'isbn')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título do livro'}),
            'author': forms.TextInput(attrs={'placeholder': 'Nome do autor'}),
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'isbn': forms.TextInput(attrs={'placeholder': 'ISBN'}),
        }

