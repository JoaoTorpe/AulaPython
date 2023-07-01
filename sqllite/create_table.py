import sqlite3

conn = sqlite3.connect('banco.db')

cursor = conn.cursor()


create_query_table ="""
create table clients (
id integer not null primary key autoincrement,
nome text not null,
idade integer,
cpf varchar(11) not null
);
"""


cursor.execute(create_query_table)

conn.close()
