from django.views import View
from django.shortcuts import render, redirect
from .forms import  SubmissionSampleForm

class Submit(View):
    def get(self, request):
        form = SubmissionSampleForm()
        return render(request, 'submissions.html', {'form': form})

    def post(self, request):
        form = SubmissionSampleForm(request.POST)
        if form.is_valid():
            produto = form.save()
            return redirect('submit')
        return render(request, 'submissions.html', {'form': form})
