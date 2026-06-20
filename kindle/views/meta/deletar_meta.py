from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from kindle.models import MetaLeitura


class MetaDeleteView(LoginRequiredMixin, DeleteView):
    model = MetaLeitura
    template_name = 'meta/delete.html'
    success_url = reverse_lazy('meta_list')
