from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def processar(data: dict):
    texto = data.get("texto", "")
    return {
        "original": texto,
        "maiusculo": texto.upper()
    }
