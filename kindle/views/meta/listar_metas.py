from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from kindle.models import MetaLeitura


class MetaListView(LoginRequiredMixin, ListView):
    model = MetaLeitura
    template_name = 'meta/list.html'
    context_object_name = 'metas'

    def get_queryset(self):
        return MetaLeitura.objects.filter(usuario=self.request.user).order_by('-data_inicio')
