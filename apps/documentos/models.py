from django.db import models


class Documento(models.Model):
    Descricao = models.CharField('Descrição', max_length=65)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Ducumentos'

    def __str__(self):
        return self.Descricao
