from typing import ContextManager
from django.http import request
from django.shortcuts import redirect, render
#from Tienda.models import Categoria, Cliente, Marca, Region, Comuna, Producto
from Tienda.models import Categoria, Cliente, Marca, Producto
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password #Encriptar
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def sucursalAjaxResponse(request):
    if request.method == 'POST':
        mensaje=""
       
        if 'btnGrabar' in request.POST:
            nombre          = request.POST["txtNombre"]
            modelo          = request.POST["txtModelo"]
            descripcion     = request.POST["txtDescripcion"]
            stock           = int(request.POST["txtStock"])
            id_marca        = request.POST["txtMarca"]
            marca           = Marca.objects.get(pk=id_marca)
            precio_venta    = request.POST["txtPrecioVenta"]
            precio_compra   = request.POST["txtPrecioCompra"]
            id_categoria    = request.POST["txtCategoria"]
            categoria       = Categoria.objects.get(pk=id_categoria)
            img_producto    = request.POST["img_producto"]
            ruta_img        = "gallery/"+img_producto
            Producto.objects.create(nombre=nombre, modelo=modelo, descripcion=descripcion, stock=stock, marca=marca, precio_venta=precio_venta, precio_compra=precio_compra, categoria=categoria, img_producto=ruta_img)
        
            try:
                if producto != None:     
                    mensaje = "La solicitud fue realizada con éxito"
                #item.save()
            except:
                return JsonResponse({'mensaje' : 'El producto no fue encontrado'})
            return JsonResponse({'mensaje' : 'La operación fue exitosa'})

        elif 'btnBuscar' in request.POST:
            try:
                id_producto = request.POST['txtBuscaCodigo']
                producto= Producto.objects.get(pk = id_producto)
                producto= model_to_dict(producto)
                return JsonResponse(producto, safe=False)
            except:
                mensaje="nono"
                return JsonResponse(mensaje,safe=False)

        elif 'btnListar' in request.POST:
            lista= Producto.objects.all().values()
            return JsonResponse(list(lista), safe=False)
            #lista = Producto.objects.filter(id__contains = id).values()
                    

    #Vista Eliminar
        elif 'btnEliminar' in request.POST:
            id_producto = request.POST["txtBuscaCodigo"]
            producto= Producto.objects.get(pk = id_producto)
            if producto!=None:
                Producto.objects.delete()
                mensaje="Registro eliminado"
                return JsonResponse(producto, safe=False)



@csrf_exempt
def sucursalAjax(request):
	return render(request, 'sucursal_ajax.html', {})
	
def ajaxTestResponse(request):
	contexto = {'mensaje' : 'Hola Mundo con Ajax!!!'}
	return JsonResponse(contexto)

def sucursalApiFetch(request):
	return render(request, 'sucursalApiFetch.html', {})


























def tienda(request):
    lista_productos = []
    lista_carrito   = []
    lista_productos = Producto.objects.all()

    if request.method == 'POST':
        if "btnAgregaProducto" in request.POST:
            id_producto     = request.POST["txtId"]
            producto        = Producto.objects.get(pk=id_producto)
            lista_carrito.append(producto)
        elif "btnEliminarProducto" in request.POST:
            id_producto     = request.POST["txtIdCarrito"]
            producto        = Producto.objects.get(pk=id_producto)
            
            lista_carrito.remove(producto)

        
    context = {'lista_productos': lista_productos, 'lista_carrito':lista_carrito}
    return render(request, 'Tienda.html', context)
    
"""def login(request):
    return render(request, 'registration/Login.html', {})"""

def carrito(request):
    return render(request, 'carrito.html', {})

def registroUsuarios(request):   
    mensaje = ""
    lista_regiones   = []
   # lista_regiones   = Region.objects.all()
    
    lista_comunas   = []
    #lista_comunas   = Comuna.objects.all()
    if request.method == 'POST':
        rut         = request.POST["txtRun"]
        nombre      = request.POST["txtNombre"]
        apellido    = request.POST["txtApellido"]
        fecha_nac   = request.POST["txtFecha_nac"]
        direccion   = request.POST["txtDireccion"]
        region   = request.POST["cmbRegion"]
        comuna   = request.POST["cmbComuna"]
       # region      = Region.objects.get(pk=id_region)
       # comuna      = Comuna.objects.get(pk=id_comuna)
        email       = request.POST["txtEmail"]
        telefono    = request.POST["txtTelefono"]
        contrasena  = request.POST["pwdCliente"]
        #validaContrasena  = request.POST["pwdClienteConfirma"]

        if "btnRegistro" in request.POST:
            User.objects.create(username=nombre, email=email, password=make_password(contrasena))
            Cliente.objects.create(rut=rut, nombre=nombre, apellido=apellido, region=region, comuna=comuna, direccion=direccion, fecha_nac=fecha_nac,telefono=telefono, email=email)
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    context = {'mensaje':mensaje, 'lista_regiones': lista_regiones, 'lista_comunas': lista_comunas}
    return render(request, 'registroUsuarios.html', context)

def admin_productos(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

   
    return render(request, 'admin_productos.html', {})


def test(request):
    return render(request, 'test.html', {})

def producto(request):
    id_producto=2
    producto = Producto.objects.get(pk=id_producto)
    context={'producto':producto}
    return render(request, 'Producto.html',context)







"""def sucursalAjaxResponse(request):
        
    if 'btnGrabar' in request.POST:
        id          = request.POST['txtId']
        nombre      = request.POST['txtNombre']
        direccion   = request.POST['txtDireccion']
        telefono    = request.POST['txtTelefono']
        encargado   = request.POST['txtEncargado']
        
        P = Producto.objects
        if id < 1:
            P.create(nombre=nombre, direccion=direccion, telefono=telefono, encargado=encargado)
        else:
            try:
                item            = P.get(pk = id)
                item.nombre     = nombre
                item.direccion  = direccion
                item.telefono   = telefono
                item.encargado  = encargado
                item.save()
            except:
                return JsonResponse({'mensaje' : 'El Id no fue encontrado'})
            return JsonResponse({'mensaje' : 'La operación fue exitosa'})
    elif 'btnListar' in request.POST:
            #lista = Producto.objects.filter(nombre__contains = nombre).values()
            lista= Producto.objects.all().values()
            P = Producto.objects

            return JsonResponse(list(lista), safe=False)
    else:
            id = request.POST['txtId']
            try:
                    item = Producto.objects.get(pk = id)
                    item = model_to_dict(item)
                    return JsonResponse(item, safe=False)
            except:
                    return JsonResponse({})"""