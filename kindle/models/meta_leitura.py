from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from kindle.models import BaseModel


class MetaLeitura(BaseModel):
    titulo = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='metas_leitura')
    quantidade_livros = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    data_inicio = models.DateField()
    data_termino = models.DateField()
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    def clean(self):
        super().clean()

        if self.data_termino <= self.data_inicio:
            raise ValidationError({
                "data_termino":
                    "A data final deve ser posterior à data inicial."
            })
