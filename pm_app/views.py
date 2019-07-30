from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def how_to_use(request):
    return render(request, 'how_to_use.html')

def how_to_cite(request):
    return render(request, 'how_to_cite.html')

def About(request):
    return render(request, 'About.html')
def Summary(request):
    return render(request, 'Summary.html')
def Useful(request):
    return render(request, 'Useful.html')
def Online(request):
    return render(request, 'Online.html')
def Tools(request):
    return render(request, 'Tools.html')
def Contact(request):
    return render(request, 'Contact.html')
def Events(request):
    return render(request, 'Events.html')
def Announcement(request):
    return render(request, 'Announcement.html')
def FeedBack(request):
    return render(request, 'FeedBack.html')
def FAQS(request):
    return render(request, 'FAQS.html')
