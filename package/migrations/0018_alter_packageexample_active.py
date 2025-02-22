# Generated by Django 4.1.2 on 2022-11-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("package", "0017_flaggedpackage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="packageexample",
            name="active",
            field=models.BooleanField(
                default=None,
                help_text="Moderators have to approve links before they are provided",
                null=True,
                verbose_name="Active",
            ),
        ),
    ]
