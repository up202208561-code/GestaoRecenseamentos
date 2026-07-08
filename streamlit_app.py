import streamlit as st
import pandas as pd
import openpyxl


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

    projetos["ID"] = dados.iloc[:,0]
    projetos["Concelho"] = dados.iloc[:,1]
    projetos["RefObra"] = dados.iloc[:,2]
    projetos["Estado"] = dados.iloc[:,3]
    projetos["Rua"] = dados.iloc[:,4]


    projetos = projetos.dropna(
        subset=["RefObra"]
    )

    return projetos



def pesquisar_projetos(projetos,texto):

    texto = texto.lower()

    resultado = projetos[
        projetos["RefObra"]
        .astype(str)
        .str.lower()
        .str.contains(texto)

        |

        projetos["Rua"]
        .astype(str)
        .str.lower()
        .str.contains(texto)

        |

        projetos["Concelho"]
        .astype(str)
        .str.lower()
        .str.contains(texto)

        |

        projetos["Estado"]
        .astype(str)
        .str.lower()
        .str.contains(texto)
    ]

    return resultado



def guardar_estado(ficheiro,ref,novo_estado):

    wb = openpyxl.load_workbook(
        ficheiro,
        keep_vba=True
    )

    ws = wb["Recenseamentos"]


    for linha in range(6,ws.max_row+1):

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


    wb.save(ficheiro)



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


if ficheiro:


    projetos = ler_recenseamentos(
        ficheiro
    )


    pesquisa = st.text_input(
        "Pesquisar:"
    )


    if pesquisa:

        resultados = pesquisar_projetos(
            projetos,
            pesquisa
        )

    else:

        resultados = projetos



    st.dataframe(
        resultados
    )


    if len(resultados)>0:


        escolha = st.selectbox(
            "Escolha o projeto:",
            resultados["RefObra"]
        )


        novo_estado = st.selectbox(
            "Novo Estado:",
            estados
        )


        if st.button(
            "Guardar Estado"
        ):

            guardar_estado(
                ficheiro,
                escolha,
                novo_estado
            )


            st.success(
                "Estado atualizado!"
            )
