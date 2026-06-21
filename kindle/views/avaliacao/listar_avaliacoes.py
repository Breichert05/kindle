from django.views.generic import ListView

from kindle.models import Avaliacao


class AvaliacaoListView(ListView):
    model = Avaliacao
    template_name = 'avaliacao/list.html'
    context_object_name = 'avaliacoes'

    def get_queryset(self):
        return Avaliacao.objects.filter(
            usuario=self.request.user
        ).select_related(
            "livro"
        )
