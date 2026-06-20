from django.db import models
from django.db.models import Q


class LivroManager(models.Manager):

    def ativos(self):
        return self.filter(ativo=True)

    def por_genero(self, genero):
        return self.ativos().filter(genero=genero)

    def buscar(self, termo=None, genero=None):
        queryset = self.ativos()

        if termo:
            queryset = queryset.filter(
                Q(titulo__icontains=termo) |
                Q(autor__icontains=termo)
            )

        if genero:
            queryset = queryset.filter(genero=genero)

        return queryset
