from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    #return HttpResponse("Home") #texto que nos responde.
    return render(request, "ProyectoWebApp/home.html")
    
def servicios(request):
    
    #return HttpResponse("Servicios")
    return render(request, "ProyectoWebApp/servicios.html")

def tienda(request):
    
    #return HttpResponse("Tienda")
    return render(request, "ProyectoWebApp/tienda.html")

def blog(request):
    
    #return HttpResponse("Blog")
    return render(request, "ProyectoWebApp/blog.html")

def contactos(request):
    
    #return HttpResponse("Contactos")
    return render(request, "ProyectoWebApp/contacto.html")