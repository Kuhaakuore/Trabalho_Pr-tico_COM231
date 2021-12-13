import psycopg2
# import sys to get more detailed Python exception info
import sys

# import the connect library for psycopg2
from psycopg2 import connect

# import the error handling libraries for psycopg2
from psycopg2 import OperationalError, errorcodes, errors

class Configuration():
    def __init__(self, dados_conexao):
        self.dados_conexao = dados_conexao

    def Set_Parametros(self):
        self.dados_conexao = "host = 'localhost' dbname = 'DB_Trabalho' user = 'dev_teste' password = 'senha12345'"
        return self

    def Altera_BD(self, string_sql, valores):
        # Iniciar a inserção ou atualização do registro
        conexao = None
        msg = ''
        try:
            # Abrir conexão
            conexao = psycopg2.connect(Configuration.Set_Parametros(self).dados_conexao)
            # Abrir a sessão - a transação começa aqui
            sessao = conexao.cursor()
            # Executar a inserção/atualização na memória RAM
            try:
                sessao.execute(string_sql, valores)
                # Comitar a inserção/atualização - fechar a transação
                conexao.commit()
            except psycopg2.OperationalError as err:
                # pass exception to function
                conexao.rollback()
                msg = str(err)
            # Encerrar a sessão
            sessao.close()
        # Aqui nós verificamos se houve algum erro de conexão e retornamos o erro
        except psycopg2.DatabaseError as e:
            return str(e)
        # Se não houver erros nós fechamos a conexão e retornamos a mensagem de sucesso
        finally:
            if conexao is not None:
                conexao.close()
            return msg