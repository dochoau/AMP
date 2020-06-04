from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # Puedo añadirle los campos que quiera
    nombre_empresa = models.CharField(max_length=40, null=True, blank=True)
    nit_empresa = models.IntegerField(null=True, blank=True)
    tel_contacto = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
