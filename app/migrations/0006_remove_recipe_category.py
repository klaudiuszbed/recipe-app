# Generated by Django 4.1 on 2022-08-23 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_recipe_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
    ]