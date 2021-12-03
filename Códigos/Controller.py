from View import View
from Modelo import Esporte, Liga, Equipe, Jogador

class Controle:
    def __init__(self):
        self.view = View()

    def inicio(self):
        opcao = self.view.inicio()
        
        while opcao != 2:
            
            # Inserção
            if opcao == 1:
                # Inserção dos dados na tabela esporte
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
                if len(status) > 0:
                    self.view.Exibe_Status('Nenhum dado novo foi cadastrado! A tabela esporte já está populada')
                else:
                    self.view.Exibe_Status('Tabela esporte populada com sucesso!')
                
                # Inserção dos dados na tabela liga
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
                if len(status) > 0:
                    self.view.Exibe_Status('Nenhum dado novo foi cadastrado! A tabela liga já está populada')
                else:
                    self.view.Exibe_Status('Tabela liga populada com sucesso!')

                # Inserção dos dados na tabela equipe
                lista_dicionarios = Equipe.Download_Data()
                for dict in lista_dicionarios:
                    dados_tratados = Equipe.Parse_Data(dict)
                    ids = dados_tratados[0]
                    nomes = dados_tratados[1]
                    paises = dados_tratados[2]
                    nomes_alternativos = dados_tratados[3]
                    esportes = dados_tratados[4]
                    anos_formacao = dados_tratados[5]
                    num_registros = len(ids)
                    for x in range(num_registros):
                        dados_equipe = [ids[x], nomes[x], paises[x], nomes_alternativos[x], esportes[x], anos_formacao[x]]
                        equipe = Equipe.Cria_Equipe(dados_equipe)
                        status = Equipe.INSERT(equipe)
                if len(status) > 0:
                    self.view.Exibe_Status('Nenhum dado novo foi cadastrado! A tabela equipe já está populada')
                else:
                    self.view.Exibe_Status('Tabela equipe populada com sucesso!')

                # Inserção dos dados na tabela jogador
                lista_dicionarios = Jogador.Download_Data()
                for dict in lista_dicionarios:
                    dados_tratados = Jogador.Parse_Data(dict)
                    ids = dados_tratados[0]
                    datas_nasc = dados_tratados[1]
                    equipes = dados_tratados[2]
                    locais_nasc = dados_tratados[3]
                    descricoes = dados_tratados[4]
                    nomes = dados_tratados[5]
                    nacionalidades = dados_tratados[6]
                    esportes = dados_tratados[7]
                    num_registros = len(ids)
                    for x in range(num_registros):
                        dados_jogador = [ids[x], datas_nasc[x], equipes[x], locais_nasc[x],
                        descricoes[x], nomes[x], nacionalidades[x], esportes[x]]
                        jogador = Jogador.Cria_Jogador(dados_jogador)
                        status = Jogador.INSERT(jogador)
                if len(status) > 0:
                    self.view.Exibe_Status('Nenhum dado novo foi cadastrado! A tabela jogador já está populada')
                else:
                    self.view.Exibe_Status('Tabela jogador populada com sucesso!')

            print()
            opcao = self.view.Main_Menu()

        print()
        print("Encerrando o programa!")

if __name__ == '__main__':
    main = Controle()
    main.inicio()