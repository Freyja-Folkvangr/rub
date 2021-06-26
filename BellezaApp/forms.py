from django import forms
from BellezaApp.models import Servicio, Reserva


# crear clases (formularios) para reseña, pedidos y reserva de hora. Estilo nativo de python

class resena(forms.Form):
    username = forms.CharField(label='Nombre Usuario')
    resena = forms.CharField(label='Danos tu opinión')


class pedido(forms.Form):
    username = forms.CharField(label='Nombre Usuario')
    password = forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput)


# SERVICIOS = [(servicio.id, servicio.nombre_servicio) for servicio in Servicio.objects.all()]


class reserva(forms.Form):
    servicio = forms.ChoiceField(choices=[])
    fecha_hora = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', }))

class crea_reserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'servicio', 'fecha_hora']
