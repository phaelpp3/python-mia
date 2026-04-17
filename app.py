from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    texto: str

@app.get("/")
def home():
    return {"msg": "Python funcionando"}

@app.post("/processar")
def processar(data: Input):
    return {
        "original": data.texto,
        "maiusculo": data.texto.upper()
    }
