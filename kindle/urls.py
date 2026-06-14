"""
URL configuration for kindle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from kindle.views.biblioteca.editar_livro import BibliotecaUsuarioUpdateView
from kindle.views.biblioteca.listar_biblioteca import BibliotecaListView
from kindle.views.colecao.criar_colecao import ColecaoCreateView
from kindle.views.colecao.deletar_colecao import ColecaoDeleteView
from kindle.views.colecao.detalhar_colecao import ColecaoReadView
from kindle.views.colecao.editar_colecao import ColecaoUpdateView
from kindle.views.colecao.listar_colecoes import ColecaoListView
from kindle.views.livro.listar_livros import AcervoListView
from kindle.views.biblioteca.adicionar_livro import BibliotecaUsuarioCreateView
from kindle.views.biblioteca.remover_livro import BibliotecaUsuarioDeleteView
from kindle.views.home import IndexView
from django.conf import settings
from django.conf.urls.static import static

from kindle.views.livro.detalhar_livro import LivroReadView
from kindle.views.nota.criar_nota import NotaCreateView
from kindle.views.nota.deletar_notas import NotaDeleteView
from kindle.views.nota.editar_notas import NotaUpdateView
from kindle.views.nota.listar_notas import NotaListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", IndexView.as_view(), name="index"),
    path("acervo/", AcervoListView.as_view(), name="acervo"),
    path("acervo/read/<int:pk>", LivroReadView.as_view(), name="livro_read"),
    path("biblioteca/", BibliotecaListView.as_view(), name="minha_biblioteca"),
    path("biblioteca/create/<int:pk>/", BibliotecaUsuarioCreateView.as_view(), name="biblioteca_adicionar"),
    path("biblioteca/delete/<int:pk>/", BibliotecaUsuarioDeleteView.as_view(), name="biblioteca_delete"),
    path("biblioteca/update/<int:pk>/", BibliotecaUsuarioUpdateView.as_view(), name="biblioteca_update"),
    path("colecao/", ColecaoListView.as_view(), name="colecao_list"),
    path("colecao/read/<int:pk>/", ColecaoReadView.as_view(), name="colecao_read"),
    path("colecao/create/", ColecaoCreateView.as_view(), name="colecao_create"),
    path("colecao/delete/<int:pk>/", ColecaoDeleteView.as_view(), name="colecao_delete"),
    path("colecao/update/<int:pk>/", ColecaoUpdateView.as_view(), name="colecao_update"),
    path("notas/", NotaListView.as_view(), name="nota_list"),
    path("notas/create/<int:pk>/", NotaCreateView.as_view(), name="nota_create"),
    path("notas/delete/<int:pk>/", NotaDeleteView.as_view(),name="nota_delete"),
    path("notas/update/<int:pk>/", NotaUpdateView.as_view(),name="nota_update"),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
