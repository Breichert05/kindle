from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from kindle.mixins import BootstrapFormMixin
from kindle.models import Avaliacao


class AvaliacaoUpdateView(BootstrapFormMixin, LoginRequiredMixin, UpdateView):
    model = Avaliacao
    template_name = 'avaliacao/form.html'
    fields = ['nota', 'comentario']
    success_url = reverse_lazy('avaliacao_list')
