from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from kindle.enums import StatusLeitura
from kindle.models import BibliotecaUsuario


class HistoricoListView(LoginRequiredMixin, ListView):
    model = BibliotecaUsuario
    template_name = "historico/list.html"
    context_object_name = "historico"

    def get_queryset(self):
        return BibliotecaUsuario.objects.filter(
            usuario=self.request.user,
            status_leitura__in=[
                StatusLeitura.LIDO,
                StatusLeitura.ABANDONADO
            ]
        ).select_related(
            "livro"
        ).order_by(
            "-data_adicao"
        )