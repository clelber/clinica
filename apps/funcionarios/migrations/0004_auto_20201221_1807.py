# Generated by Django 3.1.4 on 2020-12-21 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_auto_20201220_1013'),
        ('funcionarios', '0003_auto_20201220_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
        ),
    ]