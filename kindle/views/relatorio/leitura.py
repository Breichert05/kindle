from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from kindle.models import (
    BibliotecaUsuario,
    Colecao,
    Nota,
    Avaliacao,
    MetaLeitura
)
from kindle.enums import StatusLeitura


class RelatorioLeituraView(LoginRequiredMixin, TemplateView):
    template_name = "relatorio/leitura.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        usuario = self.request.user

        context["total_livros"] = BibliotecaUsuario.objects.filter(
            usuario=usuario
        ).count()

        context["total_lidos"] = BibliotecaUsuario.objects.filter(
            usuario=usuario,
            status_leitura=StatusLeitura.LIDO
        ).count()

        context["total_favoritos"] = BibliotecaUsuario.objects.filter(
            usuario=usuario,
            favorito=True
        ).count()

        context["total_colecoes"] = Colecao.objects.filter(
            usuario=usuario
        ).count()

        context["total_notas"] = Nota.objects.filter(
            usuario=usuario
        ).count()

        context["total_avaliacoes"] = Avaliacao.objects.filter(
            usuario=usuario
        ).count()

        context["metas_ativas"] = MetaLeitura.objects.filter(
            usuario=usuario,
            concluida=False
        ).count()

        return context
