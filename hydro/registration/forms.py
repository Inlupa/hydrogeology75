from django import forms
from .models import Article, Accommodation, type_of_report_choices


class InsertAtricleForm(forms.ModelForm):
    type_of_report = forms.ChoiceField(choices= type_of_report_choices)
    class Meta:
        model = Article
        fields = ['fio', 'article_name', 'abstract', 'type_of_report', 'organisation',]
        widgets = {
            'fio': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'ФИО'}),
            'article_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            'abstract': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Абстракт'}),
            'type_of_report': forms.Select(attrs={'class': 'input_offer', 'style':'width:100%;', 'placeholder': 'Тип доклада'}),
            'organisation': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Организация'}),
        }

        labels = {
                    'fio': 'ФИО',
                    'article_name': 'Название статьи:',
                    'abstract': 'Абстракт',
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
