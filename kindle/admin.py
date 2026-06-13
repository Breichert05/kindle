from django.contrib import admin

from kindle.models.colecao import Colecao
from kindle.models.meta_leitura import MetaLeitura
from kindle.models.biblioteca_usuario import BibliotecaUsuario
from kindle.models.avaliacao import Avaliacao
from kindle.models.nota import Nota
from kindle.models.livro import Livro

admin.site.register(Livro)
admin.site.register(Nota)
admin.site.register(Avaliacao)
admin.site.register(BibliotecaUsuario)
admin.site.register(Colecao)
admin.site.register(MetaLeitura)

