from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import UpdateView

from kindle.models import BibliotecaUsuario


class BibliotecaUsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = BibliotecaUsuario
    fields = ["status_leitura", "favorito"]

    def post(self, request, *args, **kwargs):
        biblioteca = self.get_object()

        if request.POST.get("toggle_favorito"):
            biblioteca.favorito = not biblioteca.favorito
        else:
            biblioteca.status_leitura = request.POST.get(
                "status_leitura"
            )

        biblioteca.save()

        return redirect(
            request.POST.get("next", "/")
        )
