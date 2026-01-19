from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Dylan's test page from Django on 10.0.0.50")

