import streamlit as st
import pandas as pd
import funcao

st.set_page_config(page_title="Sistema de Clientes", layout="centered")

# --- Controle de páginas ---
menu = st.sidebar.radio("Navegar", ["🏠 Início", "➕ Cadastrar", "📋 Listar / Editar"])

if menu == "🏠 Início":
    st.title("Sistema de Cadastro de Clientes")
    st.write("Bem-vindo! Use o menu à esquerda para navegar.")

elif menu == "➕ Cadastrar":
    st.title("Cadastrar Cliente")
    nome = st.text_input("Nome")
    telefone = st.text_input("Telefone")
    endereco = st.text_input("Endereço")

    if st.button("Salvar Cliente"):
        try:
            funcao.inserirDados(nome, telefone, endereco)
            st.success("Cliente adicionado com sucesso!")
        except ValueError as e:
            st.error(str(e))

elif menu == "📋 Listar / Editar":
    st.title("Clientes Cadastrados")
    dados = funcao.listarDados()
    if not dados:
        st.info("Nenhum cliente cadastrado ainda.")
    else:
        df = pd.DataFrame(dados, columns=["ID", "Nome", "Telefone", "Endereço"])
        st.dataframe(df, use_container_width=True)

        id_sel = st.selectbox("Selecione o ID do cliente:", df["ID"])
        cliente = df[df["ID"] == id_sel].iloc[0]

        nome = st.text_input("Nome", cliente["Nome"])
        telefone = st.text_input("Telefone", cliente["Telefone"])
        endereco = st.text_input("Endereço", cliente["Endereço"])

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Atualizar"):
                funcao.atualizarCliente(id_sel, nome, telefone, endereco)
                st.success("Cliente atualizado!")
                st.rerun()

        with col2:
            if st.button("Excluir"):
                funcao.excluirCliente(id_sel)
                st.warning("Cliente excluído!")
                st.experimental_rerun()
