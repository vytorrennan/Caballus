from django.contrib import admin

from dataimport.models import AnalysisFile, Sample, Element

# Register your models here.

admin.register(AnalysisFile)
admin.register(Element)
admin.register(Sample)
