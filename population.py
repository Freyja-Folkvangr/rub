# Escriba aquÃ­ el poblamiento de la base de datos, tal como vimos en la Auxiliar 8

from UserApp.models import Cliente
from BellezaApp.models import Pedido
from BellezaApp.models import Producto
from BellezaApp.models import Reserva
from BellezaApp.models import Resena
from BellezaApp.models import Servicio

ser1= Servicio(nombre_servicio='Máscara de Oro', precio ='100000', descripcion ='Elimina arrugas y manchas con nuestro kit de oro que incluye Láminas de oro de 24 kilates, polvo de diamante y agua termal de los Alpes, Pirineos y Anatolia. (Precio por sesión)')
ser2= Servicio(nombre_servicio='Permanente Pestañas mas tinte', precio='23000', descripcion='Permanente Pestañas mas tinte')
ser3= Servicio(nombre_servicio='Masaje Craneal', precio='25000', descripcion='Masajes relajantes en la zona del cráneo permiten eliminar la tensión y el estrés, que muchas veces derivan en migrañas y dolores de cabeza.')
ser4= Servicio(nombre_servicio='Drenaje Post Operatorio 10 Sesiones', precio='350000', descripcion='Drenaje Post Operatorio 10 Sesiones')
ser5= Servicio(nombre_servicio='Botox Capilar', precio='35000', descripcion='El botox capilar es un tratamiento 100% ecológico indicado para la restauración de cabellos dañados, esta compuesto por vitaminas, aminoácidos, proteínas, ácido hialurónico y colágeno.')
ser6= Servicio(nombre_servicio='Keratina Corto', precio='55000', descripcion='Keratina Corto')
ser7= Servicio(nombre_servicio='Depilación Mujer Pierna Completa', precio='14000', descripcion='Depilación Mujer Pierna Completa')
ser8= Servicio(nombre_servicio='Bronceado Dha Cuerpo completo 5 sesiones', precio='98000', descripcion='En solo 5 sesiones, todo tu cuerpo tomará el bronceado que siempre soñaste.')
ser9= Servicio(nombre_servicio='Depilación de Espalda Masculina', precio='15000', descripcion='Logra una piel sin ningún vello y cero riesgo de infección ya que todo es desechable. El sistema de Depilación de Espalda Roll-on para Hombres constituye la alternativa más moderna, grata y eficaz para depilar higiénicamente.')
ser10= Servicio(nombre_servicio='Criolipólisis 1 Sesión 1 Zona 2 Cabezales', precio='300000', descripcion='El tratamiento cooltech permite reducir la grasa subcutánea en zonas determinadas del cuerpo mediante la tecnología de enfriamiento controlado. Para ello, se utiliza un aplicador de vacío ajustable que actúa enfriando el tejido graso de forma selectiva.')

ser1.save()
ser2.save()
ser3.save()
ser4.save()
ser5.save()
ser6.save()
ser7.save()
ser8.save()
ser9.save()
ser10.save()

cli1=Cliente(nombre='Paulina Rojas', telefono='98234710', email='paulina.rojas@gmail.com', deseo_promociones='1')
cli2=Cliente(nombre='Teresa Rivas', telefono='88702451', email='tere_rivas@gmail.com', deseo_promociones='0')
cli3=Cliente(nombre='Andrea Santelices', telefono='75993014', email='andy.santelices@gmail.com', deseo_promociones='1')
cli4=Cliente(nombre='Carlos Cisternas', telefono='91024635', email='charlie_cis@hotmail.com', deseo_promociones='0')
cli5=Cliente(nombre='Pedro Lira', telefono='65390112', email='p.lira@vtr.net', deseo_promociones='1')
cli6=Cliente(nombre='Sandra Lobos', telefono='74480145', email='sandrita.wolf@yahoo.es', deseo_promociones='1')
cli7=Cliente(nombre='Patricia Cabezas', telefono='88056932', email='paty_cabezas@gmail.com', deseo_promociones='0')
cli8=Cliente(nombre='Alfonso Concha', telefono='74901204', email='foncho.concha@gmail.com', deseo_promociones='1')
cli9=Cliente(nombre='Laura Torrealba', telefono='99045574', email='lau_torre@yahoo.es', deseo_promociones='1')
cli10=Cliente(nombre='Catalina Perez', telefono='96401522', email='cataperez@gmail.com', deseo_promociones='0')

cli1.save()
cli2.save()
cli3.save()
cli4.save()
cli5.save()
cli6.save()
cli7.save()
cli8.save()
cli9.save()
cli10.save()

res1=Reserva(nombre_cliente=cli5, servicio=ser9, fecha_hora='2021-07-15 15:30')
res2

res




Crema1 = Producto(nombre ='SELVERT + Pure Vitamin C. Vitalizing Eye Contour Cream', precio ='49000', categoria_producto ='Cremas corporales para mujeres', stock ='100')



Crema1.save()
