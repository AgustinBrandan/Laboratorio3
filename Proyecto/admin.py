from django.contrib import admin
from .models import Libro
from .models import LibroDigital

# Register your models here.

admin.site.register(Libro)
admin.site.register(LibroDigital)

