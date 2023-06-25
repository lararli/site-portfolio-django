# Generated by Django 4.2.2 on 2023-06-24 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("image", models.ImageField(upload_to="")),
                ("name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("bio", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="URLs",
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
                ("name", models.CharField(max_length=100)),
                ("url", models.URLField()),
                ("image", models.ImageField(upload_to="icons")),
            ],
        ),
    ]