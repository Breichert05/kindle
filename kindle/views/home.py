from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from kindle.models import BibliotecaUsuario, Colecao, Nota, MetaLeitura


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_livros"] = BibliotecaUsuario.objects.filter(
            usuario=self.request.user
        ).count()

        context["total_colecoes"] = Colecao.objects.filter(
            usuario=self.request.user
        ).count()

        context["total_notas"] = Nota.objects.filter(
            usuario=self.request.user
        ).count()

        context["total_lidos"] = BibliotecaUsuario.objects.filter(
            usuario=self.request.user,
            status_leitura="LIDO"
        ).count()

        context["metas_ativas"] = MetaLeitura.objects.filter(
            usuario=self.request.user,
            concluida=False
        ).count()

        return context
