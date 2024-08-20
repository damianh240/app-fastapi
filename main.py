from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor : str
    paginas: int
    aditorial : Optional[str]

@app.get("/")
def index():
    return {"message" : "Hola, FASTAPI!"}

@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return{"data": id}

@app.post("/Libros")
def insertar_Libro(libro: Libro):
    return{"message": f"Libro {libro.titulo} insertado"}