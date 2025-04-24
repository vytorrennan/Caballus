from django.views import View
from django.shortcuts import render, redirect


class Submit(View):
    def get(self, request):
        return render(request, 'index.html')
