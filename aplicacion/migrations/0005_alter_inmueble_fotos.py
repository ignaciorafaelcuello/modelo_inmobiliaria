# Generated by Django 4.2.4 on 2023-09-30 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_alter_contacto_options_inmueble_fotos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='fotos',
            field=models.ImageField(upload_to='inmuebles'),
        ),
    ]
