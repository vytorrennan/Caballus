from django.shortcuts import render, get_object_or_404, redirect

from .forms import UploadFileForm
from .models import AnalysisFile
from .services.parser import parse_data


def index(request):
    all_analyses = AnalysisFile.objects.all()
    data = {'analysis_files': all_analyses}
    return render(request, "dataimport/index.html", data)


def view(request, id):
    analysis = get_object_or_404(AnalysisFile, id=id)
    return render(request, "dataimport/view.html", {'analysis': analysis})


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            content = uploaded_file.read().decode('latin-1')

            parse_data(content)

            return redirect('index')