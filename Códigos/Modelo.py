# coding: utf-8
from datetime import date, datetime
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
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
    __tablename__ = 'esporte'
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
        string_sql_esporte = 'INSERT INTO trabalho.esporte(id, formato, nome, descricao) VALUES (%s, %s, %s, %s);'
        dados_esporte = Esporte.Get_Dados_Esporte(esporte)
        status = Configuration.Altera_BD(
            Configuration, string_sql_esporte, dados_esporte)
        return status

    def Download_Data():
        response = requests.get(
            "https://www.thesportsdb.com/api/v1/json/2/all_sports.php")
        json_response = response.json()
        dictionary = json.dumps(json_response, sort_keys=True, ensure_ascii=False)
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
    nome = Column(String(100), nullable=False)
    nome_esporte = Column(ForeignKey('trabalho.esporte.nome'), nullable=False)

    esporte = relationship('Esporte')

    def __init__(self, idLeague, strLeague, strSport):
        self.id = idLeague
        self.nome = strLeague
        self.nome_esporte = strSport

    # Função para criar uma liga
    def Cria_Liga(dados_liga):
        nova_liga = Liga(int(dados_liga[0]), str(dados_liga[1]), str(dados_liga[2]))
        return nova_liga

    # Função para inserção de novas ligas no banco
    def INSERT(liga):
        string_sql_liga = 'INSERT INTO trabalho.liga(id, nome, nome_esporte) VALUES (%s, %s, %s);'
        dados_liga = Liga.Get_Dados_Liga(liga)
        status = Configuration.Altera_BD(
            Configuration, string_sql_liga, dados_liga)
        return status

    def Download_Data():
        response = requests.get(
            "https://www.thesportsdb.com/api/v1/json/2/all_leagues.php")
        json_response = response.json()
        dictionary = json.dumps(json_response, sort_keys=True, ensure_ascii=False)
        return dictionary

    def Parse_Data(dados_api):
        aux = []
        for r in findall('"idLeague": "{}", ', dados_api):
            aux.append(r[0])
        ids = np.array(aux)

        aux = []
        for r in findall('"strLeague": "{}", ', dados_api):
            aux.append(r[0])
        nomes = np.array(aux)

        aux = []
        for r in findall('"strSport": "{}"}', dados_api):
            aux.append(r[0])
        esportes = np.array(aux)

        lista_dados = [ids, nomes, esportes]
        return lista_dados

    def Get_Dados_Liga(self):
        dados = [self.id, self.nome, self.nome_esporte]
        return dados


class Time(Base):
    __tablename__ = 'time'
    __table_args__ = {'schema': 'trabalho'}

    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    pais = Column(String(20), nullable=False)
    nome_alternativo = Column(String(100))
    esporte = Column(ForeignKey('trabalho.esporte.nome'), nullable=False)
    ano_formacao = Column(Integer, nullable=False)

    esporte1 = relationship('Esporte')

    def __init__(self, idTeam, strTeam, strCountry, strAlternate, strSport, intFormedYear):
        self.id = idTeam
        self.nome = strTeam
        self.pais = strCountry
        self.nome_alternativo = strAlternate
        self.esporte = strSport
        self.ano_formacao = intFormedYear

    # Função para criar uma liga
    def Cria_Time(dados_time):
        novo_time = Time(
            int(dados_time[0]), str(dados_time[1]), str(dados_time[2]), str(dados_time[3]), str(dados_time[4]),
            int(dados_time[5]))
        return novo_time

    # Função para inserção de novas ligas no banco
    def INSERT(time):
        string_sql_time = 'INSERT INTO trabalho.time(id, nome, pais, nome_alternativo, esporte, ano_formacao) VALUES (%s, %s, %s, %s, %s, %s);'
        dados_time = Time.Get_Dados_Time(time)
        status = Configuration.Altera_BD(
            Configuration, string_sql_time, dados_time)
        return status

    def Download_Data():
        dict_list = []
        x = 0
        response = requests.get(
            "https://www.thesportsdb.com/api/v1/json/2/all_leagues.php")
        json_response = response.json()
        dictionary = json.dumps(json_response, sort_keys=True, ensure_ascii=False)
        for r in findall('"strLeague": "{}", ', dictionary):
            aux = str(r[0])
            aux.strip()
            league_link = aux.replace(" ", "%20")
            actual_response = requests.get(
                "https://www.thesportsdb.com/api/v1/json/2/search_all_teams.php?l="+league_link)
            actual_json_response = actual_response.json()
            actual_dictionary = json.dumps(actual_json_response, sort_keys=True, ensure_ascii=False)
            dict_list.append(actual_dictionary)
            x += 1
            if x == 30:
                break
        return dict_list

    def Parse(dados_api, string):
        aux = []
        for r in findall(string, dados_api):
            aux.append(r[0])
        dados = np.asanyarray(aux)
        return dados

    def Parse_Data(dados_api):
        ids = Time.Parse(dados_api, '"idTeam": "{}", ')
        nomes = Time.Parse(dados_api, '"strTeam": "{}", ')
        paises = Time.Parse(dados_api, '"strCountry": "{}", ')
        nomes_alternativos = Time.Parse(dados_api, '"strAlternate": "{}", ')
        esportes = Time.Parse(dados_api, '"strSport": "{}", ')
        anos_formacao = Time.Parse(dados_api, '"intFormedYear": "{}", ')
        lista_dados = [ids, nomes, paises, nomes_alternativos, esportes, anos_formacao]
        return lista_dados

    def Get_Dados_Time(self):
        dados = [self.id, self.nome, self.pais, self.nome_alternativo, 
        self.esporte, self.ano_formacao]
        return dados


