from shared.database import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
)

class User(Base):
    __tablename__ = 'users_tb'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(320), unique=True)
    senha = Column(String(320))
    nome = Column(String(100))
    idade = Column(Integer)
    genero = Column(Integer)
    estado = Column(String(30))
    cidade = Column(String(100))
    trilha = Column(Integer)
    conhece_a_cultura = Column(Integer)
    mais_se_interessa = Column(Integer)
