# Generated by Django 4.1.7 on 2023-02-19 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("posts", "0001_initial"),
        ("medias", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="photo",
            name="post",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="posts.post",
            ),
        ),
    ]
