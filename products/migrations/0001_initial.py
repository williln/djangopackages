# Generated by Django 4.1.4 on 2023-01-04 13:42

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Title")),
                ("slug", models.SlugField(verbose_name="slug")),
                ("active", models.BooleanField(default=True, verbose_name="Active")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Release",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "cycle",
                    models.CharField(max_length=50, verbose_name="Release Cycle"),
                ),
                (
                    "cycle_short_hand",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Shorthand name",
                    ),
                ),
                (
                    "codename",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Code name"
                    ),
                ),
                (
                    "release",
                    models.DateField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Release Date",
                    ),
                ),
                (
                    "eol",
                    models.DateField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="End of Life Date",
                    ),
                ),
                (
                    "latest",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Latest release",
                    ),
                ),
                (
                    "link",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Link to changelog",
                    ),
                ),
                (
                    "lts",
                    models.BooleanField(
                        default=False, max_length=50, verbose_name="Long-term-support"
                    ),
                ),
                (
                    "support",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Has active support",
                    ),
                ),
                (
                    "discontinued",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Discontinued",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
