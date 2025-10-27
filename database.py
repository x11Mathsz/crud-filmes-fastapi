from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# URL de conexão com PostgreSQL
DATABASE_URL = "postgresql://postgres:postgres@db:5432/filmesdb"

# Criar engine
engine = create_engine(DATABASE_URL)

# Criar sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para criar as tabelas
def create_tables():
    Base.metadata.create_all(bind=engine)

# Função para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
