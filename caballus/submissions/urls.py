from django.urls import path
from .views import Submit, Admin, submission_accept, submission_reject, submission_reset

# NÃO defina app_name aqui

urlpatterns = [
    path("submit/", Submit.as_view(), name="submit"),
    path("admin/submissions/", Admin.as_view(), name="admin_page"),
    path("admin/submissions/<int:pk>/accept/", submission_accept, name="submission_accept"),
    path("admin/submissions/<int:pk>/reject/", submission_reject, name="submission_reject"),
    path("admin/submissions/<int:pk>/reset/",  submission_reset,  name="submission_reset"),
]
