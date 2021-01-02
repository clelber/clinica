from django.db import models
from django.urls import reverse


class Empresa(models.Model):
    nome = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('home')



