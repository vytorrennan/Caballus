from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class SubmissionSample(models.Model):
    created_at = models.DateTimeField(default=now)

    # ------------- Água -------------------------------------------------
    agua_fisico_quimica = models.BooleanField(
        default=False,
        verbose_name="Água – Físico-Química"
    )
    num_agua_fisico_quimica = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        null=True, blank=True,
        verbose_name="Qtde amostras"
    )

    agua_microbiologico = models.BooleanField(
        default=False,
        verbose_name="Água – Microbiológico"
    )
    num_agua_microbiologico = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        null=True, blank=True
    )

    # ------------- Solo -------------------------------------------------
    solo_fertilidade_basica = models.BooleanField(
        default=False,
        verbose_name="Solo – Fertilidade Básica"
    )
    num_solo_fertilidade_basica = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        null=True, blank=True
    )

    solo_fertilidade_completa = models.BooleanField(
        default=False,
        verbose_name="Solo – Fertilidade Completa"
    )
    num_solo_fertilidade_completa = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        null=True, blank=True
    )

    # ------------- Tecido Vegetal ---------------------------------------
    tecido_vegetal = models.BooleanField(
        default=False,
        verbose_name="Tecido Vegetal"
    )
    num_tecido_vegetal = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        null=True, blank=True
    )

    # ----------- Outros campos ------------------------------------------
    content = models.CharField(max_length=150)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    status = models.BooleanField(
        null=True,
        default=None,
        verbose_name="status"
    )

    def __str__(self):
        return ( f"Submissão #{self.pk} – "
            f"Água Físico-Química: {self.agua_fisico_quimica} ({self.num_agua_fisico_quimica}), "
            f"Água Microbiológico: {self.agua_microbiologico} ({self.num_agua_microbiologico}), "
            f"Solo Fertilidade Básica: {self.solo_fertilidade_basica} ({self.num_solo_fertilidade_basica}), "
            f"Solo Fertilidade Completa: {self.solo_fertilidade_completa} ({self.num_solo_fertilidade_completa}), "
            f"Tecido Vegetal: {self.tecido_vegetal} ({self.num_tecido_vegetal}), " )