class Jogador(Base):
    __tablename__ = 'jogador'
    __table_args__ = {'schema': 'trabalho'}

    id = Column(Integer, primary_key=True)
    data_nasc = Column(Date, nullable=False)
    id_time = Column(ForeignKey('trabalho.time.id'), nullable=False)
    local_nasc = Column(String(50), nullable=False)
    descricao = Column(Text, nullable=False)
    nome = Column(String(20), nullable=False)
    nacionalidade = Column(String(50), nullable=False)
    esporte = Column(ForeignKey('trabalho.esporte.nome'), nullable=False)

    esporte1 = relationship('Esporte')
    time = relationship('Time')

    def __init__(self, idPlayer, dateBorn, idTeam, strBirthLocation, strDescription, strPlayer, strNationality, strSport):
        self.id = idPlayer
        self.data_nasc = dateBorn
        self.id_time = idTeam
        self.local_nasc = strBirthLocation
        self.descricao = strDescription
        self.nome = strPlayer
        self.nacionalidade = strNationality
        self.esporte = strSport

    # Função para criar uma liga
    def Cria_Jogador(dados_jogador):
        year, month, day = map(int, dados_jogador[1].split("-"))
        dados_jogador[1] = datetime(year, month, day)
        novo_jogador = Jogador(
            int(dados_jogador[0]), dados_jogador[1], int(dados_jogador[2]), 
            str(dados_jogador[3]), str(dados_jogador[4]), str(dados_jogador[5]),
            str(dados_jogador[6]), str(dados_jogador[7]),)
        return novo_jogador

    # Função para inserção de novas ligas no banco
    def INSERT(jogador):
        string_sql_jogador = 'INSERT INTO trabalho.jogador(id, data_nasc, id_time, local_nasc, descricao, nome, nacionalidade, esporte) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
        dados_jogador = Jogador.Get_Dados(jogador)
        status = Configuration.Altera_BD(
            Configuration, string_sql_jogador, dados_jogador)
        return status

    def Download_Data():
        dict_list = []
        x = 0
        response = requests.get(
            "https://www.thesportsdb.com/api/v1/json/2/searchloves.php?u=zag")
        json_response = response.json()
        dictionary = json.dumps(json_response, sort_keys=True, ensure_ascii=False)
        for r in findall('"idPlayer": "{}", ', dictionary):
            id = str(r[0])
            actual_response = requests.get(
                "https://www.thesportsdb.com/api/v1/json/2/lookupplayer.php?id="+id)
            actual_json_response = actual_response.json()
            actual_dictionary = json.dumps(actual_json_response, sort_keys=True, ensure_ascii=False)
            dict_list.append(actual_dictionary)
        return dict_list

    def Parse(dados_api, string):
        aux = []
        for r in findall(string, dados_api):
            aux.append(r[0])
        dados = np.asanyarray(aux)
        return dados

    def Parse_Data(dados_api):
        ids = Jogador.Parse(dados_api, '"idPlayer": "{}", ')
        datas_nasc = Jogador.Parse(dados_api, '"dateBorn": "{}", ')
        times = Jogador.Parse(dados_api, '"idTeam": "{}", ')
        locais_nasc = Jogador.Parse(dados_api, '"strBirthLocation": "{}", ')
        descricoes = Jogador.Parse(dados_api, '"strDescriptionEN": "{}", ')
        nomes = Jogador.Parse(dados_api, '"strPlayer": "{}", ')
        nacionalidades = Jogador.Parse(dados_api, '"strNationality": "{}", ')
        esportes = Jogador.Parse(dados_api, '"strSport": "{}", ')
        lista_dados = [ids, datas_nasc, times, locais_nasc,
        descricoes, nomes, nacionalidades, esportes]
        return lista_dados

    def Get_Dados(self):
        dados = [self.id, self.data_nasc, self.id_time, self.local_nasc, 
        self.descricao, self.nome, self.nacionalidade, self.esporte]
        return dados


class LigasTime(Base):
    __tablename__ = 'ligas_time'
    __table_args__ = {'schema': 'trabalho'}

    id = Column(Integer, primary_key=True)
    id_time = Column(ForeignKey('trabalho.time.id'), nullable=False)
    id_liga = Column(ForeignKey('trabalho.liga.id'), nullable=False)

    liga = relationship('Liga')
    time = relationship('Time')
