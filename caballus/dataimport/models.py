from django.db import models
from django.utils import timezone

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Sample(TimeStampedModel):
    label = models.CharField(max_length=255)
    concentration = models.CharField(max_length=10)
    rsd_percentage = models.CharField(max_length=10)
    mean_abs = models.CharField(max_length=10)

    def __str__(self):
        return self.label


class Element(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class AnalysisFile(TimeStampedModel):
    filename = models.CharField(max_length=255)
    calibration_mode = models.CharField(max_length=255)

    analysis_date = models.DateField()

    elements = models.ManyToManyField(Element, related_name="analysis_files")
    samples = models.ManyToManyField(Sample, related_name="analysis_files")

    def __str__(self):
        return self.filename
