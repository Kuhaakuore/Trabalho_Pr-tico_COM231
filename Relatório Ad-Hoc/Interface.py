import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from DB_Configuration import Retorna_Dados
from Report import Relatorio

class Interface:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Relatório Ad-Hoc')
        self.janela.geometry('700x340')
    
        self.frame_Esquerdo = tk.Frame(self.janela)
        self.frame_Direito = tk.Frame(self.janela)
  
        self.myVar1 = tk.IntVar()
        self.myVar2 = tk.IntVar()
        self.myVar3 = tk.IntVar()
        self.myVar4 = tk.IntVar()
        self.myVar5 = tk.IntVar()
        self.myVar6 = tk.IntVar()
        self.box1 = tk.StringVar()
        self.box1.trace('w', self.Update)
        self.box2 = tk.StringVar()
        
        self.myVar1.set(0)
        self.myVar2.set(0)
        self.myVar3.set(0)
        self.myVar4.set(0)
        self.myVar5.set(0)
        self.myVar6.set(0)

        self.listaAtributos = []
        self.lista_ordenacao = []
       
        # frame_Esquerdo
        self.txtUser = tk.Label(self.frame_Esquerdo, text='Usuário: ')
        self.txtUser.grid(column=0, row=0, sticky='')
        self.inputUser = tk.Entry(self.frame_Esquerdo, width=15)
        self.inputUser.grid(column=1, row=0, sticky='W')

        self.txtSenha = tk.Label(self.frame_Esquerdo, text='Senha: ')
        self.txtSenha.grid(column=0, row=1, sticky='')
        self.inputSenha = tk.Entry(self.frame_Esquerdo, show= '*', width=15)
        self.inputSenha.grid(column=1, row=1, sticky='W')

        self.txt000 = tk.Label(self.frame_Esquerdo, text=' ')
        self.txt000.grid(column=0, row=2)

        self.txt01 = tk.Label(self.frame_Esquerdo, text='Selecione a tabela: ')
        self.txt01.grid(column=0, row=3)

        self.combobox1 = ttk.Combobox(self.frame_Esquerdo, textvariable=self.box1)
        self.combobox1.grid(column=1, row=3, sticky='W')
        self.combobox1['values'] = ['Equipe', 'Esporte', 'Jogador', 'Liga']

        self.txt002 = tk.Label(self.frame_Esquerdo, text=' ')
        self.txt002.grid(column=0, row=4)

        self.txt01 = tk.Label(self.frame_Esquerdo, text='Campos disponíveis: ')
        self.txt01.grid(column=0, row=5)

        self.txt01 = tk.Label(self.frame_Esquerdo, text='Campos selecionados: ')
        self.txt01.grid(column=1, row=5)

        self.listbox = tk.Listbox(self.frame_Esquerdo, width=28)
        self.listbox.grid(column=0, row=6)

        self.listbox2 = tk.Listbox(self.frame_Esquerdo, width=28)
        self.listbox2.grid(column=1, row=6)

        self.buttonInserir = tk.Button(self.frame_Esquerdo, text="Selecionar")
        self.buttonInserir.grid(column=0, row=7, sticky='W')
        self.buttonInserir.bind("<Button>", self.Insere_Atributo)

        self.buttonInserir = tk.Button(self.frame_Esquerdo, text="Selecionar Todos")
        self.buttonInserir.grid(column=0, row=7, sticky='E')
        self.buttonInserir.bind("<Button>", self.Insere_Todos_Atributos)

        self.buttonTirar = tk.Button(self.frame_Esquerdo, text="Remover")
        self.buttonTirar.grid(column=1, row=7, sticky='W', padx=5)
        self.buttonTirar.bind("<Button>", self.Remove_Atributo)

        self.buttonTirar = tk.Button(self.frame_Esquerdo, text="Remover Todos")
        self.buttonTirar.grid(column=1, row=7, sticky='E')
        self.buttonTirar.bind("<Button>", self.Remove_Todos_Atributos)        

        # frame_Direito
        self.txt1 = tk.Label(self.frame_Direito, text='Filtros: ')
        self.txt1.grid(column=1, row=0, sticky='W')

        self.cb2 = tk.Checkbutton(self.frame_Direito, text='Número de linhas: ', variable=self.myVar2, command=self.Handle_Limite)
        self.cb2.grid(column=1, row=2, sticky='')

        self.inputData1 = tk.Entry(self.frame_Direito, width=15, state='disabled')
        self.inputData1.grid(column=2, row=2, sticky='W')

        self.txt00 = tk.Label(self.frame_Direito, text=' ')
        self.txt00.grid(column=0, row=3, sticky='W')

        self.txt4 = tk.Label(self.frame_Direito, text='Ordenar por: ')
        self.txt4.grid(column=1, row=6, sticky='W')

        self.combobox2 = ttk.Combobox(self.frame_Direito, textvariable=self.box2)
        self.combobox2.grid(column=2, row=6, sticky='W')

        self.cb3 = tk.Checkbutton(self.frame_Direito, text='Crescente ', variable=self.myVar3, command=self.Handle_Ordem_Cresc)
        self.cb3.grid(column=2, row=7, sticky='W')

        self.cb4 = tk.Checkbutton(self.frame_Direito, text='Decrescente ', variable=self.myVar4, command=self.Handle_Ordem_Decresc)
        self.cb4.grid(column=2, row=8, sticky='W')

        self.txt001 = tk.Label(self.frame_Direito, text=' ')
        self.txt001.grid(column=1, row=9)

        self.cb3 = tk.Checkbutton(self.frame_Direito, text='Total de registros na tabela', variable=self.myVar5)
        self.cb3.grid(column=1, row=10, sticky='W')    

        self.cb3 = tk.Checkbutton(self.frame_Direito, text='Tamanho em bytes da tabela', variable=self.myVar6)
        self.cb3.grid(column=1, row=11, sticky='W')   

        self.txt001 = tk.Label(self.frame_Direito, text=' ')
        self.txt001.grid(column=1, row=12)

        self.buttonGerar = tk.Button(self.frame_Direito, text="Gerar Relatório", command=self.Gerar_Relatorio)
        self.buttonGerar.grid(column=1, row=13, sticky='', ipady=3)

        self.buttonLimpar = tk.Button(self.frame_Direito, text="Limpar Campos", command=self.Limpar_Campos)
        self.buttonLimpar.grid(column=2, row=13, sticky='', ipady=4)

        # Empacota os frames
        self.frame_Esquerdo.grid(column=0, row=0)
        self.frame_Direito.grid(column=1, row=0)
        
        # Inicia o mainloop
        tk.mainloop()

    def Update(self, var, indx, mode):
        self.listbox.delete(0, tk.END)
        self.listbox2.delete(0, tk.END)
        tabelaSel = self.box1.get()
        if(tabelaSel == 'Equipe'):
           self.listaAtributos = ['id_equipe', 'nome', 'pais', 'esporte', 'ano_formacao']
        else:
           self.myVar1.set(0)
           self.inputData1.delete(0, tk.END)
        if(tabelaSel == 'Esporte'):
           self.listaAtributos = ['id_esporte', 'formato', 'nome', 'descricao']
        elif(tabelaSel == 'Jogador'):
           self.listaAtributos = ['id_jogador', 'data_nasc', 'id_equipe', 'local_nasc', 'descricao', 'nome', 'nacionalidade', 'esporte']
        elif(tabelaSel == 'Liga'):
           self.listaAtributos = ['id_liga', 'nome', 'nome_esporte']
        for titulo in self.listaAtributos:
           self.listbox.insert(tk.END, titulo)

    def Handle_Ordem_Cresc(self):
        if self.myVar3.get() == 1:
            self.myVar4.set(0)

    def Handle_Ordem_Decresc(self):
        if self.myVar4.get() == 1:
            self.myVar3.set(0)

    def Handle_Limite(self):
        if self.myVar2.get() == 0:
            self.inputData1.delete(0, tk.END)
            self.inputData1.config(state='disabled')        
        else:
            self.inputData1.config(state='normal')

    def Insere_Atributo(self, event):
        atributoSel = self.listbox.get(tk.ACTIVE)
        self.listbox.delete(tk.ACTIVE)
        self.Insere_Atributo_Listbox2(atributoSel)
        self.lista_ordenacao.append(atributoSel)
        self.combobox2['values'] = self.lista_ordenacao

    def Insere_Todos_Atributos(self, event):
        listbox_size = self.listbox.size()
        if listbox_size > 0:
            for i in range(listbox_size):
                atributo = self.listbox.get(0)
                self.listbox.delete(0)
                self.Insere_Atributo_Listbox2(atributo)
                self.lista_ordenacao.append(atributo)
                self.combobox2['values'] = self.lista_ordenacao

    def Insere_Atributo_Listbox2(self, atributo):
        self.listbox2.insert(tk.END, atributo)

    def insereComboBox2(self, atributo):
        self.combobox2.insert(tk.END, atributo)

    def Remove_Atributo(self, event):
        atributoSel = self.listbox2.get(tk.ACTIVE)
        self.listbox2.delete(tk.ACTIVE)
        self.lista_ordenacao.remove(atributoSel)
        if self.combobox2.get() == atributoSel:
            self.combobox2.delete(0, tk.END)
            self.combobox2['values'] = self.lista_ordenacao
        else:
            self.combobox2['values'] = self.lista_ordenacao
        self.Insere_Atributo_Listbox(atributoSel)

    def Remove_Todos_Atributos(self, event):
        listbox_size = self.listbox2.size()
        if (listbox_size > 0):
            for i in range(listbox_size):
                atributo = self.listbox2.get(0)
                self.listbox2.delete(0)
                self.Insere_Atributo_Listbox(atributo)
                self.lista_ordenacao.remove(atributo)
                self.combobox2.delete(0, tk.END)
                self.combobox2['values'] = self.lista_ordenacao

    def Insere_Atributo_Listbox(self, atributo):
        self.listbox.insert(tk.END, atributo)

    def Limpar_Campos(self):
        self.myVar1.set(0)
        self.myVar2.set(0)
        self.myVar3.set(0)
        self.myVar4.set(0)
        self.myVar5.set(0)
        self.myVar6.set(0)
        self.inputData1.delete(0, tk.END)
        self.inputData1.config(state='disabled')
        self.inputUser.delete(0, tk.END)
        self.inputSenha.delete(0, tk.END)
        self.box1.set('')
        self.listbox.delete(0, tk.END)
        self.listbox2.delete(0, tk.END)
        self.combobox2.delete(0, tk.END)
        self.lista_ordenacao.clear()
        self.combobox2['values'] = self.lista_ordenacao

    def Gerar_Relatorio(self):
        tabela = self.combobox1.get()
        user = self.inputUser.get()
        senha = self.inputSenha.get()
        atributos = list(self.listbox2.get(0, tk.END))
        limite_linhas = self.myVar2.get()
        flag = 0
        valor = self.inputData1.get()
        if limite_linhas:
            try:
                int(valor) <= 0
            except ValueError as ve:
                messagebox.showerror('ERRO!', 'O número de linhas precisa ser um número natural maior do que zero!')
                flag = 1
                return
        if(tabela == '' or user == '' or senha == '' or len(atributos) <= 0 or (limite_linhas == 1 and flag == 0 and int(valor) <= 0)):
            if(tabela == ''):
                messagebox.showerror('ERRO!', 'Selecione uma tabela!')
            elif(user == ''):
                messagebox.showerror('ERRO!', 'Forneça o nome do usuário!')
            elif(senha == ''):
                messagebox.showerror('ERRO!', 'Forneça a senha do usuário!')
            elif(len(atributos) <= 0):
                messagebox.showerror('ERRO!', 'Selecione pelo menos um atributo!')
            elif(limite_linhas == 1 and flag == 0 and int(valor) <= 0):
                messagebox.showerror('ERRO!', 'O número de linhas precisa ser um número natural maior do que zero!')
        else:
            self.dicFiltro = {}
            self.listaExibir = []

            if(self.combobox2.get() != '' and self.myVar3.get() == 1):
                self.dicFiltro['atributo_ordenacao'] = [self.combobox2.get(), 'Crescente']
            elif(self.combobox2.get() != '' and self.myVar4.get() == 1):
                self.dicFiltro['atributo_ordenacao'] = [self.combobox2.get(), 'Decrescente']
            elif(self.combobox2.get() != '' and self.myVar4.get() == 0 and self.myVar3.get() == 0):
                self.dicFiltro['atributo_ordenacao'] = [self.combobox2.get(), 'Crescente']
            else:
                self.dicFiltro['atributo_ordenacao'] = [None, None]

            if(self.myVar2.get() == 1):
                self.dicFiltro['limite'] = self.inputData1.get()
            else:
                self.dicFiltro['limite'] = None

            self.listaExibir.append(self.myVar5.get())
            self.listaExibir.append(self.myVar6.get())

            dados_tabela, dados_consulta = Retorna_Dados(user, senha, tabela, self.listaExibir, self.dicFiltro)
            dicionario = dict()

            for atributo in atributos:
                dicionario[atributo] = []
                for registro in dados_consulta:
                    dicionario[atributo].append(getattr(registro, atributo))
            self.Limpar_Campos()
            Relatorio(dados_tabela, dicionario, atributos, user, tabela)
    
def main():
    Interface()

if __name__ == '__main__': main()