import pandas as pd
import openpyxl
import tempfile

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
        projetos[campo["nome"]] = dados.iloc[:, campo["coluna"] - 1]

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
