import sqlite3 as db
import pandas as pd

conn = db.connect('banco.db')
cursor = conn.cursor()

#cursor.execute(" create table aluno( id_aluno integer not null primary key autoincrement,nome_aluno varchar(50) not null,cpf_aluno varchar(12) not null,id_turma int not null )")

#cursor.execute("create table turma(id_turma  int primary key,qtd_alunos int)")    


conn.commit()

cursor.close()
conn.close()