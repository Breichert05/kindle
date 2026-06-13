from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from kindle.enums import StatusLeitura
from kindle.models import BaseModel, Livro


class BibliotecaUsuario(BaseModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='biblioteca')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='biblioteca_usuario')
    data_adicao = models.DateTimeField(auto_now_add=True)
    favorito = models.BooleanField(default=False)
    status_leitura = models.CharField(max_length=20, choices=StatusLeitura.choices)

    def __str__(self):
        return f'{self.usuario.username} - {self.livro.titulo}'

    def clean(self):
        super().clean()

        registro = BibliotecaUsuario.objects.filter(
            usuario=self.usuario,
            livro=self.livro
        )

        if self.pk:
            registro = registro.exclude(pk=self.pk)

        if registro.exists():
            raise ValidationError(
                "Este livro já está na sua biblioteca."
            )
