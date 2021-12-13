import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
from tkinter.constants import CENTER, NO, RIGHT, BOTTOM, X, Y
from datetime import datetime

class Relatorio:
    def __init__(self, dados_tabela, dicionario, atributos, user, table):
        self.dados_tabela = dados_tabela
        self.dicionario = dicionario
        self.atributos = atributos
        self.usuario = user
        self.nome_tabela = table

        root = tk.Tk()
        root.title('Relatório')
        root.geometry('1000x600')

        scrollbarY = Scrollbar(root)
        scrollbarY.pack(side = RIGHT, fill = Y)

        scrollbarX = Scrollbar(root, orient='horizontal')
        scrollbarX.pack(side = BOTTOM, fill = X)

        self.txt00 = tk.Label(root, text='')
        self.txt00.pack()

        self.txt01 = tk.Label(root, text='Relatório gerado por: ' + str(self.usuario))
        self.txt01.pack()

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.txt02 = tk.Label(root, text='Data e hora da geração: ' + dt_string)
        self.txt02.pack()

        self.txt000 = tk.Label(root, text='')
        self.txt000.pack()

        if(self.dados_tabela['t_registros'] != None):
            self.txt03 = tk.Label(root, text='Total de registros na tabela: ' + str(self.dados_tabela['t_registros']))
            self.txt03.pack()
        if(self.dados_tabela['t_tamanho'] != None):
            self.txt04 = tk.Label(root, text='Tamanho em bytes da tabela: ' + str(self.dados_tabela['t_tamanho']))
            self.txt04.pack()
        self.txt0000 = tk.Label(root, text='')
        self.txt0000.pack()

        self.txt05 = tk.Label(root, text='Tabela: ' + self.nome_tabela)
        self.txt05.pack()

        self.txt00000 = tk.Label(root, text='')
        self.txt00000.pack()        

        tabela = ttk.Treeview(root, yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set)

        tabela['columns'] = [atributo for atributo in self.atributos]

        tabela.column("#0", width=0,  stretch=NO)
        for atributo in self.atributos:
            tabela.column(atributo,anchor=CENTER)
        
        tabela.heading("#0",text="",anchor=CENTER)
        for atributo in self.atributos:
            tabela.heading(atributo,text=atributo,anchor=CENTER)

        chaves = list(self.dicionario.keys())
        registros = []
        id = 0

        for i in range(len(self.dicionario[chaves[0]])):
            for chave in chaves:
                registros.append(self.dicionario[chave][i])
            tabela.insert(parent='', index='end', iid=id, text='', values=registros)
            id += 1
            registros = []

        tabela.pack(fill=Y,expand=1)

        scrollbarY.config(command = tabela.yview)
        scrollbarX.config(command = tabela.xview)

        tk.mainloop()