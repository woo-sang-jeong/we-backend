# Generated by Django 4.1.7 on 2023-03-06 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_initial"),
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="post",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="categories",
                to="posts.post",
            ),
        ),
    ]