from django.conf import settings
from django.db import models


class Benefit(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )


class Terpene(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
        blank=True,
    )
    also_found_in = models.CharField(
        max_length=256,
        blank=True,
    )
    aromas = models.ManyToManyField(
        "mary.Aroma",
        blank=True,
        related_name="terpene_aromas",
    )
    benefits = models.ManyToManyField(
        "mary.Benefit",
        blank=True,
        related_name="terpene_benefits",
    )
    effects = models.ManyToManyField(
        "mary.Effect",
        blank=True,
        related_name="terpene_effects",
    )


class Effect(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )


class Aroma(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )


# Create your models here.
