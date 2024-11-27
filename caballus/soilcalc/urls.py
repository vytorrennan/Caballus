from django.urls import path
from . import views

urlpatterns = [
    path("calc/", views.view_sample, name="view sample")
]
