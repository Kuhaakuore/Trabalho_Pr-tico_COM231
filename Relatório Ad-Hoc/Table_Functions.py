from sqlalchemy import MetaData
from Model import *

def Get_Tabela(nome):
    if nome == "equipe": return Equipe
    elif nome == "esporte": return Esporte
    elif nome == "jogador": return Jogador
    else: return Liga

def Corrige_Nome(nome):
    if nome == "Equipe": return "equipe"
    elif nome == "Esporte": return "esporte"
    elif nome == "Jogador": return "jogador"
    else: return "liga"

def Total_Registros(table, session):
    return session.query(table).count()


def Tamanho_Tabela(uri, tabela):
    m = MetaData(uri)
    e = lambda x: m.bind.execute(x).first()[0]
    m.reflect()
    q_pretty_size = "SELECT pg_size_pretty(pg_total_relation_size('trabalho.%s'))"
    return e(q_pretty_size % tabela)

def Get_Dados_Tabela(session, uri, nome, valores_exibir):
    dados = {}
    nome_tabela = Corrige_Nome(nome)
    if valores_exibir[0]: 
        dados['t_registros'] = Total_Registros(Get_Tabela(nome_tabela), session)
    else: 
        dados['t_registros'] = None
    if valores_exibir[1]: 
        dados['t_tamanho'] = Tamanho_Tabela(uri, nome_tabela)
    else: 
        dados['t_tamanho'] = None
    return dados
