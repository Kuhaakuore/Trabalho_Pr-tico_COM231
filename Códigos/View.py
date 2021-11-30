# Nome: Wesley da Silva Ribeiro
# Matrícula: 2019006307

from decimal import *
from datetime import datetime

class View():
    def inicio(self):
        return self.Main_Menu()

    def Main_Menu(self):
        print("MENU")
        print("1. Cadastrar esportes")
        print("2. Cadastrar ligas")
        print("3. Cadastrar times")
        print("4. Cadastrar jogadores")
        print("5. Sair")
        option = int(input("Escolha uma das opções acima: "))
        return option

    def Exibe_Status(self, status):
        print("\n" + status)