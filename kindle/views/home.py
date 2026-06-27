from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from kindle.enums import StatusLeitura
from kindle.models import BibliotecaUsuario


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["favoritos"] = BibliotecaUsuario.objects.filter(
            usuario=self.request.user,
            favorito=True
        ).select_related(
            "livro"
        )[:5]

        context["historico"] = BibliotecaUsuario.objects.filter(
            usuario=self.request.user,
            status_leitura__in=[
                StatusLeitura.LIDO,
                StatusLeitura.ABANDONADO
            ]
        ).select_related(
            "livro"
        ).order_by(
            "-data_adicao"
        )[:5]

        return context
