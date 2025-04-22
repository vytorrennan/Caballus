from django.contrib import admin

from dataimport.models import AnalysisFile, Sample, Element

# Register your models here.

admin.site.register(AnalysisFile)
admin.site.register(Element)
admin.site.register(Sample)
