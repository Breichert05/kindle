from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from kindle.enums import GeneroLivro
from kindle.managers import LivroManager
from kindle.models import BaseModel


class Livro(BaseModel):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    data_publicacao = models.DateField()
    isbn = models.CharField(max_length=20, unique=True)
    descricao = models.TextField(max_length=1000)
    numero_paginas = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    preco = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    genero = models.CharField(max_length=100, choices=GeneroLivro.choices)
    ativo = models.BooleanField(default=True)
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)

    objects = LivroManager()

    def __str__(self):
        return self.titulo

    def clean(self):
        super().clean()

        isbn_limpo = self.isbn.replace("-", "").strip()

        if len(isbn_limpo) < 10:
            raise ValidationError({
                "isbn": "O ISBN deve possuir pelo menos 10 caracteres."
            })
