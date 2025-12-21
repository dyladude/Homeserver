from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Django on 10.0.0.50")

