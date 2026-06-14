from django.views.generic import DetailView

from kindle.models import Livro, BibliotecaUsuario


class LivroReadView(DetailView):
    model = Livro
    template_name = "livros/read.html"
    context_object_name = "livro"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["na_biblioteca"] = BibliotecaUsuario.objects.filter(
            usuario=self.request.user,
            livro=self.object
        ).exists()

        context["voltar_url"] = self.request.META.get(
            "HTTP_REFERER",
            "/"
        )

        return context
