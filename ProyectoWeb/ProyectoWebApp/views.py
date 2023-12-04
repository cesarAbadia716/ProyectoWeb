from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    try:
        # Aquí podrías agregar lógica adicional según tus necesidades
        return render(request, 'ProyectoWebApp/home.html')
    except Exception as e:
        return HttpResponse(f"Error en la vista home: {e}")

def servicios(request):
    try:
        # Lógica adicional para la vista de servicios
        return render(request, 'ProyectoWebApp/servicios.html')
    except Exception as e:
        return HttpResponse(f"Error en la vista servicios: {e}")

def tienda(request):
    try:
        # Lógica adicional para la vista de la tienda
        return render(request, 'ProyectoWebApp/tienda.html')
    except Exception as e:
        return HttpResponse(f"Error en la vista tienda: {e}")

def blog(request):
    try:
        # Lógica adicional para la vista del blog
        return render(request, 'ProyectoWebApp/blog.html')
    except Exception as e:
        return HttpResponse(f"Error en la vista blog: {e}")

def contacto(request):
    try:
        # Lógica adicional para la vista de contacto
        return render(request, 'ProyectoWebApp/contacto.html')
    except Exception as e:
        return HttpResponse(f"Error en la vista contacto: {e}")
