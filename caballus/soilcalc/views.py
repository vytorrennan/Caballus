from os import walk
from django.http import request
from django.shortcuts import render
from soilcalc.services import ph_calculations
from .models import sampleSoil

# Create your views here.


def view_sample(request):
    sample = None
    sample_id = None
    if request.method == 'POST':
        sample_id = request.POST.get('sample_id')
        if sample_id:
            try:
                sample = sampleSoil.objects.get(sample=sample_id)
            except: 
                sample = None
    #ph_calculations(sample.)

    context = {
        'sample_id': sample_id, 
        "sample": sample.__dict__ if sample else None }

    return render(request, "soilcalc/index.html", context)

