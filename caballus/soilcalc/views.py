from os import walk
from django.http import request, HttpResponse
from django.shortcuts import render
from soilcalc.services import ph_calculations
from soilcalc.services import factor_correction
from django.db import connection
from .models import sampleSoil, batch

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


def search(request):
    option = None
    table = None
    if request.method == 'POST':
        option = request.POST.get('search_table')
    
    # if not option.isidentifier():
    #    return JsonResponse({'error': 'Nome de tabela inválido'}, status=400)
    
    if option == "batch":
        batches = batch.objects.all()
        
        table = [batch.id for batch in batches]


    context = {
        'option': option,
        'table': table,

    }
    return render(request, "soilcalc/index.html", context)


