from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Empresta(models.Model):

    titulo = models.CharField(max_length=50)
    termina_em = models.DateTimeField(default=timezone.now())

    @property
    def passou(self):
        if timezone.now() > self.termina_em:
            print('terminou')
            return True
        print('nao terminou')
        return False
