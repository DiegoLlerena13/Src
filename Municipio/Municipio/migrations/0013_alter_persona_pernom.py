# Generated by Django 4.2.3 on 2024-07-14 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Municipio', '0012_alter_casa_casmet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='PerNom',
            field=models.CharField(db_column='PerNom', max_length=20, verbose_name='Nombres'),
        ),
    ]
