from django import forms
from .models import *
from django.utils.timezone import now

class InsertAtricleForm(forms.ModelForm):
    class Meta:
        model = RegistrationArticle
        fields = ['reg_id', 'fio', 'article_name', 'abstract', 'thesis',]
        widgets = {
            'reg_id': forms.TextInput(attrs={'class': 'form-control input_form', 'placeholder':'ID записи'}),
            'fio': forms.TextInput(attrs={'class': 'form-control  input_form', 'placeholder':'ФИО'}),
            'article_name': forms.TextInput(attrs={'class': 'form-control  input_form', 'placeholder': 'Название статьи'}),
            'abstract': forms.TextInput(attrs={'class': 'form-control  input_form', 'placeholder': 'Абстракт'}),
            'thesis': forms.Textarea(attrs={'class': 'form-control  input_form_content', 'type': 'text', 'placeholder': 'Тезисы'}),

        }
        labels = {
            'reg_id': 'ID статьи',
            'fio': 'ФИО',
            'article_name': 'Название статьи:',
            'abstract': 'Абстракт',
            'thesis': 'Текст статьи',
        }
