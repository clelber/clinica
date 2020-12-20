from django.db import models


class Departamento(models.Model):
    nome = models.CharField('Nome', max_length=65)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nome
