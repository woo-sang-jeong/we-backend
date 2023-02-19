# Generated by Django 4.1.7 on 2023-02-19 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(default="", max_length=20)),
                ("description", models.TextField()),
                ("p_like", models.PositiveIntegerField(default="0", null=True)),
                ("p_dislike", models.PositiveIntegerField(default="0", null=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="posts",
                        to="categories.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
