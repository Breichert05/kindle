from django.db import models


class BibliotecaManager(models.Manager):
    def retorna_favoritos(self):
        return self.filter(favorito=True).select_related('livro')
