from django.views.generic import DetailView

from kindle.models import Nota


class NotaReadView(DetailView):
    model = Nota
    template_name = 'nota/read.html'
    context_object_name = 'nota'

    def get_queryset(self):
        return Nota.objects.select_related(
            'livro',
            'usuario'
        )
