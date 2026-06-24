from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from kindle.mixins import BootstrapFormMixin
from kindle.models import Nota


class NotaUpdateView(BootstrapFormMixin, LoginRequiredMixin, UpdateView):
    model = Nota
    template_name = "nota/update.html"

    fields = [
        "titulo",
        "conteudo",
        "pagina"
    ]

    success_url = reverse_lazy("nota_list")