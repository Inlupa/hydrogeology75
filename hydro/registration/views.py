from django.shortcuts import render
from .forms import InsertAtricleForm
from .models import Article


def registration(request):
    form_article = InsertAtricleForm(request.POST)
    if request.method == 'POST':
        if form_article.is_valid():
            form_article.save()
    return render(request, "registration/registration.html",
                  context={'form': form_article})