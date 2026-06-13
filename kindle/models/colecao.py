from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from kindle.models import BaseModel, Livro


class Colecao(BaseModel):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=1000)
    livros = models.ManyToManyField(Livro, related_name='colecoes')
    ativo = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='colecoes')

    def __str__(self):
        return self.nome

    def clean(self):
        super().clean()

        if not self.nome:
            raise ValidationError({
                "nome": "O nome da coleção não pode estar vazio."
            })
