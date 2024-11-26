from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rcb(request):
    return HttpResponse('<h1>virat is captain of rcb<h1>')
