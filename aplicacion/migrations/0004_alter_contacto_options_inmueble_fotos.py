# Generated by Django 4.2.4 on 2023-09-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_contacto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacto',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.AddField(
            model_name='inmueble',
            name='fotos',
            field=models.ImageField(null=True, upload_to='inmuebles'),
        ),
    ]
