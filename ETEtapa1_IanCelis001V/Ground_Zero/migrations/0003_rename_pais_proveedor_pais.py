# Generated by Django 3.2.3 on 2021-07-05 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ground_Zero', '0002_auto_20210704_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='Pais',
            new_name='pais',
        ),
    ]
