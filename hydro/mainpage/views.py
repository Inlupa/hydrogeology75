from django.shortcuts import render

def homepage(request):
    return render(request,'mainpage/mainpage.html')
def faculty(request):
    return render(request,'mainpage/faculty.html')
