# Generated by Django 5.0.1 on 2024-03-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupe1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('adress', models.CharField(max_length=100, verbose_name='Suroga')),
                ('num_phone', models.IntegerField(verbose_name='Raqami trelfon')),
                ('birth_day', models.DateField(verbose_name='Soli taw')),
                ('nation', models.CharField(max_length=100, verbose_name='Millat')),
            ],
            options={
                'verbose_name': 'Груп1',
                'verbose_name_plural': 'Групы1',
            },
        ),
    ]