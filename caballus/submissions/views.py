from django.views import View
from django.shortcuts import render, redirect


class Submit(View):
    def get(self, request):
        return render(request, 'submissions.html')

    def post(self, request):
        return render(request, 'submissions.html')
