import pandas as pd
import openpyxl
import tempfile

from copy import copy
from openpyxl.formula.translate import Translator

from dados import CAMPOS


def ler_recenseamentos(ficheiro):
    """
    Lê a folha Recenseamentos e devolve um DataFrame
    com os campos definidos em CAMPOS.
    """

    dados = pd.read_excel(
        ficheiro,
        sheet_name="Recenseamentos",
        header=None
    )

    # Ignorar cabeçalhos (linhas 1 a 5)
    dados = dados.iloc[5:]

    projetos = pd.DataFrame()

    for campo in CAMPOS:
        projetos[campo["campo"]] = dados.iloc[:, campo["coluna"] - 1]

    projetos = projetos.dropna(subset=["RefObra"])

    return projetos


def pesquisar_projetos(projetos, texto):
    """
    Pesquisa um texto em todas as colunas.
    """

    texto = texto.lower()

    return projetos[
        projetos.astype(str)
        .apply(
            lambda coluna:
                coluna.str.lower().str.contains(texto, na=False)
        )
        .any(axis=1)
    ]


def guardar_estado(ficheiro, ref_obra, novo_estado):
    """
    Atualiza o estado de uma obra.
    """

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".xlsm"
    )

    temp.write(ficheiro.getvalue())
    temp.close()

    wb = openpyxl.load_workbook(
        temp.name,
        keep_vba=True
    )

    ws = wb["Recenseamentos"]

    for linha in range(6, ws.max_row + 1):

        referencia = ws.cell(
            row=linha,
            column=3
        ).value

        if referencia == ref_obra:

            ws.cell(
                row=linha,
                column=4
            ).value = novo_estado

            break

    wb.save(temp.name)

    return temp.name
    


def procurar_linha_projeto(ws, ref_obra):
    """
    Procura a linha correspondente a uma referência de obra.
    """

    for linha in range(6, ws.max_row + 1):

        if ws.cell(row=linha, column=3).value == ref_obra:
            return linha

    return None


def ler_projeto(ws, linha):
    """
    Lê todos os campos definidos em CAMPOS para uma determinada linha
    da folha Recenseamentos.

    Devolve um dicionário.
    """

    projeto = {}

    for campo in CAMPOS:

        projeto[campo["campo"]] = ws.cell(
            row=linha,
            column=campo["coluna"]
        ).value

    return projeto

def guardar_projeto(ficheiro, ref_obra, dados_projeto):
    """
    Atualiza todos os campos editáveis de uma obra.
    dados_projeto é um dicionário:
    {
        "Concelho": "...",
        "Estado": "...",
        "Rua": "...",
        ...
    }
    """

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".xlsm"
    )

    temp.write(
        ficheiro.getvalue()
    )

    temp.close()

    wb = openpyxl.load_workbook(
        temp.name,
        keep_vba=True
    )

    ws = wb["Recenseamentos"]

    linha = procurar_linha_projeto(
        ws,
        ref_obra
    )

    if linha is None:
        raise Exception("Projeto não encontrado.")

    for campo in CAMPOS:

        if not campo["editavel"]:
            continue

        nome = campo["campo"]

        if nome in dados_projeto:

            ws.cell(
                row=linha,
                column=campo["coluna"]
            ).value = dados_projeto[nome]

    wb.save(temp.name)

    return temp.name

def criar_projeto(ficheiro, dados_projeto):
    """
    Cria uma nova obra copiando a última linha existente,
    mantendo fórmulas, estilos e formatação.
    """

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".xlsm"
    )

    temp.write(
        ficheiro.getvalue()
    )

    temp.close()

    wb = openpyxl.load_workbook(
        temp.name,
        keep_vba=True
    )

    ws = wb["Recenseamentos"]

    ultima_linha = ws.max_row
    nova_linha = ultima_linha + 1

    # Copiar altura da linha
    ws.row_dimensions[nova_linha].height = \
        ws.row_dimensions[ultima_linha].height

    # Copiar todas as células
    for col in range(1, ws.max_column + 1):

        origem = ws.cell(
            row=ultima_linha,
            column=col
        )

        destino = ws.cell(
            row=nova_linha,
            column=col
        )

        # -----------------------------
        # Valor / Fórmula
        # -----------------------------

        if (
            isinstance(origem.value, str)
            and origem.value.startswith("=")
        ):

            destino.value = Translator(
                origem.value,
                origin=origem.coordinate
            ).translate_formula(
                destino.coordinate
            )

        else:

            destino.value = origem.value

        # -----------------------------
        # Estilos
        # -----------------------------

        destino.font = copy(origem.font)
        destino.fill = copy(origem.fill)
        destino.border = copy(origem.border)
        destino.alignment = copy(origem.alignment)
        destino.protection = copy(origem.protection)
        destino.number_format = origem.number_format

    # Copiar largura das colunas (opcional)
    # As larguras pertencem às colunas, por isso não é necessário.

    # -----------------------------
    # Escrever campos manuais
    # -----------------------------

    for campo in CAMPOS:

        if not campo["editavel"]:
            continue

        nome = campo["campo"]

        if nome in dados_projeto:

            ws.cell(
                row=nova_linha,
                column=campo["coluna"]
            ).value = dados_projeto[nome]

    wb.save(temp.name)

    return temp.name
