# Importando biblioteca TKinter
from cgitb import text
from glob import glob
from operator import index
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Importando Dados
from view import *

# Esquema de cores
cor0 = "#f0f3f5"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#4fa882"  # verde
cor3 = "#38576b"  # valor
cor4 = "#403d3d"   # letra
cor5 = "#e06636"   # - profit
cor6 = "#038cfc"   # azul
cor7 = "#ef5350"   # vermelha
cor8 = "#263238"   # + verde
cor9 = "#e9edf5"   # sky blue

# Janela TKinter
janela = Tk()
janela.title('')
janela.geometry('1043x453')
janela.configure(background=cor9)
janela.resizable(width=False, height=False)

# Divisão do Espaço
quadCima = Frame(janela, width=310, height=50, background=cor2, relief='flat')
quadCima.grid(row=0, column=0)

quadBaixo = Frame(janela, width=310, height=403, background=cor1, relief='flat')
quadBaixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

quadLateral = Frame(janela, width=588, height=403, background=cor1, relief='flat')
quadLateral.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Label quadCima
labelCima = Label(quadCima, text='Cadastro de Clientes', anchor=NW, font=('Ivy 13 bold'), background=cor2, fg=cor1, relief='flat')
labelCima.place(x=10, y=20)

# Variável Global TREE
global tree

# Função de Inserção
def inserir():
  nomeCliente = e_nome.get()
  emailCliente = e_email.get()
  nomeMoto = e_nomeMoto.get()
  valorMoto = e_valorMoto.get()
  dataVenda = e_dataVenda.get()

  lista = [nomeCliente, emailCliente, nomeMoto, valorMoto, dataVenda]
  if nomeCliente == '':
    messagebox.showerror('Erro! Preencha o campo "Nome".')
  else:
    inserirDados(lista)
    messagebox.showinfo('Cliente cadastrado com sucesso.')
    e_nome.delete(0, 'end')
    e_email.delete(0, 'end')
    e_nomeMoto.delete(0, 'end')
    e_valorMoto.delete(0, 'end')
    e_dataVenda.delete(0, 'end')
  mostrarTabela()

# Função de Atualização
def atualizar():
  try:
    treeDados = tree.focus()
    treeDicionario = tree.item(treeDados)
    treeLista = treeDicionario['values']

    valorId = treeLista[0]

    e_nome.delete(0, 'end')
    e_email.delete(0, 'end')
    e_nomeMoto.delete(0, 'end')
    e_valorMoto.delete(0, 'end')
    e_dataVenda.delete(0, 'end')

    e_nome.insert(0, treeLista[1])
    e_email.insert(0, treeLista[2])
    e_nomeMoto.insert(0, treeLista[3])
    e_valorMoto.insert(0, treeLista[4])
    e_dataVenda.insert(0, treeLista[5])
    def confirmar():
      nomeCliente = e_nome.get()
      emailCliente = e_email.get()
      nomeMoto = e_nomeMoto.get()
      valorMoto = e_valorMoto.get()
      dataVenda = e_dataVenda.get()

      lista = [nomeCliente, emailCliente, nomeMoto, valorMoto, dataVenda, valorId]
      if nomeCliente == '':
        messagebox.showerror('Erro! Preencha o campo "Nome".')
      else:
        atualizarDados(lista)
        messagebox.showinfo('Dados atualizados com sucesso.')
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_nomeMoto.delete(0, 'end')
        e_valorMoto.delete(0, 'end')
        e_dataVenda.delete(0, 'end')
      mostrarTabela()

    btnConfirmar = Button(quadBaixo, text='Confirmar', command=confirmar, width=10, font=('Ivy 9 bold'), background=cor6, fg=cor1, relief='raised', overrelief='ridge')
    btnConfirmar.place(x=105, y=350)

  except IndexError:
    messagebox.showerror('Selecione um dos dados na Tabela.')

