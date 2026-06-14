from django.shortcuts import render
from django.views import View


class IndexView(View):
    @staticmethod
    def get(request):
        contexto = {
            "mensagem": "Bem-vindo(a)!"
        }

        return render(request, "index.html", contexto)