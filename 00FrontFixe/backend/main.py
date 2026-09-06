from fastapi import FastAPI

app = FastAPI()

@app.get("/taches/")
def get_all_taches():
    return {"message": "Fonction qui va récupérer toutes les tâches"}

@app.get("/taches/{id}")
def get_tache_by_id(id: int):
    return {"message": f"Fonction qui va récupérer la tâche avec l'ID {id}"}