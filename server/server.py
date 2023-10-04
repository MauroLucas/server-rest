from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

#Instancia de FastAPI
app = FastAPI()

#BaseModel valida los tipos de datos
class Receta(BaseModel):
    titulo: str
    id_usuario: int
    descripcion: Optional[str]

@app.get("/")
def index():
    return {"mensaje" : "Hello, World"}

@app.get("/receta/{id}")
def mostrar_receta(id: int):
    return {"id receta" : id}

@app.post("/receta")
def insertar_receta(receta: Receta):
    return {"mensaje" : f"receta {receta.titulo} insertado"}



