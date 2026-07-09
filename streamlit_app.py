import streamlit as st
from dados import ESTADOS
from excel import (
    ler_recenseamentos,
    pesquisar_projetos,
    guardar_estado
)


estados = [
    "Em avaliação",
    "Pendente de Nova Decisão",
    "Anulado",
    "Em Execução",
    "Executado"
]


def ler_recenseamentos(ficheiro):

    dados = pd.read_excel(
        ficheiro,
        sheet_name="Recenseamentos",
        header=None
    )

    # MATLAB: dados(6:end,:)
    dados = dados.iloc[5:]

    projetos = pd.DataFrame()

    projetos["ID"] = dados.iloc[:, 0]
    projetos["Concelho"] = dados.iloc[:, 1]
    projetos["RefObra"] = dados.iloc[:, 2]
    projetos["Estado"] = dados.iloc[:, 3]
    projetos["Rua"] = dados.iloc[:, 4]

    projetos = projetos.dropna(
        subset=["RefObra"]
    )

    return projetos



def pesquisar_projetos(projetos, texto):

    texto = texto.lower()

    resultado = projetos[
        projetos.astype(str)
        .apply(
            lambda coluna:
            coluna.str.lower()
            .str.contains(texto, na=False)
        )
        .any(axis=1)
    ]

    return resultado



def guardar_estado(ficheiro, ref, novo_estado):

    import tempfile

    # criar ficheiro temporário
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


    for linha in range(6, ws.max_row + 1):

        referencia = ws.cell(
            linha,
            3
        ).value


        if referencia == ref:

            ws.cell(
                linha,
                4
            ).value = novo_estado

            break


    wb.save(temp.name)


    return temp.name


# --------------------------
# INTERFACE
# --------------------------

st.title(
    "Gestão de Recenseamentos"
)


ficheiro = st.file_uploader(
    "Escolher ficheiro Excel",
    type=["xlsm"]
)


if ficheiro is not None:

    try:

        projetos = ler_recenseamentos(
            ficheiro
        )

        st.success(
            f"{len(projetos)} projetos carregados."
        )


        # BARRA DE PESQUISA
        pesquisa = st.text_input(
            "Pesquisar projeto:"
        )


        if pesquisa.strip() != "":

            resultados = pesquisar_projetos(
                projetos,
                pesquisa
            )

        else:

            resultados = projetos



        st.dataframe(
            resultados,
            use_container_width=True
        )


        if len(resultados) > 0:


            escolha = st.selectbox(
                "Escolha o projeto:",
                resultados["RefObra"].astype(str)
            )


            novo_estado = st.selectbox(
                "Novo Estado:",
                estados
            )


            if st.button(
                "Guardar Estado"
            ):

                novo_ficheiro = guardar_estado(
                    ficheiro,
                    escolha,
                    novo_estado
                )


                with open(novo_ficheiro, "rb") as f:

                    st.download_button(
                        "Descarregar Excel atualizado",
                        f,
                        file_name="SPRD_atualizado.xlsm"
                    )


                st.success(
                    "Estado atualizado!"
                )

        else:

            st.warning(
                "Nenhum projeto encontrado."
            )


    except Exception as e:

        st.error(
            f"Erro ao carregar ficheiro: {e}"
        )
