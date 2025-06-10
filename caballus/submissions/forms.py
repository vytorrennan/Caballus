from django import forms
from .models import SubmissionSample


class SubmissionSampleForm(forms.ModelForm):
    class Meta:
        model = SubmissionSample
        fields = [
            # checkbox + quantidade
            "agua_fisico_quimica", "num_agua_fisico_quimica",
            "agua_microbiologico", "num_agua_microbiologico",
            "solo_fertilidade_basica", "num_solo_fertilidade_basica",
            "solo_fertilidade_completa", "num_solo_fertilidade_completa",
            "tecido_vegetal", "num_tecido_vegetal",
            # observação
            "content",
        ]
        widgets = {
            # --- checkboxes --------------------------------------------------
            "agua_fisico_quimica":       forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "agua_microbiologico":       forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "solo_fertilidade_basica":   forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "solo_fertilidade_completa": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "tecido_vegetal":            forms.CheckboxInput(attrs={"class": "form-check-input"}),

            # --- números compactos (máx. 3 dígitos) -------------------------
            "num_agua_fisico_quimica":       forms.NumberInput(attrs={"class": "qty-input form-control form-control-sm", "min": 1}),
            "num_agua_microbiologico":       forms.NumberInput(attrs={"class": "qty-input form-control form-control-sm", "min": 1}),
            "num_solo_fertilidade_basica":   forms.NumberInput(attrs={"class": "qty-input form-control form-control-sm", "min": 1}),
            "num_solo_fertilidade_completa": forms.NumberInput(attrs={"class": "qty-input form-control form-control-sm", "min": 1}),
            "num_tecido_vegetal":            forms.NumberInput(attrs={"class": "qty-input form-control form-control-sm", "min": 1}),

            # --- textarea ----------------------------------------------------
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Descreva a amostra…",
            }),
        }
