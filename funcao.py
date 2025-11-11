import sqlite3
import os

def conectarBD():
    caminho = os.path.abspath("Clientes.db")
    conexao = sqlite3.connect(caminho)
    return conexao

def verificarDuplicado(nome, telefone, endereco):
    conexao = conectarBD()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT * FROM Cliente
                   WHERE nome = ? OR telefone = ? OR endereco =? 
    """, (nome, telefone, endereco))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado is not None

def inserirDados(nome, telefone, endereco):
    if verificarDuplicado(nome, telefone, endereco):
        raise ValueError("Cliente ja cadastrado (nome, telefone ou endereço duplicado).")
    
    conexao = conectarBD()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Cliente(nome, telefone, endereco) VALUES (?, ?, ?)", (nome, telefone, endereco))
    conexao.commit()
    conexao.close()

def listarDados():
    conexao = conectarBD()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Cliente")
    dados = cursor.fetchall()
    conexao.close()
    return dados

def atualizarCliente(id, nome, telefone, endereco):
    conexao = conectarBD()
    cursor = conexao.cursor()
    cursor.execute(""" 
        UPDATE Cliente
            SET nome = ?, telefone = ?, endereco = ?
                WHERE id = ?
    """, (nome, telefone, endereco, id))
    conexao.commit()
    conexao.close()


def excluirCliente(id):
    conexao = conectarBD()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Cliente WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()