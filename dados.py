# dados.py

# Estados possíveis da obra
ESTADOS = [
    "Em avaliação",
    "Pendente de Nova Decisão",
    "Anulado",
    "Para Execução",
    "Em Execução",
    "Executado"
]


# Definição dos campos da folha "Recenseamentos"
# coluna -> número da coluna no Excel (começa em 1)
# tipo -> texto | numero | lista
# editavel -> se pode ser alterado pela aplicação

CAMPOS = [

    {
        "nome": "ID",
        "coluna": 1,
        "tipo": "numero",
        "editavel": False
    },

    {
        "nome": "Concelho",
        "coluna": 2,
        "tipo": "texto",
        "editavel": True
    },

    {
        "nome": "RefObra",
        "coluna": 3,
        "tipo": "texto",
        "editavel": True
    },

    {
        "nome": "Estado",
        "coluna": 4,
        "tipo": "lista",
        "opcoes": ESTADOS,
        "editavel": True
    },

    {
        "nome": "Rua",
        "coluna": 5,
        "tipo": "texto",
        "editavel": True
    },

    {
        "nome": "NumeroPolicia",
        "coluna": 6,
        "tipo": "texto",
        "editavel": True
    }

]
