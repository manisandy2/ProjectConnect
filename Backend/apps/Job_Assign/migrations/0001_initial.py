# Generated by Django 4.1.5 on 2023-04-01 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Asset", "0011_alter_assetmanagement_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobFor",
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
                ("name", models.CharField(max_length=120)),
                (
                    "status",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="Asset.status",
                    ),
                ),
            ],
        ),
    ]
