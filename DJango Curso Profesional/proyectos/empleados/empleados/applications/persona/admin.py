from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)

# Que los datos de Empleado se vean como una tabla
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'firt_name',
        'last_name',
        'departamento',
        'job',
    )
    # Filtro buscador (horizontal)
    search_fields = ('firt_name', )
    # Filtro vertical
    list_filter = ('job',)
    # Fitro horizontal, pasar una opción a otro lado
    filter_horizontal = ('habilidades',)
    
admin.site.register(Empleado, EmpleadoAdmin)


