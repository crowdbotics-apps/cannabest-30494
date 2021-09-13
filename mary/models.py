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
        blank=True,
        max_length=256,
    )
    also_found_in = models.CharField(
        blank=True,
        max_length=256,
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


class Strain(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    aliases = models.CharField(
        max_length=512,
    )
    description = models.TextField()
    effects = models.ManyToManyField(
        "mary.Effect",
        related_name="strain_effects",
    )
    aromas = models.ManyToManyField(
        "mary.Aroma",
        related_name="strain_aromas",
    )
    terpenes = models.ManyToManyField(
        "mary.Terpene",
        related_name="strain_terpenes",
    )


# Create your models here.
