# Generated by Django 4.1.5 on 2023-01-30 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ASM",
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
            ],
            options={
                "verbose_name_plural": "ASM",
                "db_table": "ASM",
            },
        ),
        migrations.CreateModel(
            name="Manager",
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
            ],
            options={
                "verbose_name_plural": "Manager",
                "db_table": "Manager",
            },
        ),
        migrations.CreateModel(
            name="Region",
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
            ],
            options={
                "verbose_name_plural": "Region",
                "db_table": "Region",
            },
        ),
        migrations.CreateModel(
            name="RSM",
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
            ],
            options={
                "verbose_name_plural": "RSM",
                "db_table": "RSM",
            },
        ),
        migrations.CreateModel(
            name="State",
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
            ],
            options={
                "verbose_name_plural": "State",
                "db_table": "State",
            },
        ),
        migrations.CreateModel(
            name="StatusManagement",
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
            ],
            options={
                "verbose_name_plural": "Status",
                "db_table": "Status",
            },
        ),
        migrations.CreateModel(
            name="ShowroomDetail",
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
                ("CUG_NO", models.CharField(max_length=120)),
                ("Landline", models.CharField(max_length=120)),
                ("E_Mail", models.CharField(max_length=120)),
                ("Address", models.CharField(max_length=120)),
                (
                    "ASM",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="showroom.asm"
                    ),
                ),
                (
                    "Manager",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="showroom.manager",
                    ),
                ),
                (
                    "RSM",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="showroom.rsm"
                    ),
                ),
                (
                    "Region",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="showroom.region",
                    ),
                ),
                (
                    "State",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="showroom.state"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MaterialManagement",
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
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="showroom.statusmanagement",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Material Type List",
                "db_table": "Material Type List",
            },
        ),
        migrations.CreateModel(
            name="LightTypeList",
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
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="showroom.statusmanagement",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Light Type List",
                "db_table": "Light Type List",
            },
        ),
        migrations.CreateModel(
            name="ImageManagement",
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
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="showroom.statusmanagement",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "360 Degree Image Management",
                "db_table": "360 Degree Image Management",
            },
        ),
        migrations.CreateModel(
            name="Grade",
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
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="showroom.statusmanagement",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Grade",
                "db_table": "Grade",
            },
        ),
        migrations.CreateModel(
            name="ClassManagement",
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
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="showroom.statusmanagement",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Class Management",
                "db_table": "Class Management",
            },
        ),
        migrations.CreateModel(
            name="BrandLocation",
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
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="showroom.statusmanagement",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Brand Type List",
                "db_table": "Brand Type List",
            },
        ),
    ]
