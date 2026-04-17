from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Python funcionando"}

@app.post("/processar")
def processar(data: dict):
    texto = data.get("texto", "")
    return {
        "original": texto,
        "maiusculo": texto.upper()
    }
