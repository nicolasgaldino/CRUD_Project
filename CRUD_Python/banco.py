# Conectando ao Banco
import sqlite3 as lite

# Criando Conexão
conexao = lite.connect('vendas.db')

# Criando Tabela de Dados
with conexao:
  cursor = conexao.cursor()
  cursor.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome_cliente TEXT, email_cliente TEXT, nome_moto TEXT, valor_moto DECIMAL, data_venda TEXT)")