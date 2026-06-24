from django.db import models
from django.db.models import Q


class LivroManager(models.Manager):

    def ativos(self):
        return self.filter(ativo=True)

    def por_genero(self, genero):
        return self.filter(genero=genero)

    def buscar(
        self,
        termo=None,
        genero=None,
        preco_min=None,
        preco_max=None
    ):
        queryset = self.ativos()

        if termo:
            queryset = queryset.filter(
                Q(titulo__icontains=termo) |
                Q(autor__icontains=termo)
            )

        if genero:
            queryset = queryset.filter(
                genero=genero
            )

        if preco_min:
            queryset = queryset.filter(
                preco__gte=preco_min
            )

        if preco_max:
            queryset = queryset.filter(
                preco__lte=preco_max
            )

        return queryset