from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from kindle.mixins import BootstrapFormMixin
from kindle.models import Colecao


class ColecaoUpdateView(BootstrapFormMixin, LoginRequiredMixin, UpdateView):
    model = Colecao
    template_name = "colecao/update.html"
    fields = ["nome", "descricao", "livros"]
    success_url = reverse_lazy("colecao_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        for field in form.fields.values():
            field.widget.attrs["class"] = "form-control"

        return form
    