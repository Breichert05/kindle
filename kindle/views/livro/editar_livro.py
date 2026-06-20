from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from kindle.models import Livro


class LivroUpdateView(PermissionRequiredMixin, UpdateView):
    model = Livro
    template_name = 'livros/form.html'
    fields = [
        'titulo', 'autor', 'data_publicacao', 'isbn', 'descricao',
        'numero_paginas', 'preco', 'genero', 'ativo', 'capa'
    ]
    permission_required = 'kindle.change_livro'
    success_url = reverse_lazy('acervo')
