import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers


from demo.models import Demo
def index(request):
    data = {'message': 'Hello World'}
    # return HttpResponse(data)
    return JsonResponse(data)

def testing(request):
    data = {"message":"This is a test Route."}
    return JsonResponse(data)

def addDemo(request):
    name = "Demo: "+str(random.randint(1,101))
    d = Demo(name=name, description="This is a testing "+name)
    d.save()
    response = {"message": "Demo create Successfully"}
    return JsonResponse(response)

def getDemo(request):
    demos = Demo.objects.all()
    return render(request, 'demo/index.html', {
        "demos": demos
    })

def deleteDemos(request):
    demos = Demo.objects.all().delete()
    response = {"message": "Demo deleted Successfully"}
    return JsonResponse(response)
