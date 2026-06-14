from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from kindle.enums import StatusLeitura
from kindle.models import BibliotecaUsuario


class BibliotecaListView(LoginRequiredMixin, ListView):
    model = BibliotecaUsuario
    template_name = "biblioteca/list.html"
    context_object_name = "biblioteca"

    def get_queryset(self):
        return BibliotecaUsuario.objects.filter(
            usuario=self.request.user
        ).select_related(
            "livro"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["status_choices"] = StatusLeitura.choices

        return context