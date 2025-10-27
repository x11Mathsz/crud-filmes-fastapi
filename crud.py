from sqlalchemy.orm import Session
from models import Filme
from schemas import FilmeCreate
import requests

def get_filmes(db: Session):
    """Busca todos os filmes"""
    return db.query(Filme).all()

def get_filme(db: Session, filme_id: int):
    """Busca um filme pelo ID"""
    return db.query(Filme).filter(Filme.id == filme_id).first()

def create_filme(db: Session, filme: FilmeCreate):
    """Cria um novo filme"""
    db_filme = Filme(**filme.dict())
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme

def update_filme(db: Session, filme_id: int, filme_data: FilmeCreate):
    """Atualiza um filme existente"""
    filme = db.query(Filme).filter(Filme.id == filme_id).first()
    if filme:
        # Atualizar os campos
        filme.titulo = filme_data.titulo
        filme.ano = filme_data.ano
        filme.genero = filme_data.genero
        filme.nota = filme_data.nota
        
        db.commit()
        db.refresh(filme)
        return filme
    return None

def delete_filme(db: Session, filme_id: int):
    """Deleta um filme pelo ID"""
    filme = db.query(Filme).filter(Filme.id == filme_id).first()
    if filme:
        db.delete(filme)
        db.commit()
        return True
    return False

def importar_filme_omdb(db: Session, titulo: str):
    """Importa um filme da API OMDb"""
    # Chave da API OMDb - OBTENHA UMA GRATUITA EM: http://www.omdbapi.com/apikey.aspx
    api_key = "427c534"  # Chave de teste - substitua por uma real
    url = f"http://www.omdbapi.com/?t={titulo}&apikey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("Response") == "True":
            # Converter nota para float, tratando casos onde pode ser "N/A"
            nota = 0.0
            if data.get("imdbRating") and data.get("imdbRating") != "N/A":
                try:
                    nota = float(data.get("imdbRating"))
                except ValueError:
                    nota = 0.0
            
            filme_data = FilmeCreate(
                titulo=data.get("Title", titulo),
                ano=data.get("Year", "Desconhecido"),
                genero=data.get("Genre", "Desconhecido"),
                nota=nota
            )
            
            return create_filme(db, filme_data)
        else:
            # Log do erro para debug
            error_msg = data.get("Error", "Erro desconhecido")
            print(f"Erro da OMDb API: {error_msg}")
            return None
    except Exception as e:
        print(f"Erro ao importar filme: {e}")
        return None
