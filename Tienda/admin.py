from django.contrib import admin
from .models import Marca, Cliente, Producto, Categoria
from django.utils.html import format_html

# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
    list_display        = ['nombre', 'activo']
    list_display_links  = ['nombre', 'activo']
    list_filter         = ['nombre']
    search_fields       = ['nombre']
admin.site.register(Marca, MarcaAdmin)

'''class RegionAdmin(admin.ModelAdmin):
    list_display        = ['nombre_region']
admin.site.register(Region, RegionAdmin)

class ComunaAdmin(admin.ModelAdmin):
    list_display        = ['nombre_comuna', 'region']
admin.site.register(Comuna, ComunaAdmin)'''

class ClienteAdmin(admin.ModelAdmin):
    list_display        = ['rut', 'nombre', 'apellido', 'region', 'comuna', 'direccion', 'fecha_nac', 'telefono', 'email', 'contrasena']
admin.site.register(Cliente, ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):

    list_display        = ['id','nombre', 'marca', 'modelo', 'categoria','descripcion','stock','marca','precio_venta', 'precio_compra','img_producto']
    list_display_links  = ['nombre', 'marca', 'modelo']
    list_filter         = ['nombre','categoria', 'marca', 'modelo']
    search_fields       = ['nombre', 'marca', 'modelo']
admin.site.register(Producto, ProductoAdmin)

class CategoriaAdmin(admin.ModelAdmin):

    list_display        = ['nombre']
admin.site.register(Categoria, CategoriaAdmin)

    