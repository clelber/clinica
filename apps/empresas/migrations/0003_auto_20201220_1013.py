# Generated by Django 3.1.4 on 2020-12-20 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
        ('empresas', '0002_auto_20201220_0858'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empresas',
            new_name='Empresa',
        ),
    ]
