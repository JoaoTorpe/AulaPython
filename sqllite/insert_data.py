import sqlite3

conn = sqlite3.connect("banco.db")

cursor = conn.cursor()


# criando uma lista de dados
lista = [(
    'Fabio', 23, '44444444444'),
    ('Joao', 21, '55555555555'),
    ('Xavier', 24, '66666666666')]

# inserindo dados na tabela
cursor.executemany("""
INSERT INTO clients (nome, idade, cpf)
VALUES (?,?,?)
""", lista)

print("Codigo executado")

conn.commit()
conn.close()