from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from kindle.mixins import BootstrapFormMixin
from kindle.models import MetaLeitura


class MetaUpdateView(BootstrapFormMixin, LoginRequiredMixin, UpdateView):
    model = MetaLeitura
    template_name = 'meta/form.html'
    fields = ['titulo', 'quantidade_livros', 'data_inicio', 'data_termino', 'concluida']
    success_url = reverse_lazy('meta_list')
