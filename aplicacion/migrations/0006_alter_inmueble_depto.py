# Generated by Django 4.2.4 on 2023-09-30 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_alter_inmueble_fotos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='depto',
            field=models.CharField(max_length=3),
        ),
    ]