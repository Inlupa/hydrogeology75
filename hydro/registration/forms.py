from django import forms
from .models import Article


class InsertAtricleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['fio', 'article_name', 'abstract', 'thesis',]
        widgets = {
            'fio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ФИО'}),
            'article_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            'abstract': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Абстракт'}),
            'thesis': forms.Textarea(attrs={'class': 'form-control ', 'type': 'text', 'placeholder': 'Тезисы'}),
        }
        labels = {
            'fio': 'ФИО',
            'article_name': 'Название статьи:',
            'abstract': 'Абстракт',
            'thesis': 'Текст статьи',
        }
