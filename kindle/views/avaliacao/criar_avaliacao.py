from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from kindle.models import Avaliacao, Livro


class AvaliacaoCreateView(LoginRequiredMixin, CreateView):
    model = Avaliacao
    template_name = 'avaliacao/form.html'
    fields = ['nota', 'comentario']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livro'] = get_object_or_404(Livro, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.livro = get_object_or_404(Livro, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('avaliacao_list')
