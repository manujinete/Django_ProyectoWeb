from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return HttpResponse("Home") #texto que nos responde.

def servicios(request):
    
    return HttpResponse("Servicios")

def tienda(request):
    
    return HttpResponse("Tienda")

def blog(request):
    
    return HttpResponse("Blog")

def contactos(request):
    
    return HttpResponse("Contactos")
