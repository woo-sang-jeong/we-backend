# Generated by Django 4.1.7 on 2023-02-18 01:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="kind",
        ),
    ]