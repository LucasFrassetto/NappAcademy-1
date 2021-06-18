import sqlite3
from random import randrange, uniform, choice

conn = sqlite3.connect('banco1.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE vendas (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    quantidade INTEGER,
    valor FLOAT,
    total FLOAT,
    vendido_em DATE NOT NULL
);
""")

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4']
produtos += ['Produto 5', 'Produto 6', 'Produto 7', 'Produto 8']
produtos += ['Produto 9', 'Produto 10', 'Produto 11', 'Produto 12']
datas = ['2021-03-20', '2021-03-21', '2021-03-22', '2021-03-23']
for data in datas:
    for item in range(30):
        produto = choice(produtos)
        quantidade = randrange(1, 30)
        valor = uniform(4.5, 70.5)
        sql = "INSERT INTO vendas(produto, quantidade, valor,"
        sql = sql + " total, vendido_em) VALUES ('"
        sql = sql +  produto + "', " + str(quantidade) 
        sql = sql + ", " + str(round(valor, 2))
        sql = sql + ", " + str(round(quantidade * valor , 2)) +", '" + data + "')"
        cursor.execute(sql)

conn.commit()
conn.close()
