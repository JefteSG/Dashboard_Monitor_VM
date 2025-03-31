from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://root:123@db/monitor_db")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from db import engine
from models import Base  # Certifique-se de que a classe ServerMonitor está aqui

# Cria todas as tabelas definidas no modelo, se não existirem
Base.metadata.create_all(bind=engine)
