from django.db.models import TextChoices


class StatusLeitura(TextChoices):
    LENDO = "LENDO", "Lendo"
    QUERO_LER = "QUERO_LER", "Quero Ler"
    LIDO = "LIDO", "Lido"
    ABANDONADO = "ABANDONADO", "Abandonado"