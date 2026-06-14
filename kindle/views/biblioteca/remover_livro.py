from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from kindle.models import BibliotecaUsuario


class BibliotecaUsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = BibliotecaUsuario
    template_name = "biblioteca/delete.html"

    def get_success_url(self):
        return self.request.GET.get(
            "next"
        ) or self.request.POST.get(
            "next"
        ) or reverse_lazy("acervo")