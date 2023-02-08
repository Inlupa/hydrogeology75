from django.shortcuts import render
from .forms import InsertAtricleForm, AccommodationForm, UploadFileForm

def registration(request):
    form_article = InsertAtricleForm(request.POST)
    form_file = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form_article.is_valid() and form_file.is_valid():
            form_article.save()
            form_article = InsertAtricleForm()
            doc_to_save = request.FILES['file']
            filename = doc_to_save._get_name()
            with open('media/'+str(filename), 'wb+') as f:
                for chunk in doc_to_save.chunks():
                    f.write(chunk)
    return render(request, "registration/registration.html",
                  context={'form': form_article, 'form_file':form_file })

def accommodation(request):
    form_acc = AccommodationForm(request.POST)
    if request.method == 'POST':
        if form_acc.is_valid():
            form_acc.save()
            form_acc = AccommodationForm()
    return render(request, "registration/accommodation.html",
                  context={'form': form_acc})













