
from django.urls import path
from BellezaApp.views import index, pedido, resena, reserva, reservaView, pedidoView, resenaView, reservando

urlpatterns = [
    path('', index, name="index"),
    path('resena/', resenaView, name="resenaView"),
    path('pedido/', pedidoView, name="pedidoView"),
    path('reserva/', reservaView, name="reservaView"),
    path('reservando/', reservando, name='reservando')

]
