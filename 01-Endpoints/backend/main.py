from fastapi import FastAPI, Path
from schemas.tache import Tache

app = FastAPI(
    title="API Todo List",
    description="API de gestion de tâches, réalisée avec FastAPI."
)


@app.get("/taches/",
    summary="Lister toutes les tâches",
    description="Retourne l'ensemble des tâches enregistrées.",
    response_description="La liste des tâches",
    tags=["Tâches"],
)
def get_all_taches():
    return {"message": "Fonction qui va récupérer toutes les tâches"}


@app.post("/taches/",
    status_code=201,
    summary="Créer une tâche",
    description="Crée une nouvelle tâche à partir des données envoyées dans le corps de la requête.",
    response_description="La tâche créée",
    tags=["Tâches"],
)
def create_tache(t: Tache):
    return {"message": f"Tâche créée. Tâche : {t}"}


@app.get("/taches/{id}",
    summary="Récupérer une tâche",
    description="Retourne la tâche correspondant à l'identifiant fourni.",
    response_description="La tâche demandée",
    tags=["Tâches"],
)
def get_tache_by_id(id: int = Path(..., ge=1, description="Identifiant de la tâche")):
    return {"message": f"Fonction qui va récupérer la tâche avec l'ID {id}"}


@app.put("/taches/{id}",
    summary="Mettre à jour une tâche",
    description="Remplace les données de la tâche correspondant à l'identifiant fourni.",
    response_description="La tâche mise à jour",
    tags=["Tâches"],
)
def update_tache(id: int, t: Tache):
    return {"message": f"Fonction qui va mettre à jour la tâche avec l'ID {id}. Nouvelle tâche : {t}"}


@app.delete("/taches/{id}",
    status_code=204,
    summary="Supprimer une tâche",
    description="Supprime définitivement la tâche correspondant à l'identifiant fourni.",
    tags=["Tâches"],
)
def delete_tache(id: int):
    return {"message": f"Fonction qui va supprimer la tâche avec l'ID {id}"}