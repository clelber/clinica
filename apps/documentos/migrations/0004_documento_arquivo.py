# Generated by Django 3.1.4 on 2021-01-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_auto_20201220_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default='', upload_to='documentos', verbose_name='Arquivo'),
            preserve_default=False,
        ),
    ]
