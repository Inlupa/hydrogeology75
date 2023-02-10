from django.shortcuts import render

from django.core.mail import send_mail, EmailMessage
from .forms import InsertAtricleForm, AccommodationForm, UploadFileForm




def registration(request):
    form_article = InsertAtricleForm(request.POST)
    form_file = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form_article.is_valid() and form_file.is_valid():

            fio = form_article.cleaned_data['fio']
            org = form_article.cleaned_data['organisation']
            name = form_article.cleaned_data['article_name']
            abst = form_article.cleaned_data['abstract']
            type_of_report = form_article.cleaned_data['type_of_report']

            doc_to_save = request.FILES.get('file', "No_file")
            if type_of_report != "Без доклада":
                text_mail =  "Организация участника: "+ org + ". Тип доклада: " +  type_of_report + ". Название доклада: " + name + ". Абстракт: " + abst + "."
                email = EmailMessage(
                    "Заявка на участие от " + fio,
                    text_mail,
                    'anton199823@gmail.com',
                    ['msu.inlupa@gmail.com', 'msu_hydro70@mail.ru'])
                email.attach(doc_to_save.name, doc_to_save.read(), doc_to_save.content_type)
                email.send()
            else:
                text_mail =  "Организация " + org +"."
                email = EmailMessage(
                    "Заявка на участие от " + fio,
                    text_mail,
                    'anton199823@gmail.com',
                    ['msu.inlupa@gmail.com','msu_hydro70@mail.ru'])
                email.send()

            form_article.save()
            form_article = InsertAtricleForm()

            if doc_to_save != "No_file":

                filename = doc_to_save._get_name()
                with open('media/'+str(filename), 'wb+') as f:
                        for chunk in doc_to_save.chunks():
                            f.write(chunk)

    return render(request, "registration/registration.html",
                      context={'form': form_article, 'form_file':form_file})

def accommodation(request):
    form_acc = AccommodationForm(request.POST)
    if request.method == 'POST':
        if form_acc.is_valid():

            # тут надо переписать для отправки на проживание, но это не сейчас, а завтра


            # reg_fio = form_acc.cleaned_data['fio']
            # org = form_acc.cleaned_data['organisation']
            # name = form_acc.cleaned_data['article_name']
            # abst = form_acc.cleaned_data['abstract']
            # type_of_report = form_acc.cleaned_data['type_of_report']
            #
            # text_mail = "Организация участника: " + org + ". Тип доклада: " + type_of_report + ". Название доклада: " + name + ". Абстракт: " + abst + "."
            # email = EmailMessage(
            #         "Заявка на участие от " + fio,
            #         text_mail,
            #         'anton199823@gmail.com',
            #         ['msu.inlupa@gmail.com', 'msu_hydro70@mail.ru'])
            # email.send()


            form_acc.save()
            form_acc = AccommodationForm()
    return render(request, "registration/accommodation.html",
                  context={'form': form_acc})













