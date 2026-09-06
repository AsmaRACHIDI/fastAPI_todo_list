from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def tache_racine():
    return {"message": "Bienvenue sur l'API FastAPI!"}