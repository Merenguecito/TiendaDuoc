from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField
# Create your models here.
class Marca(models.Model):
    nombre  = models.TextField(max_length=30)
    activo  = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre          = models.TextField()
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre          = models.TextField()
    modelo          = models.TextField(null=True)
    descripcion     = models.TextField(max_length=256)
    stock           = models.IntegerField(default=0)
    marca           = models.ForeignKey(Marca, on_delete=models.CASCADE,null=None, default=None)
    precio_venta    = models.IntegerField(default=0)
    precio_compra   = models.IntegerField(null=None, default=None)
    categoria       = models.ForeignKey(Categoria, on_delete=CASCADE, null=None, default=None)
    img_producto    = models.ImageField(null=True, blank=True, upload_to="gallery")

    def __str__(self):
        return self.nombre

'''class Region(models.Model):
    id_region       = models.IntegerField(primary_key=True)
    nombre_region   = models.TextField()

    def __str__(self):
        return self.nombre_region

class Comuna(models.Model):
    id_comuna       = models.IntegerField(primary_key=True)
    nombre_comuna   = models.TextField()
    region          = models.ForeignKey(Region, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.nombre_comuna'''

class Cliente(models.Model):
    rut             = models.IntegerField()
    nombre          = models.TextField(max_length=30)
    apellido        = models.TextField(max_length=30)
    region          = models.TextField()
    comuna          = models.TextField()
    direccion       = models.TextField(max_length=100)
    fecha_nac       = models.DateField()
    telefono        = models.TextField()
    email           = models.EmailField()
    contrasena      = models.TextField()

    def __str__(self):
        return self.nombre