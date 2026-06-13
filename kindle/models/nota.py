from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from kindle.models import BaseModel, Livro


class Nota(BaseModel):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField(max_length=2000)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='notas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notas')
    pagina = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def clean(self):
        super().clean()

        if not self.conteudo:
            raise ValidationError({
                "conteudo": "A nota não pode estar vazia."
            })
