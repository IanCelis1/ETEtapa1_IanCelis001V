# Generated by Django 3.2.3 on 2021-07-05 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ground_Zero', '0003_rename_pais_proveedor_pais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='contrasenaproveedor',
            field=models.CharField(max_length=12, verbose_name='contraseña'),
        ),
    ]
