from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Hello World!')

def soma(request, a, b):
    return HttpResponse(f'{a} + {b} = {a+b}')

def subtracao(request, a, b):
    return HttpResponse(f'{a} - {b} = {a-b}')

def multiplicacao(request, a, b):
    return HttpResponse(f'{a} * {b} = {a*b}')

def divisao(request, a, b):
    return HttpResponse(f'{a} / {b} = {a/b}')