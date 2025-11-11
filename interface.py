import streamlit as st
import pandas as pd
import funcao

st.title("📋 Sistema de Cadastro de Clientes")

# --- Cadastro ---
st.header("Adicionar Cliente")
nome = st.text_input("Nome")
telefone = st.text_input("Telefone")
endereco = st.text_input("Endereço")

if st.button("Salvar Cliente"):
    try:
        funcao.inserirDados(nome, telefone, endereco)
        st.success("Cliente adicionado com sucesso!")
    except ValueError as e:
        st.error(str(e))

st.divider()

# --- Listagem e Edição ---
st.header("Clientes Cadastrados")
dados = funcao.listarDados()
if dados:
    df = pd.DataFrame(dados, columns=["ID", "Nome", "Telefone", "Endereço"])
    st.dataframe(df, use_container_width=True)

    # Seleciona cliente pelo ID
    id_selecionado = st.selectbox("Selecione o ID do cliente para editar/excluir:", df["ID"])

    cliente = df[df["ID"] == id_selecionado].iloc[0]
    nome_edit = st.text_input("Nome (editar)", cliente["Nome"])
    telefone_edit = st.text_input("Telefone (editar)", cliente["Telefone"])
    endereco_edit = st.text_input("Endereço (editar)", cliente["Endereço"])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Atualizar"):
            funcao.atualizarCliente(id_selecionado, nome_edit, telefone_edit, endereco_edit)
            st.success("Cliente atualizado com sucesso!")
            st.experimental_rerun()

    with col2:
        if st.button("🗑️ Excluir"):
            funcao.excluirCliente(id_selecionado)
            st.warning("Cliente excluído!")
            st.experimental_rerun()

else:
    st.info("Nenhum cliente cadastrado ainda.")
