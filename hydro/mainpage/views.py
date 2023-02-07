from django.shortcuts import render
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse

def homepage(request):
    return render(request,'mainpage/mainpage.html')
def faculty(request):
    return render(request,'mainpage/faculty.html')

def about_conference(request):
    return render(request,'mainpage/about_conference.html')

def contacts(request):
    return render(request,'mainpage/contacts.html')

def download_theses(requests):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'thesis_download.docx'
    # Define the full file path
    filepath = BASE_DIR + '/static/doc/' + filename
    # Open the file for reading content
    path = open(filepath, 'br')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response