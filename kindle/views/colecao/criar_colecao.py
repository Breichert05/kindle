from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from kindle.models import Colecao


class ColecaoCreateView(LoginRequiredMixin, CreateView):
    model = Colecao
    template_name = "colecao/create.html"
    fields = ["nome", "descricao", "livros"]
    success_url = reverse_lazy("colecao_list")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        for field in form.fields.values():
            field.widget.attrs["class"] = "form-control"

        return form
