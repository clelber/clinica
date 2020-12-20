from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField('Motivo', max_length=100)

    class Meta:
        verbose_name = 'Hora Extra'
        verbose_name_plural = 'Horas Extra'

    def __str__(self):
        return self.motivo






