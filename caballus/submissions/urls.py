from django.urls import path
from . import views

urlpatterns = [
    path("/submit", views.Submit.as_view(), name="submit"),
]
