from django.db import models
from UserApp.models import Cliente


class Pedido(models.Model):
    cantidad = models.IntegerField()
    precio_total = models.IntegerField()
    cliente_rut = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    categoria_producto = models.CharField(max_length=255)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre


# Armar relacion n-m entre Productos y Pedidos

class Productos_con_pedidos(models.Model):
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)


class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=255)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_servicio


class Reserva(models.Model):
    nombre_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()


class Resena(models.Model):
    rut_cliente = models.IntegerField()
    fecha_resena = models.DateTimeField(auto_now=True)
    resena = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
