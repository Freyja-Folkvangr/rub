# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=255)
    telefono= models.IntegerField()
    email= models.EmailField(max_length=255)
    deseo_promociones= models.BooleanField()


    def __str__ (self):
            return self.user.username


