from fastapi import FastAPI

app = FastAPI()

@app.post("/mundo")
def processar(data: dict):
    texto = data.get("texto", "")
    return {
        "original": texto
