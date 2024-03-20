from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Develop a Top Products HTTP Microservice ")