from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from kindle.models import BibliotecaUsuario


class MinhaBibliotecaListView(
    LoginRequiredMixin,
    ListView
):
    model = BibliotecaUsuario
    template_name = "biblioteca/list.html"
    context_object_name = "biblioteca"

    def get_queryset(self):
        return BibliotecaUsuario.objects.filter(
            usuario=self.request.user
        ).select_related("livro")