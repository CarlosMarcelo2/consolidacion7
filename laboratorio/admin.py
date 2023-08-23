from django.contrib import admin

# Register your models here.
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    
admin.site.register (Laboratorio, LaboratorioAdmin)

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    ordering = ('nombre', )

admin.site.register (DirectorGeneral, DirectorGeneralAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'get_year_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('laboratorio', 'f_fabricacion')
    
    ordering = ('nombre', 'laboratorio')
    
    list_display_links = ('nombre', 'laboratorio')

    list_filter = ('nombre', 'laboratorio')

    def get_year_fabricacion(self, obj):
        return obj.f_fabricacion.year
    get_year_fabricacion.short_description = 'F Fabricacion'

admin.site.register (Producto, ProductoAdmin)




