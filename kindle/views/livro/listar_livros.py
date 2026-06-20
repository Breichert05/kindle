from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from kindle.models import Livro, BibliotecaUsuario


class AcervoListView(LoginRequiredMixin, ListView):
    model = Livro
    template_name = 'livros/list.html'
    context_object_name = 'livros'

    def get_queryset(self):
        bibliotecas = {
            item.livro_id: item.id
            for item in BibliotecaUsuario.objects.filter(
                usuario=self.request.user
            )
        }

        livros = Livro.objects.buscar(
            termo=self.request.GET.get("q"),
            genero=self.request.GET.get("genero")
        )

        livros = list(livros)

        for livro in livros:
            livro.na_biblioteca = livro.id in bibliotecas
            livro.biblioteca_id = bibliotecas.get(livro.id)

        return livros