# Função de Deletar
def deletar():
  try:
    treeDados = tree.focus()
    treeDicionario = tree.item(treeDados)
    treeLista = treeDicionario['values']

    valorId = [treeLista[0]]

    excluirDados(valorId)
    messagebox.showinfo('Dados excluídos com sucesso.')

    mostrarTabela()

  except IndexError:
    messagebox.showerror('Sleciona um dos dados na Tabela.')

# Label quadBaixo

# Nome do Cliente
l_nome = Label(quadBaixo, text='Nome do Cliente', anchor=NW, font=('Ivy 10 bold'), background=cor1, fg=cor4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(quadBaixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)

# Email do Cliente
l_email = Label(quadBaixo, text='Email do Cliente', anchor=NW, font=('Ivy 10 bold'), background=cor1, fg=cor4, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(quadBaixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

# Nome da Moto
l_nomeMoto = Label(quadBaixo, text='Nome da Moto', anchor=NW, font=('Ivy 10 bold'), background=cor1, fg=cor4, relief='flat')
l_nomeMoto.place(x=10, y=130)
e_nomeMoto = Entry(quadBaixo, width=45, justify='left', relief='solid')
e_nomeMoto.place(x=15, y=160)

# Valor da Moto
l_valorMoto = Label(quadBaixo, text='Valor da Moto', anchor=NW, font=('Ivy 10 bold'), background=cor1, fg=cor4, relief='flat')
l_valorMoto.place(x=10, y=190)
e_valorMoto = Entry(quadBaixo, width=45, justify='left', relief='solid')
e_valorMoto.place(x=15, y=220)

# Data da Venda
l_dataVenda = Label(quadBaixo, text='Data da Venda (dd/mm/aa)', anchor=NW, font=('Ivy 10 bold'), background=cor1, fg=cor4, relief='flat')
l_dataVenda.place(x=10, y=250)
e_dataVenda = Entry(quadBaixo, width=15, justify='left', relief='solid')
e_dataVenda.place(x=15, y=280)

# Botões

# Inserir
btnInserir = Button(quadBaixo, command=inserir, text='Inserir', width=10, font=('Ivy 9 bold'), background=cor2, fg=cor1, relief='raised', overrelief='ridge')
btnInserir.place(x=15, y=330)

# Editar
btnEditar = Button(quadBaixo, command=atualizar, text='Editar', width=10, font=('Ivy 9 bold'), background=cor6, fg=cor1, relief='raised', overrelief='ridge')
btnEditar.place(x=105, y=330)

# Excluir
btnExcluir = Button(quadBaixo, command=deletar, text='Excluir', width=10, font=('Ivy 9 bold'), background=cor7, fg=cor1, relief='raised', overrelief='ridge')
btnExcluir.place(x=195, y=330)

# Tabela à direita

def mostrarTabela():

  global tree

  lista = exibirDados()

  # Cabeçalho

  cabecalho = ['ID','Nome do Cliente', 'Email', 'Nome da Moto', 'Valor da Moto', 'Data da Venda']

  # Criação da tabela
  tree = ttk.Treeview(quadLateral, selectmode="extended", columns=cabecalho, show="headings")

  # Scroll vertical
  vsb = ttk.Scrollbar(quadLateral, orient="vertical", command=tree.yview)

  # Scroll horizontal
  hsb = ttk.Scrollbar( quadLateral, orient="horizontal", command=tree.xview)

  # Aplicações finais à tabela

  tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
  tree.grid(column=0, row=0, sticky='nsew')
  vsb.grid(column=1, row=0, sticky='ns')
  hsb.grid(column=0, row=1, sticky='ew')

  quadLateral.grid_rowconfigure(0, weight=12)

  hd=["nw", "nw", "nw", "nw", "nw", "center"]
  h=[50, 170, 160, 100, 110, 120]
  n=0

  for col in cabecalho:
      tree.heading(col, text=col.title(), anchor=CENTER)
      # Ajusta a coluna de acordo com o valor do cabeçalho
      tree.column(col, width=h[n],anchor=hd[n])
      
      n+=1

  for item in lista:
      tree.insert('', 'end', values=item)
mostrarTabela()

janela.mainloop()