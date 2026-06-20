from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from kindle.models import Livro


class LivroDeleteView(PermissionRequiredMixin, DeleteView):
    model = Livro
    template_name = 'livros/delete.html'
    permission_required = 'kindle.delete_livro'
    success_url = reverse_lazy('acervo')
