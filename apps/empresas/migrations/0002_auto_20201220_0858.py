# Generated by Django 3.1.4 on 2020-12-20 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empresa',
            new_name='Empresas',
        ),
        migrations.AlterModelOptions(
            name='empresas',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
    ]