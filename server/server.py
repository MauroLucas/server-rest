from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

db = psycopg2.connect(
    user="postgres",
    password="root",
    host="localhost",
    port='5432',
    database = "chefencasa"
)

cursor = db.cursor()

#Instancia de FastAPI
app = FastAPI()

#BaseModel valida los tipos de datos
class Receta(BaseModel):
    titulo: str
    id_usuario: int
    descripcion: Optional[str]

class Message(BaseModel):
    sender_id: int
    recipient_id: int
    subject: str
    message: str

@app.get("/")
def index():
    return {"mensaje" : "Hello, World"}

@app.get("/receta/{id}")
def mostrar_receta(id: int):
    return {"id receta" : id}

@app.post("/receta")
def insertar_receta(receta: Receta):
    return {"mensaje" : f"receta {receta.titulo} insertado"}

@app.get("/user/{id}")
def get_user(id : int):
    query = "SELECT s.id, s.name, s.last_name, s.email, s.popularity FROM users as s WHERE s.id = '{0}'".format(id)
    cursor.execute(query)
    result = cursor.fetchone()
    return {"id" : result[0], "name" : result[1] , "last_name" : result[2] , "email" : result[3] , "popularity" : result[4]}

@app.post("/user/message")
def create_message(message: Message):
    query = "INSERT INTO messages (sender_id,recipient_id,subject,message) VALUES('{0}','{1}','{2}','{3}')".format(message.sender_id,message.recipient_id,message.subject,message.message)
    cursor.execute(query)
    db.commit() 
    return {"sender_id" : message.sender_id, "recipient_id" : message.recipient_id,"subject": message.subject, "message" : message.message, }

