# Generated by Django 4.1.5 on 2023-02-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("showroom", "0004_alter_showroomdetail_cug_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="showroomdetail",
            name="Address",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]