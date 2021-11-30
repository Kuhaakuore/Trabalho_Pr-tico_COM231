# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from decimal import *
from psycopg2.extensions import AsIs
from DB_Configuration import Configuration
from parse import findall
import requests
import json
import re
import numpy as np

Base = declarative_base()
metadata = Base.metadata


class Esporte(Base):
    __tablename__ = 'esportes'
    __table_args__ = {'schema': 'trabalho'}

    id = Column(Integer, primary_key=True)
    formato = Column(String(30), nullable=False)
    nome = Column(String(20), nullable=False, unique=True)
    descricao = Column(Text, nullable=False)

    def __init__(self, idSport, strFormat, strSport, strSportDescription):
        self.id = idSport
        self.formato = strFormat
        self.nome = strSport
        self.descricao = strSportDescription

    # Função para criar um esporte
    def Cria_Esporte(dados_esporte):
        novo_esporte = Esporte(int(dados_esporte[0]), str(dados_esporte[1]), str(dados_esporte[2]), str(dados_esporte[3]))
        return novo_esporte

    # Função para inserção de novos esportes no banco
    def INSERT(esporte):
        string_sql_esporte = 'INSERT INTO trabalho.esportes(id, formato, nome, descricao) VALUES (%s, %s, %s, %s);'
        dados_esporte = Esporte.Get_Dados_Esporte(esporte)
        status = Configuration.Altera_BD(
            Configuration, string_sql_esporte, dados_esporte)
        return status

    def Download_Data():
        response = requests.get(
            "https://www.thesportsdb.com/api/v1/json/2/all_sports.php")
        json_response = response.json()
        dictionary = json.dumps(json_response, sort_keys=True)
        return dictionary

    def Parse_Data(dados_api):
        aux = []
        for r in findall('"idSport": "{}", ', dados_api):
            aux.append(r[0])
        ids = np.array(aux)

        aux = []
        for r in findall('"strFormat": "{}", ', dados_api):
            aux.append(r[0])
        formatos = np.array(aux)

        aux = []
        for r in findall('"strSport": "{}", ', dados_api):
            aux.append(r[0])
        nomes = np.array(aux)

        aux = []
        for r in findall('"strSportDescription": "{}", ', dados_api):
            aux.append(r[0])
        descricoes = np.array(aux)

        lista_dados = [ids, formatos, nomes, descricoes]
        return lista_dados

    def Get_Dados_Esporte(self):
        dados = [self.id, self.formato, self.nome, self.descricao]
        return dados


class Liga(Base):
    __tablename__ = 'liga'
    __table_args__ = {'schema': 'trabalho'}

    id = Column(Integer, primary_key=True)
    nome = Column(String(20), nullable=False)
    nome_esporte = Column(ForeignKey('trabalho.esportes.nome'), nullable=False)
    country = Column(String(20), nullable=False)

    esporte = relationship('Esporte')
