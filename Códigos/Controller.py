# Nome: Wesley da Silva Ribeiro
# Matrícula: 2019006307

from View import View
from Modelo import Esporte, Liga, Time, Jogador

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
                    esporte = Esporte.Cria_Esporte(dados_esporte)
                    status = Esporte.INSERT(esporte)
                self.view.Exibe_Status(status)

            if opcao == 2:
                
                dados_api = Liga.Download_Data()
                dados_tratados = Liga.Parse_Data(dados_api)
                ids = dados_tratados[0]
                nomes = dados_tratados[1]
                esportes = dados_tratados[2]
                num_registros = len(ids)
                for x in range(num_registros):
                    dados_liga = [ids[x], nomes[x], esportes[x]]
                    liga = Liga.Cria_Liga(dados_liga)
                    status = Liga.INSERT(liga)
                    if status != 'Registro cadastrado com sucesso!':
                        self.view.Exibe_Status(status)
                self.view.Exibe_Status(status)

            if opcao == 3:
                lista_dicionarios = Time.Download_Data()
                for dict in lista_dicionarios:
                    dados_tratados = Time.Parse_Data(dict)
                    ids = dados_tratados[0]
                    nomes = dados_tratados[1]
                    paises = dados_tratados[2]
                    nomes_alternativos = dados_tratados[3]
                    esportes = dados_tratados[4]
                    anos_formacao = dados_tratados[5]
                    num_registros = len(ids)
                    for x in range(num_registros):
                        dados_time = [ids[x], nomes[x], paises[x], nomes_alternativos[x], esportes[x], anos_formacao[x]]
                        time = Time.Cria_Time(dados_time)
                        status = Time.INSERT(time)
                        if status != 'Registro cadastrado com sucesso!':
                            self.view.Exibe_Status(status)
                self.view.Exibe_Status(status)

            if opcao == 4:
                lista_dicionarios = Jogador.Download_Data()
                for dict in lista_dicionarios:
                    dados_tratados = Jogador.Parse_Data(dict)
                    ids = dados_tratados[0]
                    datas_nasc = dados_tratados[1]
                    times = dados_tratados[2]
                    locais_nasc = dados_tratados[3]
                    descricoes = dados_tratados[4]
                    nomes = dados_tratados[5]
                    nacionalidades = dados_tratados[6]
                    esportes = dados_tratados[7]
                    num_registros = len(ids)
                    for x in range(num_registros):
                        dados_jogador = [ids[x], datas_nasc[x], times[x], locais_nasc[x],
                        descricoes[x], nomes[x], nacionalidades[x], esportes[x]]
                        jogador = Jogador.Cria_Jogador(dados_jogador)
                        status = Jogador.INSERT(jogador)
                        if status != 'Registro cadastrado com sucesso!':
                            self.view.Exibe_Status(status)
                self.view.Exibe_Status(status)

            print()
            opcao = self.view.Main_Menu()

        print()
        print("Encerrando o programa!")

if __name__ == '__main__':
    main = Controle()
    main.inicio()