from os import walk
from django.http import request, HttpResponse
from django.shortcuts import render
from soilcalc.services import ph_calculations
from soilcalc.services import factor_correction
from .models import sampleSoil

# Create your views here.


def view_sample(request):
    sample = None
    sample_id = None
    ph = None
    if request.method == 'POST':
        sample_id = request.POST.get('sample_id')
        if sample_id:
            try:

                sample = sampleSoil.objects.get(sample=sample_id)
                ph = ph_calculations.calculate_soil_ph(sample.ca, sample.mg)
                sample = sample.__dict__ #transforma o objeto em um dicionario
                sample.pop(next(iter(sample)))

            except: 
                sample = None

    context = {
        'sample_id': sample_id,
        'sample': sample,
        'ph': ph
    }

    return render(request, "soilcalc/index.html", context)


def view_factor(request):
    name_factor = ""
    witness = 7
    reference = 5
    if request.method == 'POST':
      name_factor = request.POST.get("name_factor")
      witness = request.POST.get('witness')
      reference = request.POST.get("value_reference")
    
    result_factor = factor_correction.calculate_factor(witness,reference)
   
    return HttpResponse(f"Result: {result_factor}")
