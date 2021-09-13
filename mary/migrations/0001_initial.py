# Generated by Django 2.2.24 on 2021-09-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aroma",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Benefit",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Effect",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Terpene",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=256)),
                ("also_found_in", models.CharField(blank=True, max_length=256)),
                (
                    "aromas",
                    models.ManyToManyField(
                        blank=True, related_name="terpene_aromas", to="mary.Aroma"
                    ),
                ),
                (
                    "benefits",
                    models.ManyToManyField(
                        blank=True, related_name="terpene_benefits", to="mary.Benefit"
                    ),
                ),
                (
                    "effects",
                    models.ManyToManyField(
                        blank=True, related_name="terpene_effects", to="mary.Effect"
                    ),
                ),
            ],
        ),
    ]
