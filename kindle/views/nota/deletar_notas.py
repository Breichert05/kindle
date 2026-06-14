from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from kindle.models import Nota


class NotaDeleteView(LoginRequiredMixin, DeleteView):
    model = Nota
    template_name = "nota/delete.html"
    success_url = reverse_lazy("nota_list")