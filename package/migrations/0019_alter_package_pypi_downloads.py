# Generated by Django 4.1.3 on 2022-11-30 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("package", "0018_alter_packageexample_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="package",
            name="pypi_downloads",
            field=models.IntegerField(default=0, verbose_name="PyPI downloads"),
        ),
    ]
