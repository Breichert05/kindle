from django.views.generic import DetailView

from kindle.models import Colecao, BibliotecaUsuario


class ColecaoReadView(DetailView):
    model = Colecao
    template_name = "colecao/read.html"
    context_object_name = "colecao"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        livros_usuario = BibliotecaUsuario.objects.filter(
            usuario=self.request.user
        )

        livros_usuario_ids = set(
            livros_usuario.values_list(
                "livro_id",
                flat=True
            )
        )

        livros = list(self.object.livros.all())

        for livro in livros:
            livro.na_biblioteca = livro.id in livros_usuario_ids

            registro = livros_usuario.filter(
                livro=livro
            ).first()

            livro.biblioteca_id = registro.id if registro else None

        context["livros"] = livros

        return context
