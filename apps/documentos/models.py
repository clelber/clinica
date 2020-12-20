from django.db import models
from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField('Descrição', max_length=65)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Ducumentos'

    def __str__(self):
        return self.descricao
