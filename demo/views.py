from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data = {'message': 'Hello World'}
    return HttpResponse(data)

