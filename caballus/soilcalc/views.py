from os import walk
from django.http import request, HttpResponse 
from django.shortcuts import render
from soilcalc.services import ph_calculations
from soilcalc.services import factor_correction
from .models import sampleSoil


# Create your views here.


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
