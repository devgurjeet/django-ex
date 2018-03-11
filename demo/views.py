from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request):
    data = {'message': 'Hello World'}
    # return HttpResponse(data)
    return JsonResponse(data)

