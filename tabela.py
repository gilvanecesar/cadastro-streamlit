import sqlite3

conexao = sqlite3.connect("Clientes.db")

cursor = conexao.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS Clientes(
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Telefone TEXT NOT NULL,
            Endereco TEXT NOT NULL

        );
    """
)
conexao.commit()
cursor.close()
conexao.close()

print("Tabela criada com sucesso")