# Generated by Django 4.2.3 on 2024-07-14 18:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Municipio', '0009_alter_vivienda_vivcal_alter_vivienda_vivcodpos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='CasCodBlo',
            field=models.CharField(db_column='CasCodBlo', default=' ', max_length=2, null=True, validators=[django.core.validators.MaxLengthValidator(2)], verbose_name='Código de Bloque'),
        ),
        migrations.AlterField(
            model_name='casa',
            name='CasEsc',
            field=models.CharField(blank=True, db_column='CasEsc', default=' ', max_length=2, null=True, validators=[django.core.validators.MaxLengthValidator(2), django.core.validators.RegexValidator('^[0-9]*$', 'Ingrese solo números válidos.')], verbose_name='Escalera'),
        ),
        migrations.AlterField(
            model_name='casa',
            name='CasNumPue',
            field=models.CharField(blank=True, db_column='CasNumPue', default=' ', max_length=2, null=True, validators=[django.core.validators.MaxLengthValidator(2), django.core.validators.RegexValidator('^[0-9]*$', 'Ingrese solo números válidos.')], verbose_name='Número de Puerta'),
        ),
        migrations.AlterField(
            model_name='casa',
            name='CasPla',
            field=models.CharField(blank=True, db_column='CasPla', default=' ', max_length=2, null=True, validators=[django.core.validators.MaxLengthValidator(2), django.core.validators.RegexValidator('^[0-9]*$', 'Ingrese solo números válidos.')], verbose_name='Planta'),
        ),
    ]
