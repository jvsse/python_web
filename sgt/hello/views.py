from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello world!")

def richarlison(request):
	return HttpResponse("Hello Richarlison!")

def paqueta(request):
	return HttpResponse("Hello Paquetá!")
