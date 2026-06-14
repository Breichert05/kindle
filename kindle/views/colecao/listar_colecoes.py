from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from kindle.models import Colecao


class ColecaoListView(LoginRequiredMixin, ListView):
    model = Colecao
    template_name = "colecao/list.html"
    context_object_name = "colecoes"

    def get_queryset(self):
        return Colecao.objects.filter(
            usuario=self.request.user
        )