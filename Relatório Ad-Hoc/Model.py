from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from decimal import *

Base = declarative_base()
metadata = Base.metadata


class Esporte(Base):
    __tablename__ = 'esporte'
    __table_args__ = {'schema': 'trabalho'}

    id_esporte = Column(Integer, primary_key=True)
    formato = Column(String(30), nullable=False)
    nome = Column(String(20), nullable=False, unique=True)
    descricao = Column(Text, nullable=False)

class Liga(Base):
    __tablename__ = 'liga'
    __table_args__ = {'schema': 'trabalho'}

    id_liga = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    nome_esporte = Column(ForeignKey('trabalho.esporte.nome'), nullable=False)

    esporte = relationship('Esporte')

class Equipe(Base):
    __tablename__ = 'equipe'
    __table_args__ = {'schema': 'trabalho'}

    id_equipe = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False, unique=True)
    pais = Column(String(20), nullable=False)
    nome_alternativo = Column(String(100))
    esporte = Column(ForeignKey('trabalho.esporte.nome'), nullable=False)
    ano_formacao = Column(Integer, nullable=False)

    esporte1 = relationship('Esporte')

   
class Jogador(Base):
    __tablename__ = 'jogador'
    __table_args__ = {'schema': 'trabalho'}

    id_jogador = Column(Integer, primary_key=True)
    data_nasc = Column(Date, nullable=False)
    id_equipe = Column(ForeignKey('trabalho.equipe.id_equipe'), nullable=False)
    local_nasc = Column(String(50), nullable=False)
    descricao = Column(Text, nullable=False)
    nome = Column(String(20), nullable=False)
    nacionalidade = Column(String(50), nullable=False)
    esporte = Column(ForeignKey('trabalho.esporte.nome'), nullable=False)

    esporte1 = relationship('Esporte')
    equipe = relationship('Equipe')