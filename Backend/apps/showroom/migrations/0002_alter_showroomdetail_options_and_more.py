# Generated by Django 4.1.5 on 2023-02-23 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="showroomdetail",
            options={"verbose_name_plural": "Show Room Detail"},
        ),
        migrations.AlterModelTable(
            name="showroomdetail",
            table="Show Room Detail",
        ),
    ]
