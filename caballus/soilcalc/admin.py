from django.contrib import admin
from .models import (sampleSoil, standardCurves)
# Register your models here.
#
#para que eu veja esta informações na pagina de admin
class SampleSoilAdmin(admin.ModelAdmin):
    list_display = ('sample', 'ph', 'organicMaterial', 'phosporo', 'potassium')



admin.site.register(sampleSoil, SampleSoilAdmin)
admin.site.register(standardCurves)
