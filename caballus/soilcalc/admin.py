from django.contrib import admin
from django.contrib.auth.models import User
from .models import (batch , sampleSoil, element, standardCurves)
from soilcalc import models

# Register your models here.
#
#


admin.site.register(batch)
admin.site.register(sampleSoil)
admin.site.register(element)
admin.site.register(standardCurves)
