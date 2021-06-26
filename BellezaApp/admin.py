from django.contrib import admin
from BellezaApp.models import Pedido, Producto, Productos_con_pedidos, Reserva, Servicio, Resena


admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Productos_con_pedidos)
admin.site.register(Reserva)
admin.site.register(Resena)
admin.site.register(Servicio)

