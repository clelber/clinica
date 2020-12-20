# Generated by Django 3.1.4 on 2020-12-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do funcionário', max_length=50, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
    ]
