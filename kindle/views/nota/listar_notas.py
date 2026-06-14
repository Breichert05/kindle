from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from kindle.models import Nota


class NotaListView(LoginRequiredMixin, ListView):
    model = Nota
    template_name = "nota/list.html"
    context_object_name = "notas"

    def get_queryset(self):
        return Nota.objects.filter(
            usuario=self.request.user
        ).select_related(
            "livro"
        ).order_by(
            "-data_criacao"
        )
