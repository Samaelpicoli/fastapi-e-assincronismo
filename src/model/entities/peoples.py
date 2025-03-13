from sqlalchemy import Column, Integer, String, Table

from src.model.settings.db_metadata import metadata


"""
Define a estrutura da tabela 'pessoas' no banco de dados.

Este módulo contém a representação da entidade 'Pessoas' utilizando 
SQLAlchemy, que será usada nas operações de banco de dados.
"""

Pessoas = Table(
    "pessoas", metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)