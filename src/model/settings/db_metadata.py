"""
Define a metadata do banco de dados.

O objeto `metadata` armazena as definições das tabelas do banco e é 
usado para configurar as entidades do SQLAlchemy.
"""

from sqlalchemy import MetaData

metadata = MetaData()
