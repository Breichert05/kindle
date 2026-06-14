from django.views.generic import DetailView

from kindle.models import Livro, BibliotecaUsuario


class LivroReadView(DetailView):
    model = Livro
    template_name = "livros/read.html"
    context_object_name = "livro"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        registro_biblioteca = BibliotecaUsuario.objects.filter(
            usuario=self.request.user,
            livro=self.object
        ).first()

        self.object.na_biblioteca = registro_biblioteca is not None
        self.object.biblioteca_id = (
            registro_biblioteca.id
            if registro_biblioteca
            else None
        )

        context["voltar_url"] = self.request.GET.get(
            "next",
            "/"
        )

        return context
