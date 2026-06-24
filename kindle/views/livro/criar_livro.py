from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from kindle.mixins import BootstrapFormMixin
from kindle.models import Livro


class LivroCreateView(BootstrapFormMixin, PermissionRequiredMixin, CreateView):
    model = Livro
    template_name = 'livros/form.html'
    fields = [
        'titulo', 'autor', 'data_publicacao', 'isbn', 'descricao',
        'numero_paginas', 'preco', 'genero', 'ativo', 'capa'
    ]
    permission_required = 'kindle.add_livro'
    success_url = reverse_lazy('acervo')
