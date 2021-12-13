from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Table_Functions import Get_Dados_Tabela
from Query_Functions import Get_Dados_Consulta

def Get_Session(user, senha):
    uri = "postgresql+psycopg2://{user}:{senha}@localhost:5432/DB_Trabalho".format(user=user, senha=senha)
    engine = create_engine(uri, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, uri

def Retorna_Dados(user, senha, nome_tabela, valores_exibir, valores_filtro):
    session, uri = Get_Session(user, senha) 
    dados_tabela = Get_Dados_Tabela(session, uri, nome_tabela, valores_exibir)
    dados_consulta = Get_Dados_Consulta(session, nome_tabela, valores_filtro)
    session.close()
    return dados_tabela, dados_consulta