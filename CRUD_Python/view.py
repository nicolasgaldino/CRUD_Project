# Conectando ao Banco
import sqlite3 as lite

# Conexão com o BD
con = lite.connect('./vendas.db')

# Inserção de Dados
def inserirDados(i):
  with con:
    cur = con.cursor()
    query = "INSERT INTO formulario (nome_cliente, email_cliente, nome_moto, valor_moto, data_venda) VALUES (?, ?, ?, ?, ?)"
    cur.execute(query, i)

# Exibição de Dados
def exibirDados():
  lista = []
  with con:
    cur = con.cursor()
    query = "SELECT * FROM formulario"
    cur.execute(query)
    info = cur.fetchall()
    for i in info:
      lista.append(i)
  return lista

# Atualização de Dados
def atualizarDados(i):
  with con:
    cur = con.cursor()
    query = "UPDATE formulario SET nome_cliente=?, email_cliente=?, nome_moto=?, valor_moto=?, data_venda=? WHERE id=?"
    cur.execute(query, i)

# Excluir Dados
def excluirDados(i):
  with con:
    cur = con.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cur.execute(query, i)