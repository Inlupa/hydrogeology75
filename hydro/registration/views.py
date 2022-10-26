from django.shortcuts import render
from .forms import InsertAtricleForm
def registration(request):
    form_article = InsertAtricleForm()
    if request.method == "POST":
        form_article = InsertAtricleForm(request.POST)
        if form_article.is_valid():
            form_article.save()
    return render(request, "registration/registration.html",
                      context={'form_article': form_article})