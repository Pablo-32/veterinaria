from django.contrib import admin
from .models import Producto
from .models import Turno

admin.site.register(Producto)

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_mascota', 'animal', 'edad_mascota', 'tipo', 'fecha', 'hora', 'contacto')
    list_filter = ('tipo', 'fecha')
    search_fields = ('nombre', 'contacto')