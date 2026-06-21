from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from kindle.models import Nota, Livro


class NotaCreateView(LoginRequiredMixin, CreateView):
    model = Nota
    template_name = "nota/create.html"

    fields = [
        "titulo",
        "conteudo",
        "pagina"
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["livro"] = get_object_or_404(
            Livro,
            pk=self.kwargs["pk"]
        )

        return context

    def form_valid(self, form):
        livro = get_object_or_404(
            Livro,
            pk=self.kwargs["pk"]
        )

        form.instance.usuario = self.request.user
        form.instance.livro = livro

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "biblioteca_list"
        )
