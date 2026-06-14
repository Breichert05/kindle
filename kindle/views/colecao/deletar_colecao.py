from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from kindle.models import Colecao


class ColecaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Colecao
    template_name = "colecao/delete.html"
    success_url = reverse_lazy("colecao_list")