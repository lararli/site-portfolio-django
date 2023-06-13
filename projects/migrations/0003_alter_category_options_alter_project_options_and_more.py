# Generated by Django 4.2.2 on 2023-06-13 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_rename_projects_project"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="project",
            options={"verbose_name_plural": "Projects"},
        ),
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(blank=True, upload_to="images"),
        ),
    ]