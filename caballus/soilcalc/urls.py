from django.urls import path
from . import views

urlpatterns = [
    path("calc/", views.view_factor, name="view sample")
]
