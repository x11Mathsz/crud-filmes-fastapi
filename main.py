from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, create_tables
from schemas import Filme, FilmeCreate
import crud

# Criar instância do FastAPI
app = FastAPI(title="CRUD de Filmes", description="API simples para gerenciar filmes")

# Criar tabelas no banco ao iniciar
@app.on_event("startup")
def startup_event():
    create_tables()

# Rota inicial
@app.get("/")
def read_root():
    return {"message": "API de Filmes funcionando! Acesse /docs para ver a documentação"}

# GET /filmes - Lista todos os filmes
@app.get("/filmes", response_model=list[Filme])
def listar_filmes(db: Session = Depends(get_db)):
    filmes = crud.get_filmes(db)
    return filmes

# POST /filmes - Adiciona um novo filme
@app.post("/filmes", response_model=Filme)
def criar_filme(filme: FilmeCreate, db: Session = Depends(get_db)):
    return crud.create_filme(db, filme)

# GET /filmes/{id} - Busca um filme pelo ID
@app.get("/filmes/{filme_id}", response_model=Filme)
def buscar_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = crud.get_filme(db, filme_id)
    if filme is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme

# PUT /filmes/{id} - Atualiza um filme existente
@app.put("/filmes/{filme_id}", response_model=Filme)
def atualizar_filme(filme_id: int, filme: FilmeCreate, db: Session = Depends(get_db)):
    filme_atualizado = crud.update_filme(db, filme_id, filme)
    if filme_atualizado is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme_atualizado

# DELETE /filmes/{id} - Deleta um filme
@app.delete("/filmes/{filme_id}")
def deletar_filme(filme_id: int, db: Session = Depends(get_db)):
    sucesso = crud.delete_filme(db, filme_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return {"message": "Filme deletado com sucesso"}

# POST /importar/{titulo} - Importa filme da API OMDb
@app.post("/importar/{titulo}", response_model=Filme)
def importar_filme(titulo: str, db: Session = Depends(get_db)):
    filme = crud.importar_filme_omdb(db, titulo)
    if filme is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado na API OMDb")
    return filme
