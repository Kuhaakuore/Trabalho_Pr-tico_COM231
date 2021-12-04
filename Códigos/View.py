# Grupo: 
#Wesley da Silva Ribeiro(2019006307)
#João Vitor de Faria(2019006030)
#Daniel Henrique Ferreira Carvalho(2019005426)


from decimal import *
from datetime import datetime

class View():
    def inicio(self):
        return self.Main_Menu()

    def Main_Menu(self):
        print("MENU")
        print("1. Dar carga no banco")
        print("2. Sair")
        option = int(input("Escolha uma das opções acima: "))
        return option

    def Exibe_Status(self, status):
        print("\n" + status)
