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
        "tipo": "numero",
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
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Extensão Rede Secundária (m)",
        "nome": "Extensão PE110 (m)",
        "campo": "PE110",
        "coluna": 9,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Extensão Rede Secundária (m)",
        "nome": "Extensão PE160 (m)",
        "campo": "PE160",
        "coluna": 10,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Extensão Rede Secundária (m)",
        "nome": "Extensão PE200 (m)",
        "campo": "PE200",
        "coluna": 11,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Extensão Rede Secundária (m)",
        "nome": "Investimento (€)",
        "campo": "InvestimentoRede",
        "coluna": 13,
        "tipo": "numero",
        "editavel": True
    },

    # =====================================================
    # MERCADO POTENCIAL
    # =====================================================

    {
        "secao": "Mercado Potencial",
        "nome": "Moradia Conversão",
        "campo": "MoradiaConv",
        "coluna": 14,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Moradia Reconversão",
        "campo": "MoradiaReconv",
        "coluna": 15,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Moradia Nº Imóveis",
        "campo": "MoradiaImoveis",
        "coluna": 16,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Edif. Coletivo Conversão",
        "campo": "EdificioConv",
        "coluna": 17,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Edif. Coletivo Reconversão",
        "campo": "EdificioReconv",
        "coluna": 18,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Edif. Coletivo Nº Imóveis",
        "campo": "EdificioImoveis",
        "coluna": 19,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Pequeno Terciário",
        "campo": "PequenoTerciario",
        "coluna": 20,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Consumo estimado (m³)",
        "campo": "ConsumoExistente",
        "coluna": 21,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Mercado novo - Moradia",
        "campo": "NovoMoradia",
        "coluna": 23,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Mercado novo - Edif. Coletivo (PA)",
        "campo": "NovoEdificioPA",
        "coluna": 24,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Mercado novo - Edif. Coletivo (Nº Imóveis)",
        "campo": "NovoEdificioImoveis",
        "coluna": 25,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Mercado novo - Pequeno Terciário",
        "campo": "NovoTerciario",
        "coluna": 26,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Mercado novo - Consumo estimado (m³)",
        "campo": "NovoConsumo",
        "coluna": 27,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Grande consumidor - Nº de PA BP",
        "campo": "PABP",
        "coluna": 29,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Grande consumidor - Consumo estimado BP (m³)",
        "campo": "ConsumoBP",
        "coluna": 30,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Grande consumidor - Nº de PA MP",
        "campo": "PAMP",
        "coluna": 31,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Mercado Potencial",
        "nome": "Grande consumidor - Consumo estimado MP (m³)",
        "campo": "ConsumoMP",
        "coluna": 32,
        "tipo": "numero",
        "editavel": True
    },

    # =====================================================

    {
        "secao": "Taxa de Penetração",
        "nome": "Taxa de penetração estimada (%)",
        "campo": "TaxaPenetracao",
        "coluna": 36,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Indicadores de Mercado Existente",
        "nome": "Investimento (€)",
        "campo": "InvestimentoMercado",
        "coluna": 46,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Outros Investimentos",
        "nome": "Outros investimentos",
        "campo": "OutrosInvestimentos",
        "coluna": 49,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Indicadores Totais",
        "nome": "Comparticipações",
        "campo": "Comparticipacoes",
        "coluna": 52,
        "tipo": "numero",
        "editavel": True
    },

    {
        "secao": "Taxa Interna de Retorno",
        "nome": "Taxa Interna de Retorno - TIR (%)",
        "campo": "TIR",
        "coluna": 61,
        "tipo": "numero",
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
