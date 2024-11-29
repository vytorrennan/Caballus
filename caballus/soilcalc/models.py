from typing import DefaultDict
from django.db import models
from django.contrib.auth.models import User 
from django.utils.timezone import now

class batch(models.Model):
    id = models.IntegerField(primary_key=True, default=None) # Nome do lote ex : 317-340 


class sampleSoil(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    created_at = models.DateField(default=now)

    batch_id = models.ForeignKey(
        batch,
        on_delete= models.CASCADE,
        default = None,
        null=True,  # Permitir valores nulos, se necessário
        blank=True,
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE, #atributo só para teste remover depois
        default = None,
        null=True,  # Permitir valores nulos, se necessário
        blank=True,
    )

class element(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=20)
    value = models.FloatField(blank=True, null=True)

    sampleSoil_id = models.ForeignKey(
        sampleSoil, 
        on_delete = models.CASCADE, # remover 
        default = None,
        blank = True,
        null = True
    )

class standardCurves(models.Model):
    curve_element = models.CharField(primary_key=True, default=None)
    value = models.FloatField(blank=True, null=True)
    bath_id = models.ForeignKey(
        batch,
        on_delete = models.CASCADE,
        default = None,
        blank = True, 
        null =True 
    )
    
