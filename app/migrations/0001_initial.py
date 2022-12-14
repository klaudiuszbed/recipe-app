# Generated by Django 4.1 on 2022-08-22 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('requirements', models.TextField(blank=True)),
                ('instruction', models.TextField(blank=True)),
                ('prep_time', models.IntegerField(blank=True)),
                ('price', models.IntegerField(blank=True)),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='app.category')),
            ],
            options={
                'ordering': ['-prep_time'],
            },
        ),
    ]
