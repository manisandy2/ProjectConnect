# Generated by Django 4.1.5 on 2023-02-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Asset", "0003_alter_brandlocation_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statusmanagement",
            name="VisibilityList",
            field=models.BooleanField(
                choices=[("Assets", "Assets"), ("Vendor", "Vendor")], max_length=120
            ),
        ),
    ]