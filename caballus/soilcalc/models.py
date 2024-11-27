from contextlib import nullcontext
from django.db import models

class sampleSoil(models.Model):
    sample = models.AutoField(primary_key =True)
    ph = models.FloatField(blank=True, null=True)
    organicMaterial = models.FloatField(blank=True, null=True)
    phosporo = models.FloatField(blank=True, null=True)
    potassium = models.FloatField(blank=True, null=True)
    na = models.FloatField(blank=True, null=True)
    ca = models.FloatField(blank=True, null=True)
    mg = models.FloatField(blank=True, null=True)
    al = models.FloatField(blank=True, null=True)
    hAl = models.FloatField(blank=True, null=True)
    cu = models.FloatField(blank=True, null=True)
    fe = models.FloatField(blank=True, null=True)
    mn = models.FloatField(blank=True, null=True)
    zn = models.FloatField(blank=True, null=True)
    pRem = models.FloatField(blank=True, null=True)
    emptyBecker1 = models.FloatField(blank=True, null=True)
    emptyBecker2 = models.FloatField(blank=True, null=True)
    claySilt = models.FloatField(blank=True, null=True)
    clay = models.FloatField(blank=True, null=True)

class standardCurves(models.Model):
    curveName = models.CharField()
    stage1 = models.FloatField(blank=True, null=True)
    stage2 = models.FloatField(blank=True, null=True)
    stage3 = models.FloatField(blank=True, null=True)
    stage4 = models.FloatField(blank=True, null=True)
    stage5 = models.FloatField(blank=True, null=True)
    stage6 = models.FloatField(blank=True, null=True)







