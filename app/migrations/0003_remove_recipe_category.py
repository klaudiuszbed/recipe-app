# Generated by Django 4.1 on 2022-08-22 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_recipe_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
    ]