import sqlite3
conexao= sqlite3.connect('festa.db')
cursor= conexao.cursor()

cursor.execute("SELECT * FROM convidados")
pessoas = cursor.fetchall()

print("\n=== LISTA DE PRESENÇA ===")

for pessoa in pessoas:
    print(f"Nome: {pessoa[0]} | Vai? {pessoa[1]} | Total: {pessoa[2]}")


conexao.close