import streamlit as st
import openpyxl
import tempfile

from dados import CAMPOS
from excel import (
    ler_recenseamentos,
    pesquisar_projetos,
    procurar_linha_projeto,
    ler_projeto,
    guardar_projeto,
    criar_projeto
)

# -------------------------------------------------
# TÍTULO
# -------------------------------------------------

st.set_page_config(
    page_title="Gestão de Recenseamentos",
    layout="wide"
)

st.title("Gestão de Recenseamentos")


ficheiro = st.file_uploader(
    "Escolher ficheiro Excel",
    type=["xlsm"]
)

if ficheiro is None:
    st.stop()

tab_editar, tab_nova = st.tabs(
    [
        "✏️ Editar Obra",
        "➕ Nova Obra"
    ]
)

# =================================================
# EDITAR OBRA
# =================================================

with tab_editar:


    # -------------------------------------------------
    # LER LISTA DE PROJETOS
    # -------------------------------------------------

    try:

        projetos = ler_recenseamentos(ficheiro)

    except Exception as e:

        st.error(e)
        st.stop()

    st.success(
        f"{len(projetos)} projetos carregados."
    )

    # -------------------------------------------------
    # PESQUISA
    # -------------------------------------------------

    pesquisa = st.text_input(
        "Pesquisar obra"
    )

    if pesquisa.strip():

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

    if resultados.empty:
        st.warning("Nenhum projeto encontrado.")
        st.stop()

    # -------------------------------------------------
    # ESCOLHER PROJETO
    # -------------------------------------------------

    escolha = st.selectbox(

        "Projeto",

        resultados["RefObra"].astype(str)

    )

    # -------------------------------------------------
    # ABRIR EXCEL
    # -------------------------------------------------

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

    # -------------------------------------------------
    # FORMULÁRIO
    # -------------------------------------------------

    st.divider()

    st.header("Dados da Obra")

    dados = {}

    secao_atual = None

    for campo in CAMPOS:

        if not campo["editavel"]:
            continue

        if campo["secao"] != secao_atual:

            secao_atual = campo["secao"]

            st.subheader(secao_atual)

        valor = projeto.get(

            campo["campo"]

        )

        # ----------------------------
        # TEXTO
        # ----------------------------

        if campo["tipo"] == "texto":

            dados[campo["campo"]] = st.text_input(

                campo["nome"],

                value="" if valor is None else str(valor)

            )

        # ----------------------------
        # INTEIRO
        # ----------------------------

        elif campo["tipo"] == "int":

            if valor is None:
                valor = 0

            try:
                valor = int(valor)
            except:
                valor = 0

            dados[campo["campo"]] = st.number_input(

                campo["nome"],

                value=valor,

                step=1,

                format="%d"

            )

        # ----------------------------
        # DECIMAL
        # ----------------------------

        elif campo["tipo"] == "float":

            if valor is None:
                valor = 0.0

            try:
                valor = float(valor)
            except:
                valor = 0.0

            dados[campo["campo"]] = st.number_input(

                campo["nome"],

                value=valor,

                step=0.01,

                format="%.2f"

            )

        # ----------------------------
        # LISTA
        # ----------------------------

        elif campo["tipo"] == "lista":

            opcoes = campo["opcoes"]

            if valor not in opcoes:
                indice = 0
            else:
                indice = opcoes.index(valor)

            dados[campo["campo"]] = st.selectbox(

                campo["nome"],

                opcoes,

                index=indice

            )

    # -------------------------------------------------
    # GUARDAR
    # -------------------------------------------------

    st.divider()

    if st.button(
        "💾 Guardar Projeto",
        use_container_width=True
    ):

        try:

            novo_ficheiro = guardar_projeto(

                ficheiro,

                escolha,

                dados

            )

            st.success(
                "Projeto atualizado com sucesso."
            )

            with open(
                novo_ficheiro,
                "rb"
            ) as f:

                st.download_button(

                    "📥 Descarregar Excel atualizado",

                    data=f,

                    file_name="SPRD_atualizado.xlsm",

                    mime="application/vnd.ms-excel.sheet.macroEnabled.12",

                    use_container_width=True

                )

        except Exception as e:

            st.error(
                f"Erro ao guardar: {e}"
            )

# =================================================
# NOVA OBRA
# =================================================

with tab_nova:

    st.header("Nova Obra")

    dados_novos = {}

    secao_atual = None

    for campo in CAMPOS:

        if not campo["editavel"]:
            continue

        if campo["secao"] != secao_atual:

            secao_atual = campo["secao"]

            st.subheader(secao_atual)

        # ----------------------------
        # TEXTO
        # ----------------------------

        if campo["tipo"] == "texto":

            dados_novos[campo["campo"]] = st.text_input(

                campo["nome"],

                value="",

                key="novo_" + campo["campo"]

            )

        # ----------------------------
        # INTEIRO
        # ----------------------------

        elif campo["tipo"] == "int":

            dados_novos[campo["campo"]] = st.number_input(

                campo["nome"],

                value=0,

                step=1,

                format="%d",

                key="novo_" + campo["campo"]

            )

        # ----------------------------
        # FLOAT
        # ----------------------------

        elif campo["tipo"] == "float":

            dados_novos[campo["campo"]] = st.number_input(

                campo["nome"],

                value=0.0,

                step=0.01,

                format="%.2f",

                key="novo_" + campo["campo"]

            )

        # ----------------------------
        # LISTA
        # ----------------------------

        elif campo["tipo"] == "lista":

            dados_novos[campo["campo"]] = st.selectbox(

                campo["nome"],

                campo["opcoes"],

                key="novo_" + campo["campo"]

            )

    st.divider()

    if st.button(
        "➕ Criar Obra",
        use_container_width=True
    ):

        try:

            novo_ficheiro = criar_projeto(
                ficheiro,
                dados_novos
            )

            st.success("Obra criada com sucesso.")

            with open(novo_ficheiro, "rb") as f:

                st.download_button(
                    "📥 Descarregar Excel atualizado",
                    data=f,
                    file_name="SPRD_atualizado.xlsm",
                    mime="application/vnd.ms-excel.sheet.macroEnabled.12",
                    use_container_width=True
                )

        except Exception as e:

            st.error(f"Erro: {e}")
