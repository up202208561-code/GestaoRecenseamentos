# dados.py

ESTADOS = [
    "Em avaliação",
    "Pendente de Nova Decisão",
    "Anulado",
    "Para Execução",
    "Em Execução",
    "Executado"
]

CAMPOS = [

    # =====================================================
    # VALORES GLOBAIS
    # =====================================================

    {
        "secao": "Valores Globais",
        "nome": "ID",
        "campo": "ID",
        "coluna": 1,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Valores Globais",
        "nome": "Concelho",
        "campo": "Concelho",
        "coluna": 2,
        "tipo": "texto",
        "editavel": True
    },

    {
        "secao": "Valores Globais",
        "nome": "Ref. Obra",
        "campo": "RefObra",
        "coluna": 3,
        "tipo": "texto",
        "editavel": True
    },

    {
        "secao": "Valores Globais",
        "nome": "Estado",
        "campo": "Estado",
        "coluna": 4,
        "tipo": "lista",
        "opcoes": ESTADOS,
        "editavel": True
    },

    {
        "secao": "Valores Globais",
        "nome": "Rua(s)",
        "campo": "Rua",
        "coluna": 5,
        "tipo": "texto",
        "editavel": True
    },

    {
        "secao": "Valores Globais",
        "nome": "Nº polícia inicial",
        "campo": "NumeroInicial",
        "coluna": 6,
        "tipo": "texto",
        "editavel": True
    },

    {
        "secao": "Valores Globais",
        "nome": "Nº polícia final",
        "campo": "NumeroFinal",
        "coluna": 7,
        "tipo": "texto",
        "editavel": True
    },

    # =====================================================
    # EXTENSÃO REDE SECUNDÁRIA
    # =====================================================

    {
        "secao": "Extensão Rede Secundária (m)",
        "nome": "Extensão PE63 (m)",
        "campo": "PE63",
        "coluna": 8,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Extensão Rede Secundária (m)",
        "nome": "Extensão PE110 (m)",
        "campo": "PE110",
        "coluna": 9,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Extensão Rede Secundária (m)",
        "nome": "Extensão PE160 (m)",
        "campo": "PE160",
        "coluna": 10,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Extensão Rede Secundária (m)",
        "nome": "Extensão PE200 (m)",
        "campo": "PE200",
        "coluna": 11,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Extensão Rede Secundária (m)",
        "nome": "Investimento (€)",
        "campo": "InvestimentoRede",
        "coluna": 13,
        "tipo": "float",
        "editavel": True
    },

    # =====================================================
    # MERCADO POTENCIAL
    # =====================================================

    {
        "secao": "Mercado Potencial - Mercado Existente",
        "nome": "Nº Moradias Conversão",
        "campo": "MoradiaConv",
        "coluna": 14,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Mercado Existente",
        "nome": "Nº Moradias Reconversão",
        "campo": "MoradiaReconv",
        "coluna": 15,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Mercado Existente",
        "nome": "Nº Edif. Coletivo Conversão",
        "campo": "EdificioConv",
        "coluna": 17,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Mercado Existente",
        "nome": "Nº Edif. Coletivo Reconversão",
        "campo": "EdificioReconv",
        "coluna": 18,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Mercado Existente",
        "nome": "Nº Pequeno Terciário",
        "campo": "PequenoTerciario",
        "coluna": 20,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Mercado Existente",
        "nome": "Consumo estimado (m³)",
        "campo": "ConsumoExistente",
        "coluna": 21,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Mercado Novo",
        "nome": "Nº Moradias",
        "campo": "NovoMoradia",
        "coluna": 23,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Mercado Novo",
        "nome": "Edif. Coletivo (Nº PAs)",
        "campo": "NovoEdificioPA",
        "coluna": 24,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Mercado Novo",
        "nome": "Edif. Coletivo (Nº Imóveis)",
        "campo": "NovoEdificioImoveis",
        "coluna": 25,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Mercado Novo",
        "nome": "Nº Pequeno Terciário",
        "campo": "NovoTerciario",
        "coluna": 26,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Mercado Novo",
        "nome": "Consumo estimado (m³)",
        "campo": "NovoConsumo",
        "coluna": 27,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Grande Consumidor",
        "nome": "Nº de PAs BP",
        "campo": "PABP",
        "coluna": 29,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Grande Consumidor",
        "nome": "Consumo estimado BP (m³)",
        "campo": "ConsumoBP",
        "coluna": 30,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Grande Consumidor",
        "nome": "Nº de PAs MP",
        "campo": "PAMP",
        "coluna": 31,
        "tipo": "int",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial - Grande Consumidor",
        "nome": "Consumo estimado MP (m³)",
        "campo": "ConsumoMP",
        "coluna": 32,
        "tipo": "float",
        "editavel": True
    },

    # =====================================================

    {
        "secao": "Taxa de Penetração",
        "nome": "Taxa de penetração estimada (%)",
        "campo": "TaxaPenetracao",
        "coluna": 36,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Indicadores de Mercado Existente",
        "nome": "Investimento (€)",
        "campo": "InvestimentoMercado",
        "coluna": 46,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Outros Investimentos",
        "nome": "Outros investimentos",
        "campo": "OutrosInvestimentos",
        "coluna": 49,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Indicadores Totais",
        "nome": "Comparticipações",
        "campo": "Comparticipacoes",
        "coluna": 52,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Taxa Interna de Retorno",
        "nome": "Taxa Interna de Retorno - TIR (%)",
        "campo": "TIR",
        "coluna": 61,
        "tipo": "float",
        "editavel": True
    },

    {
        "secao": "Detalhes de Outros Investimentos",
        "nome": "Detalhes de Outros Investimentos",
        "campo": "DetalhesInvestimento",
        "coluna": 62,
        "tipo": "texto",
        "editavel": True
    },

    {
        "secao": "Observações",
        "nome": "Observações",
        "campo": "Observacoes",
        "coluna": 63,
        "tipo": "texto",
        "editavel": True
    }

]
