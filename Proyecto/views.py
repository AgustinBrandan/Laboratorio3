from django.http import HttpResponse
from django.shortcuts import render
from Proyecto.models import Libro
from Proyecto.models import LibroDigital
# Create your views here.

def home(request):

    return render(request, "Proyecto/home.html")

def is1(request):
    libros= Libro.objects.all()
    librodigital= LibroDigital.objects.all()
    return render(request, "Proyecto/is1.html", {"libros":libros, "librodigital":librodigital})

def pr(request):
    libros= Libro.objects.all()
    librodigital= LibroDigital.objects.all()
    return render(request, "Proyecto/pr.html", {"libros":libros, "librodigital":librodigital})

def pd(request):
    libros= Libro.objects.all()
    librodigital= LibroDigital.objects.all()
    return render(request, "Proyecto/pd.html", {"libros":libros, "librodigital":librodigital})

def doo(request):
    libros= Libro.objects.all()
    librodigital= LibroDigital.objects.all()
    return render(request, "Proyecto/doo.html", {"libros":libros, "librodigital":librodigital})

def ts(request):
    libros= Libro.objects.all()
    librodigital= LibroDigital.objects.all()
    
    return render(request, "Proyecto/ts.html", {"libros":libros, "librodigital":librodigital})

def sbd(request):
    libros= Libro.objects.all()
    librodigital= LibroDigital.objects.all()
    return render(request, "Proyecto/sbd.html", {"libros":libros, "librodigital":librodigital})



