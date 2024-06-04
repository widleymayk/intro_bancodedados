import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM clientes;
""")

conn.close()