from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def how_to_use(request):
    return render(request, 'how_to_use.html')

def how_to_cite(request):
    return render(request, 'how_to_cite.html')