# Nome: Wesley da Silva Ribeiro
# Matrícula: 2019006307

from View import View
from Trabalho_Modelo import Esporte

class Controle:
    def __init__(self):
        self.view = View()

    def inicio(self):
        opcao = self.view.inicio()
        
        while opcao != 5:
            
            # Inserção
            if opcao == 1:
                
                dados_api = Esporte.Download_Data()
                dados_tratados = Esporte.Parse_Data(dados_api)
                ids = dados_tratados[0]
                formatos = dados_tratados[1]
                nomes = dados_tratados[2]
                descricoes = dados_tratados[3]
                num_registros = len(ids)
                for x in range(num_registros):
                    dados_esporte = [ids[x], formatos[x], nomes[x], descricoes[x]]
                    print(dados_esporte)
                    esporte = Esporte.Cria_Esporte(dados_esporte)
                    status = Esporte.INSERT(esporte)
                self.view.Exibe_Status(status)
            print()
            opcao = self.view.Main_Menu()

        print()
        print("Encerrando o programa!")

if __name__ == '__main__':
    main = Controle()
    main.inicio()