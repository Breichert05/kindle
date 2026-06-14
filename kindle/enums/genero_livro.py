from django.db.models import TextChoices


class GeneroLivro(TextChoices):
    FICCAO = 'FICCAO', 'Ficção'
    FANTASIA = 'FANTASIA', 'Fantasia'
    ROMANCE = 'ROMANCE', 'Romance'
    MISTERIO = 'MISTERIO', 'Mistério'
    DRAMA = 'DRAMA', 'Drama'
    HISTORICO = 'HISTORICO', 'Histórico'
    BIOGRAFIA = 'BIOGRAFIA', 'Biografia'
    TERROR = 'TERROR', 'Terror'
    AVENTURA = 'AVENTURA', 'Aventura'
    AUTOAJUDA = 'AUTOAJUDA', 'Autoajuda'
    CULINARIA = 'CULINARIA', 'Culinária'
    POESIA = 'POESIA', 'Poesia'
    FICCAO_CIENTIFICA = 'FICCAO_CIENTIFICA', 'Ficção Científica'
    OUTROS = 'OUTROS', 'Outros'
