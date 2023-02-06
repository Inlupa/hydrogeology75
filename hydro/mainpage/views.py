from django.shortcuts import render

def homepage(request):
    return render(request,'mainpage/mainpage.html')
def faculty(request):
    return render(request,'mainpage/faculty.html')

def about_conference(request):
    return render(request,'mainpage/about_conference.html')

def contacts(request):
    return render(request,'mainpage/contacts.html')