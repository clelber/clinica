from django.db import models
from apps.funcionarios.models import Funcionario
from django.shortcuts import reverse


class Documento(models.Model):
    descricao = models.CharField('Descrição', max_length=65)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField('Arquivo', upload_to='documentos')

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Ducumentos'

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.funcionario.id])

    def __str__(self):
        return self.descricao
