# Generated by Django 5.0.1 on 2024-01-30 06:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_remove_blogpost_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]