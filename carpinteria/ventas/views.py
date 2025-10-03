from django.shortcuts import render
from django.http import HttpResponse

def ventas(request):
    return HttpResponse ("Esta es la pagina de ventas ")
