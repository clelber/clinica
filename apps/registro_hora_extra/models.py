from django.db import models
from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField('Motivo', max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, null=True, blank=True)
    horas = models.DecimalField('Horas', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Hora Extra'
        verbose_name_plural = 'Horas Extra'

    def __str__(self):
        return self.motivo






