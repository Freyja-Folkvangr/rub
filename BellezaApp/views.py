from django.shortcuts import render
from BellezaApp.models import Pedido, Producto, Productos_con_pedidos, Reserva, Resena, Servicio
from BellezaApp.forms import resena, pedido, reserva


# Create your views here.

def index(request):
    # Productos y/o servicio (como reserva de hora)
    return render(request, 'BellezaApp/index.html')


def resenaView(request):
    context = {'form': resena}
    return render(request, 'BellezaApp/resena.html', context)


def reservaView(request):
    context = {'form': reserva}
    return render(request, 'BellezaApp/reserva.html', context)


def reservando(request):
    cliente = request.user.cliente
    servicio = request.POST['servicio']
    fecha_hora = request.POST['fecha_hora']

    reserva = Reserva(cliente=cliente, servicio=Reserva.objects.get(id=int(servicio)), fecha_hora=fecha_hora)

    reserva.save()
    return index(request)


def pedidoView(request):
    context = {'form': pedido}
    return render(request, 'BellezaApp/pedido.html', context)


def resenacreate(request):
    texto = request.POST['comentario']


def pedidoscreate(request):
    listapedidos = Pedido.objects.filter(cliente=request.user.cliente)

    context = {"pedidos": listapedidos}
    return render(request, 'BellezaApp/pedido.html', context)
