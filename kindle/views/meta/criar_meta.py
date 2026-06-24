from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from kindle.mixins import BootstrapFormMixin
from kindle.models import MetaLeitura


class MetaCreateView(BootstrapFormMixin, LoginRequiredMixin, CreateView):
    model = MetaLeitura
    template_name = 'meta/form.html'
    fields = ['titulo', 'quantidade_livros', 'data_inicio', 'data_termino', 'concluida']
    success_url = reverse_lazy('meta_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
