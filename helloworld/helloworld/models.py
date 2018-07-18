# coding=utf-8

from django.db import models
import datetime

class Comercio(models.Model):

    name = models.CharField(
        'Comércio',
        max_length=100,
        null=False,
        blank=False
    )

    slug = models.CharField(
        'Identificador',
        max_length=100,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        'Criado em',
        auto_now_add=True,
        null=True
    )

    updated_at = models.DateTimeField(
        'Atualizado em',
        auto_now=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comércio'
        verbose_name_plural = 'Comércios'
        ordering = ['-created_at']

    objetos = models.Manager()

class Gasto(models.Model):

    name = models.CharField(
        'Gasto',
        max_length=100,
        null=False,
        blank=False
    )

    slug = models.CharField(
        'Identificador',
        max_length=100,
        null=False,
        blank=False
    )

    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

    # valor = BRDecimalField(
    #     u'Valor',
    #     max_digits=8,
    #     decimal_places=2,
    #     null=False,
    #     blank=False
    # )

    datagasto = models.DateField(
        default=datetime.datetime.today,
        null=True,
        blank=True
    )

    comercio = models.ForeignKey(
        Comercio,
        verbose_name='Comércio',
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(
        'Criado em',
        auto_now_add=True,
        null=True
    )

    modified_at = models.DateTimeField(
        'Atualizado em',
        auto_now=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        ordering = ['-datagasto']

    objetos = models.Manager()
