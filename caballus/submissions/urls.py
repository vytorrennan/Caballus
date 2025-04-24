from django.urls import path
from . import views

urlpatterns = [
    path("", views.Submit.as_view(), name="Submit"),
]
