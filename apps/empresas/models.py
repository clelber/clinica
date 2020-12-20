from django.db import models


class Empresa(models.Model):
    nome = models.CharField('Nome', max_length=100, help_text='Nome da empresa')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome


