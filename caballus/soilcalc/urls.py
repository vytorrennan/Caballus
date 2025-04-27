from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_sample, name="home "),
    path("calc/", views.view_sample, name="view sample"),
]
