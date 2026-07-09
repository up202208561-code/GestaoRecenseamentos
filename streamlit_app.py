import streamlit as st
from dados import ESTADOS
from excel import (
    ler_recenseamentos,
    pesquisar_projetos,
    guardar_estado

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
                ESTADOS
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
