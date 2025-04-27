from django.contrib import admin
from django.contrib.auth.models import User
from .models import (batch, sampleSoil, element, standardCurves)

# Register your models here.
#
#


admin.site.register(batch)
admin.site.register(sampleSoil)
admin.site.register(element)


# para que eu veja esta informações na pagina de admin
# Ex: class SampleSoilAdmin(admin.ModelAdmin):
# list_display = ('sample', 'ph', 'organicMaterial', 'phosporo', 'potassium')
# admin.site.register(sampleSoil, SampleSoilAdmin)
