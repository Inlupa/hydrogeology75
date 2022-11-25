from django import forms
from .models import Article, Accommodation


class InsertAtricleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['fio', 'article_name', 'abstract', 'thesis',]
        widgets = {
            'fio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ФИО'}),
            'article_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            'abstract': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Абстракт'}),
            'thesis': forms.Textarea(attrs={'class': 'form-control ', 'type': 'text', 'placeholder': 'Тезисы', 'cols':'200'}),
        }

        labels = {
                    'fio': 'ФИО',
                    'article_name': 'Название статьи:',
                    'abstract': 'Абстракт',
                    'thesis': 'Тезисы',
                }


class UploadFileForm(forms.Form):
    file = forms.FileField()

MONTHS = {
    1:('Январь'), 2:('Февраль'), 3:('Март'), 4:('Апрель'),
    5:('Май'), 6:('Июнь'), 7:('Июль'), 8:('Август'),
    9:('Сентябрь'), 10:('Октябрь'), 11:('Ноябрь'), 12:('Декабрь')
}
class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ['reg_fio', 'pers_num','date_start', 'date_end', 'comments',]
        widgets = {
            'reg_fio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ФИО'}),
            'pers_num': forms.NumberInput(attrs={'class': 'form-control',  'placeholder': 'Кол-во людей'}),
            'date_start': forms.SelectDateWidget(attrs={'class': 'form-control ', 'placeholder': 'Начало проживания'}, months=MONTHS),
            'date_end': forms.SelectDateWidget(attrs={'class': 'form-control ', 'placeholder': 'Конец проживания'}, months=MONTHS),
            'comments': forms.Textarea(attrs={'class': 'form-control ', 'type': 'text', 'placeholder': 'Комментарий', 'cols':'200'}),
        }

        labels = {
            'reg_fio': 'ФИО',
            'pers_num': 'Кол-во людей:',
            'date_start': 'Начало проживания',
            'date_end': 'Конец проживания',
            'comments': 'Комментарии',
        }
