from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome do funcionário')
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


