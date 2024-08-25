# Generated by Django 5.1 on 2024-08-25 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name': 'categorias',
                'verbose_name_plural': 'categorias',
                'db_table': 'categorias',
                'ordering': ['name', '-name'],
            },
        ),
        migrations.CreateModel(
            name='prediccion_power',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='powerbi.categorias')),
            ],
        ),
    ]
