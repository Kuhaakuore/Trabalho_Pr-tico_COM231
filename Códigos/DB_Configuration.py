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
        self.dados_conexao = "host = 'localhost' dbname = 'BD_Trabalho' user = 'postgres' password = 'root'"
        return self

    def Altera_BD(self, string_sql, valores):
        # Iniciar a inserção ou atualização do registro
        conexao = None
        msg = 'Registro cadastrado com sucesso!'
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
            except Exception as err:
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
        
    def Consulta_BD(self, string_sql, valores):
        # Iniciar a consulta do registro
        conexao = None
        try:
            # Abrir conexão
            conexao = psycopg2.connect(Configuration.Set_Parametros(self).dados_conexao)
            # Abrir a sessão - a transação começa aqui
            sessao = conexao.cursor()
            # Executar a consulta
            sessao.execute(string_sql, valores)
            #Armazenar os resultados
            registros = sessao.fetchall()
            colunas = [desc[0] for desc in sessao.description]
            # Comitar no - fechar a transação
            conexao.commit()
            # Encerrar a sessão
            sessao.close()
        # Aqui nós verificamos se houve algum erro de conexão e retornamos o erro
        except psycopg2.OperationalError as e:
            return str(e)
        # Se não houver erros nós fechamos a conexão e retornamos os registros obtidos
        finally:
            if conexao is not None:
                conexao.close()
        return [colunas, registros]

    def Deleta_Pedido(self, string_sql_pedido, string_sql_informacoes_pedido, id):
        # Iniciar a consulta do registro
        conexao = None
        # Essas variáveis irão nos ajudar a identificar se os registros foram de fato eliminados
        count_order = 0
        count_order_details = 0
        try:
            # Abrir conexão
            conexao = psycopg2.connect(Configuration.Set_Parametros(self).dados_conexao)
            # Abrir a sessão - a transação começa aqui
            sessao = conexao.cursor()
            # Executar a remoção na memória RAM
            # Aqui nós primeiro eliminamos todos os dados da tabela order_details relcionados ao pedido para então eliminar o pedido
            sessao.execute(string_sql_informacoes_pedido, id)
            count_order_details = sessao.rowcount
            sessao.execute(string_sql_pedido, id)
            count_order = sessao.rowcount
            # Comitar no - fechar a transação
            conexao.commit()
            # Encerrar a sessão
            sessao.close()
        # Aqui nós verificamos se houve algum erro de conexão e retornamos o erro
        except psycopg2.OperationalError as e:
            return str(e)
        # Se não houver erros nós fechamos a conexão e retornamos os registros obtidos
        finally:
            if conexao is not None:
                conexao.close()
            return str(count_order) + ' ' + ' registros apagados com sucesso da tabela order!' + '\n' + str(count_order_details) + ' ' + ' registros apagados com sucesso da tabela order_details!'