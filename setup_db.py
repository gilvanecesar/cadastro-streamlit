import sqlite3
import os

def criar_banco():
    caminho = os.path.abspath("Clientes.db")
    print("Criando banco em:", caminho)
    
    conexao = sqlite3.connect(caminho)
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()
    print("Tabela 'Cliente' criada com sucesso.")

if __name__ == "__main__":
    criar_banco()
