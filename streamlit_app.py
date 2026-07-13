import streamlit as st
import openpyxl
import tempfile
import hashlib
import os

from dados import CAMPOS
from excel import (
    ler_recenseamentos,
    pesquisar_projetos,
    procurar_linha_projeto,
    ler_projeto,
    guardar_projeto,
    criar_projeto,
    abrir_excel
)

# -------------------------------------------------
# TÍTULO
# -------------------------------------------------

st.set_page_config(
    page_title="Gestão de Recenseamentos",
    layout="wide"
)

st.title("Gestão de Recenseamentos")

if "nova_obra_id" not in st.session_state:
    st.session_state["nova_obra_id"] = 0
    
if "upload_key" not in st.session_state:
    st.session_state["upload_key"] = 0

ficheiro = st.file_uploader(
    "Escolher ficheiro Excel",
    type=["xlsm"]
)

if ficheiro is None:
    st.stop()


# Guardar Excel em memória durante a sessão

if (
    "ficheiro_temp" not in st.session_state
    or st.session_state.get("nome_ficheiro") != ficheiro.name
):

    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".xlsm"
    )

    tmp.write(ficheiro.getvalue())
    tmp.close()

    st.session_state["ficheiro_temp"] = tmp.name
    st.session_state["nome_ficheiro"] = ficheiro.name

pagina = st.radio(
    "",
    ["✏️ Editar Obra", "➕ Nova Obra"],
    horizontal=True,
    key="pagina"
)

# =================================================
# EDITAR OBRA
# =================================================

if pagina == "✏️ Editar Obra":

    # -------------------------------------------------
    # LER LISTA DE PROJETOS
    # -------------------------------------------------

    try:
        
        projetos = ler_recenseamentos(
            st.session_state["ficheiro_temp"]
        )

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

    else:

        # -------------------------------------------------
        # ESCOLHER PROJETO
        # -------------------------------------------------

        escolha = st.selectbox(
            "Projeto",
            resultados["RefObra"].astype(str).tolist()
        )

        # -------------------------------------------------
        # ABRIR EXCEL
        # -------------------------------------------------

        wb = abrir_excel(
            st.session_state["ficheiro_temp"]
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

            valor = projeto.get(campo["campo"])

            if campo["tipo"] == "texto":

                dados[campo["campo"]] = st.text_input(
                    campo["nome"],
                    value="" if valor is None else str(valor),
                    key=f"editar_{escolha}_{campo['campo']}"
                )

            elif campo["tipo"] == "int":

                try:
                    valor = int(valor or 0)
                except:
                    valor = 0

                dados[campo["campo"]] = st.number_input(
                    campo["nome"],
                    value=valor,
                    step=1,
                    format="%d",
                    key=f"editar_{escolha}_{campo['campo']}"
                )

            elif campo["tipo"] == "float":

                try:
                    valor = float(valor or 0)
                except:
                    valor = 0.0

                dados[campo["campo"]] = st.number_input(
                    campo["nome"],
                    value=valor,
                    step=0.01,
                    format="%.2f",
                    key=f"editar_{escolha}_{campo['campo']}"
                )

            elif campo["tipo"] == "lista":

                opcoes = campo["opcoes"]

                indice = opcoes.index(valor) if valor in opcoes else 0

                dados[campo["campo"]] = st.selectbox(
                    campo["nome"],
                    opcoes,
                    index=indice,
                    key=f"editar_{escolha}_{campo['campo']}"
                )

        st.divider()

        if st.button(
            "💾 Guardar Projeto",
            use_container_width=True
        ):

            try:

                novo_ficheiro = guardar_projeto(
                    st.session_state["ficheiro_temp"],
                    escolha,
                    dados
                )

                with open(st.session_state["ficheiro_temp"], "wb") as f:
                    f.write(novo_ficheiro)

                st.session_state["excel_atual"] = novo_ficheiro

                st.session_state["mensagem"] = "✅ Projeto atualizado com sucesso."

                st.session_state["upload_key"] += 1

                st.rerun()

            except Exception as e:
                st.error(f"Erro ao guardar: {e}")


# =================================================
# NOVA OBRA
# =================================================

if pagina == "➕ Nova Obra":

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
                key=f"novo_{st.session_state['nova_obra_id']}_{campo['campo']}"
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
                key=f"novo_{st.session_state['nova_obra_id']}_{campo['campo']}"
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
                key=f"novo_{st.session_state['nova_obra_id']}_{campo['campo']}"
            )

        # ----------------------------
        # LISTA
        # ----------------------------

        elif campo["tipo"] == "lista":

            dados_novos[campo["campo"]] = st.selectbox(
                campo["nome"],
                campo["opcoes"],
                key=f"novo_{st.session_state['nova_obra_id']}_{campo['campo']}"
            )

    st.divider()

    if st.button(
        "➕ Criar Obra",
        use_container_width=True
    ):

        if not dados_novos["RefObra"].strip():
            st.error("O campo 'Ref. Obra' é obrigatório.")
            st.stop()

        try:

            novo_ficheiro = criar_projeto(
                st.session_state["excel_atual"],
                dados_novos
            )

            st.session_state["excel_atual"] = novo_ficheiro

            st.session_state["mensagem"] = "✅ Obra criada com sucesso."

            st.session_state["nova_obra_id"] += 1

            st.rerun()

        except Exception as e:

            st.error(f"Erro: {e}")

st.divider()

st.download_button(
    "📥 Descarregar Excel atualizado",
    data=st.session_state["excel_atual"],
    file_name="SPRD_atualizado.xlsm",
    mime="application/vnd.ms-excel.sheet.macroEnabled.12",
    use_container_width=True
)
