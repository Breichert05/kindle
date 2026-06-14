import os
from datetime import date
from decimal import Decimal

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kindle.settings")
django.setup()

from kindle.models import Livro
from kindle.enums import GeneroLivro

livros = [
    {
        "titulo": "A Chama de Eldoria",
        "autor": "Marcos Valente",
        "data_publicacao": date(2018, 5, 12),
        "isbn": "1000000001",
        "descricao": "Uma jovem descobre um poder ancestral capaz de mudar o destino de seu reino.",
        "numero_paginas": 412,
        "preco": Decimal("49.90"),
        "genero": GeneroLivro.FANTASIA,
    },
    {
        "titulo": "O Último Guardião",
        "autor": "Ana Ribeiro",
        "data_publicacao": date(2020, 8, 20),
        "isbn": "1000000002",
        "descricao": "O último defensor de uma cidade perdida enfrenta criaturas das sombras.",
        "numero_paginas": 368,
        "preco": Decimal("42.50"),
        "genero": GeneroLivro.AVENTURA,
    },
    {
        "titulo": "Entre Estrelas Distantes",
        "autor": "Carlos Mendes",
        "data_publicacao": date(2022, 3, 15),
        "isbn": "1000000003",
        "descricao": "Uma missão interestelar revela segredos sobre a origem da humanidade.",
        "numero_paginas": 520,
        "preco": Decimal("59.90"),
        "genero": GeneroLivro.FICCAO_CIENTIFICA,
    },
    {
        "titulo": "Sombras de Inverno",
        "autor": "Fernanda Costa",
        "data_publicacao": date(2017, 11, 2),
        "isbn": "1000000004",
        "descricao": "Mistérios antigos começam a surgir durante um rigoroso inverno.",
        "numero_paginas": 298,
        "preco": Decimal("34.90"),
        "genero": GeneroLivro.MISTERIO,
    },
    {
        "titulo": "Além do Horizonte",
        "autor": "Ricardo Oliveira",
        "data_publicacao": date(2019, 7, 8),
        "isbn": "1000000005",
        "descricao": "Uma emocionante história sobre reencontros e segundas chances.",
        "numero_paginas": 276,
        "preco": Decimal("29.90"),
        "genero": GeneroLivro.ROMANCE,
    },
    {
        "titulo": "A Cidade Perdida",
        "autor": "Juliana Lopes",
        "data_publicacao": date(2021, 4, 28),
        "isbn": "1000000006",
        "descricao": "Exploradores encontram uma cidade esquecida no coração da floresta.",
        "numero_paginas": 445,
        "preco": Decimal("47.90"),
        "genero": GeneroLivro.AVENTURA,
    },
    {
        "titulo": "Código Eclipse",
        "autor": "Lucas Ferreira",
        "data_publicacao": date(2023, 1, 10),
        "isbn": "1000000007",
        "descricao": "Hackers descobrem um código capaz de controlar sistemas globais.",
        "numero_paginas": 390,
        "preco": Decimal("54.90"),
        "genero": GeneroLivro.FICCAO_CIENTIFICA,
    },
    {
        "titulo": "O Castelo das Névoas",
        "autor": "Patrícia Martins",
        "data_publicacao": date(2016, 9, 30),
        "isbn": "1000000008",
        "descricao": "Uma fortaleza cercada por névoas guarda segredos centenários.",
        "numero_paginas": 330,
        "preco": Decimal("39.90"),
        "genero": GeneroLivro.FANTASIA,
    },
    {
        "titulo": "Segredos do Passado",
        "autor": "Bruno Almeida",
        "data_publicacao": date(2015, 2, 18),
        "isbn": "1000000009",
        "descricao": "Documentos antigos revelam acontecimentos esquecidos pela história.",
        "numero_paginas": 355,
        "preco": Decimal("36.90"),
        "genero": GeneroLivro.HISTORICO,
    },
    {
        "titulo": "Noite Sem Lua",
        "autor": "Gabriela Souza",
        "data_publicacao": date(2021, 10, 31),
        "isbn": "1000000010",
        "descricao": "Eventos assustadores transformam uma pequena cidade do interior.",
        "numero_paginas": 287,
        "preco": Decimal("32.90"),
        "genero": GeneroLivro.TERROR,
    },
    {
        "titulo": "As Crônicas de Veridian",
        "autor": "Thiago Nunes",
        "data_publicacao": date(2020, 6, 14),
        "isbn": "1000000011",
        "descricao": "Heróis improváveis unem forças para salvar o continente de Veridian.",
        "numero_paginas": 612,
        "preco": Decimal("69.90"),
        "genero": GeneroLivro.FANTASIA,
    },
    {
        "titulo": "Reflexos da Alma",
        "autor": "Mariana Duarte",
        "data_publicacao": date(2018, 1, 22),
        "isbn": "1000000012",
        "descricao": "Uma jornada emocional sobre identidade, amor e autoconhecimento.",
        "numero_paginas": 248,
        "preco": Decimal("27.90"),
        "genero": GeneroLivro.ROMANCE,
    },
    {
        "titulo": "Operação Tempestade",
        "autor": "Rafael Cardoso",
        "data_publicacao": date(2022, 12, 5),
        "isbn": "1000000013",
        "descricao": "Uma investigação internacional tenta impedir uma catástrofe iminente.",
        "numero_paginas": 418,
        "preco": Decimal("52.90"),
        "genero": GeneroLivro.MISTERIO,
    },
    {
        "titulo": "A Fórmula do Amanhã",
        "autor": "Camila Rocha",
        "data_publicacao": date(2024, 2, 9),
        "isbn": "1000000014",
        "descricao": "Uma cientista descobre uma fórmula capaz de prever eventos futuros.",
        "numero_paginas": 501,
        "preco": Decimal("61.90"),
        "genero": GeneroLivro.FICCAO_CIENTIFICA,
    },
]

for dados in livros:
    try:
        livro = Livro(**dados)
        livro.full_clean()
        livro.save()

        print(f"{livro.titulo}")

    except Exception as e:
        print(f"Erro ao criar {dados['titulo']}: {e}")

print("\nCarga finalizada.")