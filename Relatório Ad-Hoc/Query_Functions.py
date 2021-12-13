from sqlalchemy.sql.expression import desc, asc
from Table_Functions import Get_Tabela, Corrige_Nome


def Consulta(session, nome_tabela, valores_filtros):
    nome = Corrige_Nome(nome_tabela)
    tabela = Get_Tabela(nome)

    if valores_filtros['atributo_ordenacao'][0] != None:
        if valores_filtros['limite'] != None and valores_filtros['atributo_ordenacao'][1] == 'Crescente':
            return session.query(tabela).order_by(asc(valores_filtros['atributo_ordenacao'][0])).limit(valores_filtros['limite']).all()
        
        elif valores_filtros['limite'] == None and valores_filtros['atributo_ordenacao'][1] == 'Crescente':
            return session.query(tabela).order_by(asc(valores_filtros['atributo_ordenacao'][0])).all()
        
        elif valores_filtros['limite'] != None and valores_filtros['atributo_ordenacao'][1] == 'Decrescente':
            return session.query(tabela).order_by(desc(valores_filtros['atributo_ordenacao'][0])).limit(valores_filtros['limite']).all()
        
        elif valores_filtros['limite'] == None and valores_filtros['atributo_ordenacao'][1] == 'Decrescente':
            return session.query(tabela).order_by(desc(valores_filtros['atributo_ordenacao'][0])).all()
             
    else:
        if valores_filtros['limite'] != None:
            return session.query(tabela).limit(valores_filtros['limite']).all()
        else:
            return session.query(tabela).all()

def Get_Dados_Consulta(session, nome_tabela, valores_filtros):
    dados = []
    dados = Consulta(session, nome_tabela, valores_filtros)

    return dados