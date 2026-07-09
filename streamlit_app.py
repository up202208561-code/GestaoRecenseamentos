import streamlit as st
import openpyxl
import tempfile

from dados import ESTADOS
from excel import (
    ler_recenseamentos,
    pesquisar_projetos,
    guardar_estado,
    procurar_linha_projeto,
    ler_projeto,
    guardar_projeto
)

# --------------------------
# INTERFACE
# --------------------------

st.title("Gestão de Recenseamentos")

ficheiro = st.file_uploader(
    "Escolher ficheiro Excel",
    type=["xlsm"]
)

if ficheiro is not None:

    try:

        projetos = ler_recenseamentos(ficheiro)

        st.success(
            f"{len(projetos)} projetos carregados."
        )

        # --------------------------
        # Pesquisa
        # --------------------------

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

            # --------------------------
            # Abrir Excel
            # --------------------------

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
                escolha
            )

            projeto = ler_projeto(
                ws,
                linha
            )

            # --------------------------
            # Dados da obra
            # --------------------------

            st.subheader("Dados da Obra")

            concelho = st.text_input(
                "Concelho",
                value=projeto["Concelho"]
            )

            estado = st.selectbox(
                "Estado",
                ESTADOS,
                index=ESTADOS.index(projeto["Estado"])
                if projeto["Estado"] in ESTADOS else 0
            )

            rua = st.text_input(
                "Rua",
                value=projeto["Rua"]
            )

            numero = st.text_input(
                "Nº Polícia",
                value=projeto["NumeroPolicia"]
                if projeto["NumeroPolicia"] is not None
                else ""
            )

            # --------------------------
            # Alterar estado (funcionalidade atual)
            # --------------------------

            if st.button("Guardar Projeto"):

    dados = {

        "Concelho": concelho,
        "Estado": estado,
        "Rua": rua,
        "NumeroPolicia": numero

    }

    novo_ficheiro = guardar_projeto(
        ficheiro,
        escolha,
        dados
    )

    with open(novo_ficheiro, "rb") as f:

        st.download_button(
            "Descarregar Excel atualizado",
            f,
            file_name="SPRD_atualizado.xlsm"
        )

    st.success("Projeto atualizado com sucesso.")

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
