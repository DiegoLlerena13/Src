# Generated by Django 4.2.3 on 2024-07-14 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Municipio', '0016_alter_pagotributario_pagtricat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagotributario',
            name='PagTriCat',
            field=models.CharField(db_column='PagTriCat', default=' ', max_length=1, null=True, verbose_name='Categoria'),
        ),
    ]
