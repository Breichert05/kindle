from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from kindle.enums import StatusLeitura
from kindle.mixins import BootstrapFormMixin
from kindle.models import BibliotecaUsuario, Livro


class BibliotecaUsuarioCreateView(BootstrapFormMixin, LoginRequiredMixin, CreateView):
    model = BibliotecaUsuario
    fields = []
    template_name = "biblioteca/create.html"

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
        form.instance.status_leitura = StatusLeitura.QUERO_LER

        form.instance.full_clean()

        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get(
            "next"
        ) or self.request.POST.get(
            "next"
        ) or reverse_lazy("acervo")
