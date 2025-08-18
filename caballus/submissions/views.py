# views.py
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from .forms import SubmissionSampleForm
from .models import SubmissionSample


class Submit(View):
    def get(self, request):
        form = SubmissionSampleForm()
        return render(request, 'submissions.html', {'form': form})

    def post(self, request):
        form = SubmissionSampleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if request.user.is_authenticated:
                obj.user = request.user  # vincula quem enviou
            obj.save()
            messages.success(request, "Submissão registrada com sucesso!")
            return redirect('submit')
        # quando inválido, re-renderiza com erros
        return render(request, 'submissions.html', {'form': form})


@method_decorator(staff_member_required, name="dispatch")
class Admin(View):
    def get(self, request):
        # Filtro por status via querystring (?status=all|pending|accepted|rejected)
        status_param = request.GET.get("status", "all")
        qs = SubmissionSample.objects.select_related("user").order_by("-created_at")

        if status_param == "accepted":
            qs = qs.filter(status=True)
        elif status_param == "rejected":
            qs = qs.filter(status=False)
        elif status_param == "pending":
            qs = qs.filter(status__isnull=True)
        # else: "all" (sem filtro)

        context = {
            "submissions": qs,
            "status_param": status_param,  # para marcar option selecionada no template
        }
        return render(request, "admin.html", context)


# ===== AÇÕES =====

def _redirect_back(request, fallback_name="admin_page"):
    """
    Volta para a página anterior preservando o filtro da querystring.
    """
    ref = request.META.get("HTTP_REFERER")
    return redirect(ref or fallback_name)


@staff_member_required
@require_POST
def submission_accept(request, pk):
    s = get_object_or_404(SubmissionSample, pk=pk)
    s.status = True
    s.save(update_fields=["status"])
    messages.success(request, f"Submissão #{s.pk} marcada como ACEITA.")
    return _redirect_back(request)


@staff_member_required
@require_POST
def submission_reject(request, pk):
    s = get_object_or_404(SubmissionSample, pk=pk)
    s.status = False
    s.save(update_fields=["status"])
    messages.warning(request, f"Submissão #{s.pk} marcada como RECUSADA.")
    return _redirect_back(request)


@staff_member_required
@require_POST
def submission_reset(request, pk):
    """
    Opcional: volta a submissão para PENDENTE (status = NULL).
    """
    s = get_object_or_404(SubmissionSample, pk=pk)
    s.status = None
    s.save(update_fields=["status"])
    messages.info(request, f"Submissão #{s.pk} voltou para PENDENTE.")
    return _redirect_back(request)
